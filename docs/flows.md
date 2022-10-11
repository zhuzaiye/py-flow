# Flows

> `flow`在python中是一个单独的函数。是Prefect中不需要依赖引擎等支持的独立运行的模块。

## Overview

1. 从`函数`到`flow`

`Prefect`使用`@flow`将普通函数转换成`Prefect`的flow函数。
flow函数拥有普通函数行为属性的同时，还具备一下功能：

- 运行`状态可观察`
- 输入`参数可验证`
- 运行`失败可重试`
- 运行`超时可限制`

2. `flow` IN `workflows` from `task` as well as `subflow`

> All workflows are defined within the context of a flow. 
> Flows can include calls to tasks as well as to other flows, which we call "subflows" in this context.
> Flows may be defined within modules and imported for use as subflows in your flow definitions.

3. `flow` IN `deployments`

> Flows are required for deployments — every deployment points to a specific flow as the entrypoint for a flow run.

## create, run flow

使用`@flow`装饰器将函数转成`flow`函数

```python
from prefect import flow

@flow
def my_flow():
    print("Hello Prefect")
    return 
```

运行

```shell
21:43:17.474 | INFO    | prefect.engine - Created flow run 'ruby-walrus' for flow 'my-flow'
Hello Prefect-Flow
21:43:17.713 | INFO    | Flow run 'ruby-walrus' - Finished in state Completed()
```

`my-flow`整个运行过程中状态都内prefect记录下来。直观展示运行的时态。

