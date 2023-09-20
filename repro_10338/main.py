from prefect import flow, task


@task()
async def build_dataframe_async(id, index):
    print(f"Hello World = id = {id}, index = {index}")
    return


@flow(cache_result_in_memory=False)
async def flow_async(id):
    a = []
    while True:
        print(len(a))
        a.append(" " * 10**6)
    # for index in range(30):
    #    await build_dataframe_async(id, index)
