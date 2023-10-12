import asyncio


async def delete_row(rownum):
    await asyncio.sleep(1)
    print(f"{rownum} deleted")
    return rownum


async def main():
    l = await asyncio.gather(delete_row(1), delete_row(2), delete_row(3))
    print(l)

asyncio.run(main())