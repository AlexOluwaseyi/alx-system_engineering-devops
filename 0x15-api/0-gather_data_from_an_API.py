#!/usr/bin/python3

"""
Python script that, using this REST API (https://jsonplaceholder.typicode.com/)
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


def get_todos():
    """
    Function definition to retrieve data from API
    """

    # Check if Employee ID has been provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <ID>")
        sys.exit(1)

    # Base URL
    base_url = "https://jsonplaceholder.typicode.com/users"

    employee_id = sys.argv[1]

    # Get Employee name
    response = requests.get("{}/{}".format(base_url, employee_id))
    if response.status_code == 200:
        employee = response.json()
        employee_name = employee['name']

    # Get Todos
    response = requests.get("{}/{}/todos".format(base_url, employee_id))
    if response.status_code == 200:
        todos = response.json()
        total_todos = len(todos)
        completed_todos = [todo for todo in todos if todo['completed']]
        total_completed = len(completed_todos)

    # Extract titles from completed todos
    completed_titles = [todo['title'] for todo in completed_todos]

    print("Employee {} is done with tasks({}/{})".format(
        employee_name, total_completed, total_todos
        ))
    for title in completed_titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    """Function call"""
    get_todos()
