#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID and export to CSV
"""
import csv
import requests
from sys import argv


def display():
    """return API data"""
    user_id = int(argv[1])
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == user_id:
            employee_name = u.get('name')
            break

    tasks = requests.get("http://jsonplaceholder.typicode.com/todos")
    employee_tasks = []

    for task in tasks.json():
        if task.get('userId') == user_id:
            task_completed_status = str(task.get('completed'))
            task_title = task.get('title')
            employee_tasks.append([str(user_id), employee_name, task_completed_status, task_title])

    if employee_tasks:
        file_name = f"{user_id}.csv"
        with open(file_name, mode='w', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_writer.writerows(employee_tasks)
        print(f"Data exported to {file_name}")
    else:
        print(f"No tasks found for user ID {user_id}")


if __name__ == "__main__":
    display()
