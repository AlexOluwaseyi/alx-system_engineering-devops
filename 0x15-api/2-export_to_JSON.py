#!/usr/bin/python3

"""
Python script that, using this REST API (https://jsonplaceholder.typicode.com/)
for a given employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
import sys


def export_csv():
    """
    Function definition to retrieve data from API
    """

    # Check if Employee ID has been provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <ID>")
        sys.exit(1)

    # Base URL
    user_url = "https://jsonplaceholder.typicode.com/users"

    # Get Employee name
    response = requests.get("{}".format(user_url))
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == int(sys.argv[1]):
                user_id = user['id']
                username = user['username']

    # Get Todos status
    response = requests.get("{}/{}/todos".format(user_url, sys.argv[1]))
    if response.status_code == 200:
        todos = response.json()

    json_data = {
            user_id: [
                {"task": todo['title'], "completed": todo['completed'],
                    "username": username} for todo in todos
                ]
            }

    # Write JSON to file
    filename = str(user_id) + ".json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    """Function call"""
    export_csv()
