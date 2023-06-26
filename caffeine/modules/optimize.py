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
    var_statements, subbed = [(i, ln) for i, ln in enumerate(optimized_tree) if ln and (ln[0] == opmap["var"])], False

    # Clean up reassigned variables
    for i, var in enumerate(var_statements[::-1]):
        for other_var in var_statements[:-i]:
            if (other_var[1][1] == var[1][1]) and (other_var[0] == var[0] - 1):
                var_statements.remove(other_var)
                optimized_tree.remove(other_var[1])
                variable_counts[var[1][1]].remove(other_var[0])

    for variable, var_lines in variable_counts.items():
        if (len(var_lines) < 2) or not all([optimized_tree[ln] for ln in var_lines]):
            continue

        # Guess the current value
        var_values = [vs for vs in var_statements if vs[1][1] == variable]
        for ln in var_lines:
            line = optimized_tree[ln]
            if (line[0].__name__ == "var") and (line[1] == variable):
                continue

            possible_vals = [v for v in var_values if (v[0] <= ln) and (optimized_tree[v[0]] is not None)]
            if not possible_vals:
                break

            value = possible_vals[-1][1][2]
            if not is_literal(value):
                break  # Ignore this variable, too complicated for me

            elif variable not in line:
                break

            optimized_tree[ln] = [
                p if p != variable else value
                for p in list(line)
            ]

            # Remove the previous line from existance
            # Why not just use (ln - 1)? I have no clue, but it doesn't work sometimes.
            # Why does THIS work? Absolutely no fuckin' idea.
            if optimized_tree[possible_vals[0][0]] != optimized_tree[ln]:
                optimized_tree[possible_vals[0][0]] = None

            else:
                optimized_tree[ln - 1] = None

            subbed = True

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
