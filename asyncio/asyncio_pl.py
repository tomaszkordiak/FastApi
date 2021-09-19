import asyncio


async def tomek():
    print("tomek1")
    await asyncio.sleep(1)
    print("tomek2")


async def piotrek():
    print("piotrek1")
    await asyncio.sleep(1)
    print("piotrek2")


async def michal():
    print("michal1")
    await asyncio.sleep(1)
    print("michal2")


async def main():
    await asyncio.gather(tomek(), piotrek(), michal())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
