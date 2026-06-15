#! /usr/bin/env python
# import asyncio
#
# import websockets
#
#
# async def hello():`
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Hello world!")
#         response = await websocket.recv()
#         print(f"Received: {response}")
#
#
# asyncio.run(hello())


# import asyncio
# from websockets.server import serve
#
#
# async def main():
#     # 1. Start the server on port 8765
#     async with serve(echo, "localhost", 8765) as server:
#         print("Server is running on ws://localhost:8765")
#         await server.serve_forever()
#
# async def echo(websocket):
#     # 2. Wait for a message from the client
#     message = await websocket.recv()
#     print(f"Server received: {message}")
#
#     # 3. Send a reply back
#     await websocket.send(f"Hello from server! You said: {message}")
#
# asyncio.run(main())


# import asyncio
#
# from websockets.server import serve
#
#
# async def main():
#     # 1. Start the server on port 8765
#     async with serve(echo, "localhost", 8765) as server:
#         print("Server is running on ws://localhost:8765")
#         await server.serve_forever()
#
#
# async def echo(websocket):
#     # 2. Wait for a message from the client
#     message = await websocket.recv()
#     print(f"Server received: {message}")
#
#     # 3. Send a reply back
#     await websocket.send(f"Hello from server! You said: {message}")
#
#
# asyncio.run(main())

import asyncio

import websockets  # Import the main package directly


async def echo(websocket):
    # Receive a single message
    message = await websocket.recv()
    print(f"Server received: {message}")

    # Send a single reply
    await websocket.send(f"Hello from server! You said: {message}")


async def main():
    # websockets.serve is the correct function path
    async with websockets.serve(echo, "localhost", 8765):
        print("Server is running on ws://localhost:8765")
        await asyncio.Future()  # Keeps the server running continuously


asyncio.run(main())
