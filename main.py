import json
import time
import asyncio
from aiohttp import ClientSession, client_exceptions

ATTEMPTS = 3


async def fetch(session, url):
    try:
        load_time = 0
        for i in range(ATTEMPTS):
            start = time.time()
            async with await session.get(url):
                end = time.time()
                load_time += end - start
        return {url: load_time / i}
    except client_exceptions.ClientConnectionError:
        return {url: -1}


async def crawl(urls: set):
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        return await asyncio.gather(*tasks)


def lambda_handler(event, context):
    try:
        links = list(event["links"])
    except TypeError as e:
        return {
            'statusCode': 500,
            'body': e,
        }
    resp = {}
    for k in asyncio.run(crawl(links)):
        resp.update(k)
    return {
        'statusCode': 200,
        'body': resp,
    }
