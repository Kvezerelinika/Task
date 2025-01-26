import pytest
from unittest.mock import patch
from project import Task

@pytest.fixture
def task_instance():
    return Task()

def test_add_task(capsys, task_instance, monkeypatch):
    inputs = iter(['Task Title', 'Task Description', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Task added succesfully!"
    assert task_instance.task_data[-1] == {"title": "Task Title", "description": "Task Description", "date": "05/07/2024"}

def test_add_task_invalid_date_format(capsys, task_instance, monkeypatch):

    inputs = iter(['Task Title', 'Task Description', 'Invalid Date Format', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    captured = capsys.readouterr()
    assert "Deadline is mandatory, correct format is (mm/dd/yyyy)! " in captured.out
    assert task_instance.task_data[-1] == {"title": "Task Title", "description": "Task Description", "date": "05/07/2024"}

def test_add_task_empty_title(capsys, task_instance, monkeypatch):

    inputs = iter(['', 'Task Title', 'Task Description', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    captured = capsys.readouterr()
    assert "Please type title of the task!" in captured.out
    assert task_instance.task_data[-1] == {"title": "Task Title", "description": "Task Description", "date": "05/07/2024"}

def test_add_task_empty_desc(capsys, task_instance, monkeypatch):

    inputs = iter(['Task Title', '', 'Task Description', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    captured = capsys.readouterr()
    assert "Please type description of the task!" in captured.out
    assert task_instance.task_data[-1] == {"title": "Task Title", "description": "Task Description", "date": "05/07/2024"}


def test_add_task_empty_date(capsys, task_instance, monkeypatch):

    inputs = iter(['Task Title', 'Task Description', '', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    captured = capsys.readouterr()
    assert "Deadline is mandatory, correct format is (mm/dd/yyyy)! " in captured.out
    assert task_instance.task_data[-1] == {"title": "Task Title", "description": "Task Description", "date": "05/07/2024"}

def test_saving(task_instance, monkeypatch):
    inputs = iter(['Task Title', 'Task Description', '05/07/2024'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    task_instance.add_task()
    with open('tasks.txt', 'r') as file_rf:
        for line in file_rf:
            last_line = line
    assert last_line.strip() == 'Task Title,Task Description,05/07/2024'

def test_delete_task(task_instance):

    with open("tasks.txt", 'r') as file_rf:
        num_tasks_before = sum(1 for _ in file_rf)

    input_mock = "1\n"
    with patch('builtins.input', return_value=input_mock):
        task_instance.delete_task()

    with open("tasks.txt", 'r') as file_rf:
        num_tasks_after = sum(1 for _ in file_rf)

    assert num_tasks_after == num_tasks_before - 1
    assert num_tasks_after < num_tasks_before

def test_modify_task(task_instance, capsys):

    with patch('builtins.input', side_effect=["1", "Edited Title", "Edited Description", "11/11/2024"]):
        task_instance.modify_task()

    captured = capsys.readouterr()
    assert "Task updated!" in captured.out
    assert task_instance.task_data[0]['title'] == "Edited Title"
    assert task_instance.task_data[0]['description'] == "Edited Description"
    assert task_instance.task_data[0]['date'] == "11/11/2024"
