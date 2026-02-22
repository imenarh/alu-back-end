#!/usr/bin/python3
"""Fetch and display an employee TODO list progress from a REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_data = user_response.json()

    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id},
    )
    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), len(done_tasks), total_tasks
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
