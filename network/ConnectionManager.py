import socket
import threading
import websockets
import windows.MainWindow


class ConnectionManager:
    def __init__(self):
        self.uri = None
        self.connection = None

    async def connect(self, uri: str):
        self.uri = uri

        windows.window.window.title(f"Luminol Profiler - Connecting to {uri}")

        self.connection = await websockets.connect(self.uri)
        print(f"Connected to {self.uri}")
        windows.window.window.title(f"Luminol Profiler - Connected to {uri}")

    async def send(self, message):
        if self.connection:
            await self.connection.send(message)
            print(f"Message sent: {message}")
        else:
            print("Connection not established.")

    async def receive(self):
        if self.connection:
            return await self.connection.recv()
        else:
            print("Connection not established.")
            return None

    async def disconnect(self):
        if self.connection:
            await self.connection.close()
            self.connection = None
            print("Disconnected.")