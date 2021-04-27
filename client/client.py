import asyncio
import websockets


async def receive():
    uri = 'ws://server:6677'

    async with websockets.connect(uri) as websocket:
        print(f"start listening on {uri}", flush=True)
        while True:
            data = await websocket.recv()
            print(f"received {data}", flush=True)


def main():
    print("client started", flush=True)
    asyncio.get_event_loop().run_until_complete(receive())

main()

