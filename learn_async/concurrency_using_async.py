import asyncio
import time

# a coroutine
async def async1():
    for i in range(3):
        print("I am an async function 1")
        await asyncio.sleep(5)

# a coroutine
async def async2():
    for i in range(2):
        print("I am an async function 2")
        await asyncio.sleep(10)

#using gather
async def main():
    # we can use gather (it takes all kind of awaitables, which are Tasks, Coroutines and asyncio.Future)
    future = asyncio.gather(async1(), async2(),return_exceptions=True)

    while not future.done():
        print("waiting")
        await asyncio.sleep(1)

    print("done")

#using TaskGroup
async def main2():
    # we can use TaskGroup to group the tasks and get them to event loop
    # TaskGroup provides more structured manner to control the tasks and it also provide a way to introduce some extra logic in between the tasks
    # the only problem with TaskGroup is the exception handling, we need to handle the exceptions manually inside the tasks definition
    # if a exception occurs in the tasks,then all the other remaining tasks will be automatically cancelled
    async with asyncio.TaskGroup() as group:
        group.create_task(async1())
        print("doing something else")
        group.create_task(async2())

    print("done")

if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main2())