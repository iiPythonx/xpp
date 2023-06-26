# Copyright 2023 iiPython

# Modules
import operator
from typing import Any, Tuple
from xpp.modules.ops import opmap

from .analysis import FlowTree

# Helper functions
string_block_starts = ["\"", "'"]
math_ops = ["add", "sub", "div", "mul", "pow"]
str_ops = ["chr", "flt", "idx", "int", "len", "lwr", "str", "upr"]
requires_output_ops = math_ops + str_ops + ["rng"]

def is_number(value: Any) -> bool:
    if isinstance(value, (int, float)):
        return True

    return (value[0].isdigit()) or (value[0] in ["-", "+"])

def is_literal(value: Any) -> bool:
    if not isinstance(value, str):
        return True

    return is_number(value) or \
        ((value[0] in string_block_starts) and (value[-1] in string_block_starts))

# Simple per-operator optimizations
def recurse_sub_operations(tree: FlowTree) -> Tuple[FlowTree, dict]:
    """Takes a :class:`FlowTree` and performs basic optimizations on a per-operator
    basis. This is currently just mathematical operators, but more niche optimizations
    are soon to come.

    Parameters:
        tree (:class:`FlowTree`): The :class:`FlowTree` to modify

    Returns:
        :class:`FlowTree`: The modified :class:`FlowTree`
        :class:`dict`: A count of every variable in the :class:`FlowTree` (for recurse_sub_variables)
    """
    optimized_tree, variable_counts = [], {}
    for line_num, line in enumerate(tree):
        op_name, do_append = line[0].__name__, True

        # Remove useless builtin calls
        if op_name in requires_output_ops:
            if not [a for a in line[1:] if a[0] == "?"]:
                do_append = False

        # Math optimizations
        if op_name in math_ops:
            support_opt = True
            for arg in line[:-1][1:]:
                if not is_number(arg):
                    support_opt = False

            if support_opt:
                result, operator_fn = float(line[1]), getattr(operator, op_name if op_name != "div" else "truediv")
                for item in line[2:][:-1]:
                    result = operator_fn(result, float(item))

                line = (opmap["var"], line[-1].lstrip("?"), result)

        # Handle merging tree
        if do_append:
            optimized_tree.append(line)

            # Count variable names
            for v in [a for a in line[1:] if isinstance(a, str) and (a[0] != "?")]:
                variable_counts[v] = variable_counts.get(v, []) + [len(optimized_tree) - 1]

    return optimized_tree, variable_counts

# More complex one-time-variable substitutions
def recurse_sub_variables(optimized_tree: FlowTree, variable_counts: dict) -> None:
    """Takes a :class:`FlowTree` and :class:`dict` containing variable counts, then removes
    variables that are only used once; thereby reducing the number of operations in static apps.

    Parameters:
        optimized_tree (:class:`FlowTree`): The :class:`FlowTree` to modify (shallow)
        variable_counts (:class:`dict`): A dictionary of `{ varname: [ found_on_line_numbers ] }` key-value pairs

    For example, in the following:
    var x 5
    prt x

    `x` is referenced on lines 1 and 2, meaning `variable_counts` would be `{ "x": [1, 2] }`.
    """
    var_statements, subbed = [ln for ln in optimized_tree if ln and (ln[0] == opmap["var"])], False
    for variable, var_lines in variable_counts.items():
        if (len(var_lines) != 2) or not all([optimized_tree[ln] for ln in var_lines]):
            continue

        # Guess the current value
        var_value = None
        for line in var_statements:
            if line[1] != variable:
                continue

            var_value = line[2]

        if not is_literal(var_value):
            continue  # Ignore this variable, too complicated for me

        # Replace lines
        optimized_tree[var_lines[1]] = [
            p if p != variable else var_value
            for p in list(optimized_tree[var_lines[1]])
        ]
        optimized_tree[var_lines[0]], subbed = None, True

    # Keep recursing as long as we're changing things
    if subbed:
        recurse_sub_variables(optimized_tree, variable_counts)

# Handle optimizing a flow tree
def optimize(tree: FlowTree) -> FlowTree:
    """Takes a :class:`FlowTree` and performs various optimizations on it to reduce the amount
    of operator calls and parsing required by the interpreter. It currently calls `recurse_sub_operations`
    and `recurse_sub_variables` recursively until `recurse_sub_operations` returns `False`.

    Parameters:
        tree (:class:`FlowTree`): The :class:`FlowTree` to modify

    Returns:
        :class:`FlowTree`: The optimized :class:`FlowTree`
    """
    changed = True
    while changed:
        ntree, vcounts = recurse_sub_operations([obj for obj in tree if obj is not None])
        changed = tree != ntree
        tree = ntree
        recurse_sub_variables(tree, vcounts)

    return tree
