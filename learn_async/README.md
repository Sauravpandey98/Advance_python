# Asynchronous Programming in Python

This directory contains examples and demonstrations of asynchronous programming in Python using the `asyncio` library. Asynchronous programming allows for concurrent execution of tasks, improving performance and responsiveness in I/O-bound applications.

## Table of Contents

- [Basic Concepts](#basic-concepts)
- [Concurrency with `asyncio`](#concurrency-with-asyncio)
- [Concurrency with `aiohttp`](#concurrency-with-aiohttp)
- [Rate Limiting](#rate-limiting)
- [Files](#files)

## Basic Concepts

Asynchronous programming involves defining coroutines, which are special functions that can be paused and resumed. This allows other tasks to run while a coroutine is waiting for an I/O operation to complete.

-   **Coroutines:** Defined using `async def`. They can pause execution using the `await` keyword.
-   **Event Loop:** The core of `asyncio`, responsible for scheduling and running coroutines.
-   **Tasks:** Wrappers around coroutines that allow them to be scheduled and run concurrently.

## Concurrency with `asyncio`

The `asyncio` library provides tools for managing concurrent tasks.

### `asyncio.gather`

-   Allows running multiple awaitables (coroutines, tasks, and `asyncio.Future` objects) concurrently.
-   Returns a list of results in the order the awaitables were passed.
-   Can be configured to return exceptions instead of raising them using `return_exceptions=True`.

### `asyncio.TaskGroup`

-   Provides a structured way to manage and control tasks.
-   Automatically cancels remaining tasks if an exception occurs in one of the tasks.
-   Requires manual exception handling within the task definitions.

## Concurrency with `aiohttp`

`aiohttp` is an asynchronous HTTP client/server framework that allows making concurrent HTTP requests.

-   **Client Sessions:** Use `aiohttp.ClientSession` to manage connections and make requests.
-   **Asynchronous Requests:** Use `async with session.get(url)` to make GET requests asynchronously.

## Rate Limiting

When making concurrent requests, it's important to implement rate limiting to avoid overwhelming servers and getting banned.

-   **`asyncio.Semaphore`:** Used to limit the number of concurrent requests.
-   **`asyncio.sleep`:** Used to introduce delays between requests.

## Files

### `basic.py`

-   **Description:** Demonstrates basic asynchronous concepts, including coroutines, tasks, and the event loop.
-   **Key Concepts:**
    -   Defining and running coroutines.
    -   Converting coroutines to tasks for concurrent execution.
    -   Mixing synchronous and asynchronous code.

### `concurrency_using_async.py`

-   **Description:** Shows how to use `asyncio.gather` and `asyncio.TaskGroup` to run multiple coroutines concurrently.
-   **Key Concepts:**
    -   Using `asyncio.gather` to run coroutines concurrently and collect results.
    -   Using `asyncio.TaskGroup` for structured concurrency and exception handling.

### `concurrency_in_requests.py`

-   **Description:** Demonstrates making concurrent HTTP requests using `aiohttp` and implementing rate limiting.
-   **Key Concepts:**
    -   Making asynchronous HTTP requests using `aiohttp`.
    -   Implementing rate limiting using `asyncio.Semaphore` and `asyncio.sleep`.
    -   Comparing the performance of synchronous and asynchronous requests.