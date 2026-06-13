import asyncio

from websockets.asyncio.client import connect


async def main():
    # 1. Connect to the server
    async with connect("ws://localhost:8765") as websocket:
        # 2. Send a message
        await websocket.send("Hi!")

        # 3. Wait for the reply
        reply = await websocket.recv()
        print(f"Client received: {reply}")


asyncio.run(main())
