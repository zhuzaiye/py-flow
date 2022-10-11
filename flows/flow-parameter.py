#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# DESC: Flows can be called with both positional and keyword arguments
# These arguments are resolved at runtime into a dictionary of parameters mapping name to value

from prefect import flow, task
from pydantic import BaseModel


class Model(BaseModel):
    a: int
    b: int
    c: str


@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")


@flow
def model_validator(model: Model):
    printer(model)


if __name__ == '__main__':
    model_validator({"a": 42, "b": 0, "c": 55})
