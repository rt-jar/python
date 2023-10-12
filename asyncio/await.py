import asyncio
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
#asyncio.run(main())

with asyncio.Runner() as runner:
    runner.run(main())
    runner.close()
