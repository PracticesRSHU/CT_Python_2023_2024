import signal
import sys
import asyncio
import aiohttp
import json

# #https://www.reddit.com/r/python/top.json?sort=top&t=day&limit=5
# #https://www.reddit.com/r/programming/top.json?sort=top&t=day&limit=5
# #https://www.reddit.com/r/compsci/top.json?sort=top&t=day&limit=5
# loop = asyncio.get_event_loop()
# client = aiohttp.ClientSession(loop=loop)
#
# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200
#         return await response.read()
#
# async def get_reddit_top(subreddit, client):
#     data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')
#
#     j = json.loads(data1.decode('utf-8'))
#     for i in j['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + ' (' + link + ')')
#
#     print('DONE:', subreddit + '\n')
#
# def signal_handler(signal, frame):
#     loop.stop()
#     client.close()
#     sys.exit(0)
#
# signal.signal(signal.SIGINT, signal_handler)
#
# asyncio.ensure_future(get_reddit_top('python', client))
# asyncio.ensure_future(get_reddit_top('programming', client))
# asyncio.ensure_future(get_reddit_top('compsci', client))
# loop.run_forever()
#


#==============================================
# import asyncio
# import aiohttp
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'https://www.example.com')
#         print(html)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


#=============================================================
# import asyncio
# from aiohttp import web
# async def hello(request):
#     return web.Response(text="Hello, world")
# async def main():
#     app = web.Application()
#     app.add_routes([web.get('/', hello)])
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, 'localhost', 8080)
#     await site.start()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


#=============================
import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
