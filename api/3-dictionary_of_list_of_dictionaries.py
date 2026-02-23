#!/usr/bin/python3
"""Export TODO list data for all employees to JSON format."""

import json
import requests


def fetch_users():
    """Return all users from JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def fetch_todos():
    """Return all TODO items from JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def export_all_to_json():
    """Export all employees and their tasks to todo_all_employees.json."""
    users = fetch_users()
    todos = fetch_todos()

    usernames = {user.get("id"): user.get("username") for user in users}
    data = {str(user.get("id")): [] for user in users}

    for todo in todos:
        user_id = todo.get("userId")
        key = str(user_id)
        if key not in data:
            data[key] = []

        data[key].append(
            {
                "username": usernames.get(user_id),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
        )

    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    export_all_to_json()
