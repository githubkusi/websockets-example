import asyncio
import websockets
import socket

async def send(websocket, path):
    for k in range(100):
        print(f"send {k}", flush=True)
        await websocket.send(str(k))
        await asyncio.sleep(1)


def main():
    # host_name = socket.gethostname()
    host_name = 'server'
    port = 6677

    # Create websocket server
    start_server = websockets.serve(send, host_name, port)

    # Start and run websocket server forever
    asyncio.get_event_loop().run_until_complete(start_server)
    print(f"server started on {host_name}:{port}", flush=True)
    asyncio.get_event_loop().run_forever()


main()
