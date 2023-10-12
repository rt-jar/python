import asyncio
import time

async def check_port(port):
    await asyncio.sleep(2)
    if port%2 == 0:
        print(f"{port} port is open")
    else:
        print(f"{port} is closed")

async def check_ports(ports):
    print(f"Started checking ports: {time.strftime('%X')}")
    tasks = set()
    for x in ports:
        t = asyncio.create_task(check_port(x))

        tasks.add(t)

    for task in tasks:
        await task
    print(f"finished check port {time.strftime('%X')}")

asyncio.run(check_ports(range(8080,8085)))


