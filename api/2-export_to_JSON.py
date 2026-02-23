#!/usr/bin/python3
"""Export TODO list data for a given employee to JSON format."""

import json
import requests
import sys


def fetch_employee(user_id):
    """Return employee data for a given user id."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def fetch_todos(user_id):
    """Return all TODO items owned by the given user id."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    if response.status_code != 200:
        return []
    return response.json()


def export_to_json(user_id):
    """Export all TODO tasks for one employee to USER_ID.json."""
    employee = fetch_employee(user_id)
    if employee is None:
        return

    username = employee.get("username")
    todos = fetch_todos(user_id)

    data = {
        str(user_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username,
            }
            for todo in todos
        ]
    }

    filename = "{}.json".format(user_id)
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    export_to_json(employee_id)
