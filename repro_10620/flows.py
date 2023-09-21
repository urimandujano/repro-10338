import asyncio

from prefect import flow, task

from prefect.deployments import run_deployment


@task()
async def some_task(id, index):
    print(f"Hello World = id = {id}, index = {index}")
    return


@flow(cache_result_in_memory=False)
async def k8s_job_flow(id):
    a = []
    for i in range(6000):
        print(len(a), i)
        a.append(" " * 10**6)
    # for index in range(30):
    #    await build_dataframe_async(id, index)


@flow
async def parent_flow():
    fut = await run_deployment(
        "k8s-job-flow/repro-10620-deployment", parameters={"id": "uriel-3"}
    )
    return [fut.state]


if __name__ == "__main__":
    asyncio.run(parent_flow())
