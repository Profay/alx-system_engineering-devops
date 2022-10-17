#!/usr/bin/python3
"""This module gets employer todo list from
https://jsonplaceholder.typicode.com/todos/
"""

import json
import requests
import sys

def get_user_todo_list():
    employee_id = sys.argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    url2 = '%s/todos' % url1
    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()
    completed_todo = []
    for todo in todo_list:
        if todo.get('completed') == True:
            completed_todo.append(todo.get('title'))

    print("First line: Employee {} is done with tasks({}/{}): \n"
    .format(user.get('name'), len(completed_todo), len(todo_list)))
    


if __name__ == '__main__':
    todo_list = get_user_todo_list()
