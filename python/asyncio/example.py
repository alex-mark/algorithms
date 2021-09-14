# async_scrape.py (requires Python 3.7+)
import asyncio, random, time


async def fetch_url(url):
    print(f"~ executing fetch_url({url})")
    t = time.perf_counter()
    await asyncio.sleep(random.randint(1, 5))
    print(f"time of fetch_url({url}): {time.perf_counter() - t:.2f}s")
    return f"<em>fake</em> page html for {url}"


async def analyze_sentiment(html):
    print(f"~ executing analyze_sentiment('{html}')")
    t = time.perf_counter()
    await asyncio.sleep(random.randint(1, 5))
    r = {"positive": random.uniform(0, 1)}
    print(f"time of analyze_sentiment('{html}'): {time.perf_counter() - t:.2f}s")
    return r


urls = [
    "https://www.ietf.org/rfc/rfc2616.txt",
    "https://en.wikipedia.org/wiki/Asynchronous_I/O",
]
extracted_data = {}


async def handle_url(url):
    html = await fetch_url(url)
    extracted_data[url] = await analyze_sentiment(html)


async def main():
    t = time.perf_counter()
    await asyncio.gather(*(handle_url(url) for url in urls))
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")


async def main_race():
    t = time.perf_counter()
    await asyncio.wait(
        [handle_url(url) for url in urls], return_when=asyncio.FIRST_COMPLETED
    )
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")


async def main_concurrent():
    t = time.perf_counter()
    tasks = [asyncio.create_task(handle_url(url)) for url in urls]

    ## All of the variants below would wait for everything:

    # V1: this will wait as little as possible
    #   (point of this is to show that tasks start executing when created)
    # for task in tasks:
    #     await task

    # V2: ensures all is done by waiting for longest possible time
    # await asyncio.sleep(11)

    # V3: the kind of code one could actually write in real life
    #   (but it's a bit redundant: `wait` or `gather` can also receive
    #    coroutines and can start and run them properly)
    await asyncio.wait(tasks)

    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")


asyncio.run(main_race())
