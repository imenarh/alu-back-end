#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}", timeout=10
    )
    user_data = user_response.json()

    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id},
        timeout=10,
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
