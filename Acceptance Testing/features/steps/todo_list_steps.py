import builtins
from behave import given, when, then
from todo_list import Task, ToDoListManager


@given("the to-do list is empty")
def step_given_todo_list_empty(context):
    context.todo_manager = ToDoListManager()


@when('the user adds a task "{task_description}"')
def step_when_user_adds_task(context, task_description):
    context.todo_manager.add_task(Task(task_description))


@then('the to-do list should contain "{task_description}"')
def step_then_todo_list_should_contain(context, task_description):
    task_found = any(
        task.description == task_description for task in context.todo_manager.tasks
    )
    assert task_found, f"Task '{task_description}' not found in the to-do list"


@given("the to-do list contains the following tasks")
def step_given_todo_list_contains_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        task = Task(row["Task"])
        if "Status" in row:
            task.status = row["Status"]
        context.todo_manager.add_task(task)


@when("the user lists all tasks")
def step_when_user_lists_all_tasks(context):
    context.output = ""

    def mock_print(value):
        context.output += value + "\n"

    context.real_print = builtins.print

    try:
        builtins.print = mock_print
        context.todo_manager.list_tasks()
    finally:
        builtins.print = context.real_print


@then("the output should contain the following tasks")
def step_then_output_should_contain_tasks(context):
    expected_tasks = [row["Task"] for row in context.table]
    output_tasks = context.output.strip().split("\n")
    assert set(expected_tasks) == set(
        output_tasks
    ), "Output mismatch: Tasks do not match"


@when('the user marks task "{task_description}" as completed')
def step_when_user_marks_task_completed(context, task_description):
    context.todo_manager.mark_task_completed(task_description)


@then('the to-do list should show task "{task_description}" as completed')
def step_then_todo_list_should_show_task_completed(context, task_description):
    task = next(
        (
            task
            for task in context.todo_manager.tasks
            if task.description == task_description
        ),
        None,
    )
    assert task is not None, f"Task '{task_description}' not found in the to-do list"
    assert (
        task.status == "Completed"
    ), f"Task '{task_description}' is not marked as completed"


@when('the user marks task "{task_description}" as pending')
def step_when_user_marks_task_pending(context, task_description):
    context.todo_manager.mark_task_pending(task_description)


@then('the to-do list should show task "{task_description}" as pending')
def step_then_todo_list_should_show_task_pending(context, task_description):
    task = next(
        (
            task
            for task in context.todo_manager.tasks
            if task.description == task_description
        ),
        None,
    )
    assert task is not None, f"Task '{task_description}' not found in the to-do list"
    assert (
        task.status == "Pending"
    ), f"Task '{task_description}' is not marked as pending"


@when("the user clears the to-do list")
def step_when_user_clears_todo_list(context):
    context.todo_manager.clear_tasks()


@then("the to-do list should be empty")
def step_then_todo_list_should_be_empty(context):
    assert len(context.todo_manager.tasks) == 0, "The to-do list is not empty"


@then("the to-do list should be empty.")
def step_then_todo_list_should_be_empty_dot(context):
    assert len(context.todo_manager.tasks) == 0, "The to-do list is not empty"
