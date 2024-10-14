import asyncio #to run asynchronous I/O operations
import websockets
import time

async def hello():
    uri = "ws://192.168.137.174:80"
    async with websockets.connect(uri) as websocket: #ws connection to the server called websocket
        while True:
            message = "hello"
            await websocket.send(message)
            print(f"Sent message: {message}")

            response = await websocket.recv()
            print(f"Received response: {response}")
            time.sleep(1)

if __name__ == "__main__":
    asyncio.run(hello())
