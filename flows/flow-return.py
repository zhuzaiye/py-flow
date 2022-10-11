#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# DESC:

from prefect import flow, task


# Raise an exception: the flow is immediately marked as failed
# @flow
# def always_fails_flow():
#     raise ValueError("This flow immediately fails")


# Return None: A flow with no return statement is determined by the state of all of its task runs.
@task
def always_fails_task():
    raise ValueError("I fail successfully")


@task
def always_succeeds_task():
    print("I'm fail safe!")
    return "success"


@flow
def always_fails_flow():
    always_fails_task.submit().result(raise_on_failure=False)
    always_succeeds_task()


# Return a future: If a flow returns one or more futures,
# the final state is determined based on return argument's states.

# Return multiple states or futures: If a flow returns a mix of futures and states, the final state is determined by
# resolving all futures to states, then determining if any of the states are not COMPLETED.

# Return a manual state: If a flow returns a manually created state,
# the final state is determined based on the return value

# Return an object: If the flow run returns any other object, then it is marked as completed.

if __name__ == '__main__':
    always_fails_flow()
