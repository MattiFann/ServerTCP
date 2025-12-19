# ServerTCP

TCP Multithreaded Server (Educational)

A minimal Python TCP server designed to handle simultaneous connections using multithreading. Developed as an educational project to explore socket programming and concurrent client-server communication.

Key Features:

    Concurrency: Non-blocking architecture where each client is handled in a separate thread.

    Clean Logging: IP tracking and integrated error handling for better debugging.

    Safe Shutdown: Graceful server exit using CTRL+C.

    Source: Inspired by concepts from BlackHat Python V2.

Technical Flow

The server architecture follows this logical sequence:

    Listen: The main thread waits for incoming connections on port 9998.

    Spawn: Upon connection, it creates a new client_handler thread.

    Process: The worker thread receives data and sends an acknowledgment while the main thread returns to listen for new clients.
