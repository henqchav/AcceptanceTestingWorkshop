Feature: To-Do List Manager

  Scenario: Adding a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: Listing all tasks in the to-do list
    Given the to-do list contains the following tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain the following tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |

  Scenario: Marking a task as completed
    Given the to-do list contains the following tasks:
      | Task          | Status    |
      | Buy groceries | Pending   |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Marking a task as pending
    Given the to-do list contains the following tasks:
      | Task          | Status    |
      | Buy groceries | Completed |
    When the user marks task "Buy groceries" as pending
    Then the to-do list should show task "Buy groceries" as pending

  Scenario: Clearing the entire to-do list
    Given the to-do list contains the following tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty.

  Scenario: Verifying the to-do list is empty
    Given the to-do list is empty
    Then the to-do list should be empty.
