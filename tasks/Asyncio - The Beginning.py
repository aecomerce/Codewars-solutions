import asyncio

async def dreaming(n, m):
    await asyncio.sleep(n)
    return m ** n

async def main():
    task = asyncio.create_task(dreaming(5, 4))
    await task

asyncio.run(main())
