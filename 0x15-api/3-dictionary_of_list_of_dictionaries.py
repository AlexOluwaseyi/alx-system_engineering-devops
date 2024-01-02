#!/usr/bin/python3

"""
Python script that, using this REST API (https://jsonplaceholder.typicode.com/)
for a given employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
import sys


def export_dict():
    """
    Function definition to retrieve data from API
    """

    # Base URL
    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Empty dictionary
    full_dict = {}

    # Get Employee name
    response = requests.get("{}".format(user_url))
    if response.status_code == 200:
        users = response.json()
        for user in users:
            user_id = user['id']
            username = user['username']

            # Get Todos status
            resp = requests.get("{}/{}/todos".format(user_url, user_id))
            if resp.status_code == 200:
                todos = resp.json()

                to_dict = {
                        user_id: [
                            {"task": todo['title'],
                                "completed": todo['completed'],
                                "username": username} for todo in todos
                            ]
                        }

                # Write each to the empty dictionary for every user in users
                full_dict[user_id] = to_dict

    # Write dict to JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(full_dict, json_file)


if __name__ == "__main__":
    """Function call"""
    export_dict()
