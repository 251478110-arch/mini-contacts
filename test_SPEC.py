import solution_V0

def test_init():
    result = solution_V0.run_command("init")
    assert result == "Contact storage initialized"


def test_add():
    solution_V0.run_command("init")
    result = solution_V0.run_command("add 1 Ahmet 5551234")
    assert result == "Contact added"


def test_add_missing_arguments():
    result = solution_V0.run_command("add")
    assert result == "Error: Missing arguments"


def test_unknown_command():
    result = solution_V0.run_command("hello")
    assert result == "Error: Unknown command"


def test_list_not_implemented():
    result = solution_V0.run_command("list")
    assert result == "Not implemented"


def test_search_not_implemented():
    result = solution_V0.run_command("search 1")
    assert result == "Not implemented"


def test_delete_not_implemented():
    result = solution_V0.run_command("delete 1")
    assert result == "Not implemented"


def test_export_not_implemented():
    result = solution_V0.run_command("export file.txt")
    assert result == "Not implemented"


def test_second_add():
    solution_V0.run_command("init")
    result = solution_V0.run_command("add 2 Ali 5550000")
    assert result == "Contact added"


def test_add_other_contact():
    solution_V0.run_command("init")
    result = solution_V0.run_command("add 3 Veli 5559999")
    assert result == "Contact added"