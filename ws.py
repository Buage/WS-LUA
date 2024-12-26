import asyncio
import websockets
import os

PORT = 8765  # Remplace par le port souhaité

async def handle_connection(websocket, path):
    print("Client connecté")
    try:
        async for message in websocket:
            print(f"Message reçu : {message}")
            await websocket.send(f"Message reçu : {message}")
    except websockets.ConnectionClosedOK:
        print("Client déconnecté")

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", PORT):
        print(f"Serveur WebSocket en écoute sur ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # Garde le serveur en marche

if __name__ == "__main__":
    asyncio.run(main())
