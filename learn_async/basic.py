import asyncio
import time
from datetime import datetime

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

# a normal function
def sync():
    for i in range(1):
        print("I am a sync function")
        time.sleep(5)

async def combined_function():
    print("entering combined function")
    
    result_async1 = async1() #will return a coroutine object
    result_async2 = async2() #will return a coroutine object
    result_sync1 = sync() # will start running as soon as we call it

    print(result_async1) #<coroutine object async1 at 0x10082dec0>
    print(result_async2) #<coroutine object async2 at 0x100c2b140>
    print(result_sync1) #returns None

    # to start a coroutine we need to await the coroutine (the operation is sequential)
    result_async1 = await async1() #the execution of couroutine will stop the further execution
    result_async2 = await async2() #the execution of couroutine will stop the further execution

    print(result_async1)
    print(result_async2)

    # to have parallel excution we need to convert the coroutine to Tasks
    result_async1_task = asyncio.Task(async1())
    result_async2_task = asyncio.Task(async2())

    # the event loop will move between these tasks to run them
    await result_async1_task
    await result_async2_task

    print(result_async1_task.result())
    print(result_async2_task.result())

if __name__ == "__main__":

    asyncio.run(combined_function())
    