#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# DESC:

from prefect import flow, task


@task(name="Task: Print Hello")
def print_hello(name):
    msg = f"Hello {name}"
    print(msg)
    return msg


# @flow(name="Subflow: My Flow")
# def my_subflow(msg):
#     print(f"Subflow says: {msg}")


@flow(name="Normal: Hello Flow")
def hello_world(name="world"):
    message = print_hello(name)
    # my_subflow(message)


if __name__ == '__main__':
    hello_world("Marvin")

"""
1. First: create parent flow
2. Second: create and run task by Sequential way, then finished
3. Third: create and run subflow by Sequential way, then finished
4. Fourth: finish parent flow

22:12:38.041 | INFO    | prefect.engine - Created flow run 'tricky-fulmar' for flow 'Normal: Hello Flow'
22:12:38.260 | INFO    | Flow run 'tricky-fulmar' - Created task run 'Task: Print Hello-1fa5169b-0' for task 'Task: Print Hello'
22:12:38.260 | INFO    | Flow run 'tricky-fulmar' - Executing 'Task: Print Hello-1fa5169b-0' immediately...
Hello Marvin
22:12:38.354 | INFO    | Task run 'Task: Print Hello-1fa5169b-0' - Finished in state Completed()
22:12:38.463 | INFO    | Flow run 'tricky-fulmar' - Created subflow run 'funny-locust' for flow 'Subflow: My Flow'
Subflow says: Hello Marvin
22:12:38.635 | INFO    | Flow run 'funny-locust' - Finished in state Completed()
22:12:38.682 | INFO    | Flow run 'tricky-fulmar' - Finished in state Completed('All states completed.')
"""
