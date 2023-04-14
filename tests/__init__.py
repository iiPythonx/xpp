# Modules
from rich import print as rp
from rich.table import Table

# Load xpp
from xpp import Interpreter
from xpp.core.sections import Section

# Fake out the x++ interpreter
inter = Interpreter("_tests.xpp", [])
section = Section("_tests.main", "", [], 1, [])
section.initialize(inter.memory)
inter.stack.append(section)

# Start running x++ code
def start_tests(name: str, tests: list) -> None:
    table = Table(title = f"x++ {name} Test Results")
    [table.add_column(c) for c in ["Expression", "x++", "Expected", "Result"]]
    for test in tests:
        try:
            resp = inter.execute(test[0])

        except Exception as e:
            resp = type(e).__name__

        table.add_row(
            str(test[0]),
            str(resp),
            str(test[1]),
            "[green]✓ PASS[/]" if resp == test[1] else "[red]✕ FAIL[/]"
        )

    rp(table)
