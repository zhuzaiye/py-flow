#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# DESC: 创建，运行flow

from prefect import flow


# @flow
# def my_flow():
#     print("Hello Prefect-Flow")
#
#
# @flow(name="My Flow")
# def my_flow_with_name():
#     print("Hello Prefect-Flow")


@flow(name="My Flow",
      description="My flow using decorator")
def my_flow_with_name_desc():
    print("Hello Prefect-Flow")


if __name__ == '__main__':
    # my_flow()
    # my_flow_with_name()
    my_flow_with_name_desc()
