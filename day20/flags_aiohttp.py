import asyncio

import aiohttp
import tqdm

from Http_Request import BASE_URL, save_flag, show, main


async def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        html = await res.read()
        return html


async def download_one(cc):
    image = await get_flag(cc)
    # show(cc)
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, save_flag, image, cc)
    return cc


async def download_coro(cc_list):
    tasks = [download_one(cc) for cc in cc_list * 50]
    todo_iter = asyncio.as_completed(tasks)
    todo_iter = tqdm.tqdm(todo_iter, total=len(cc_list) * 50, ncols=80)
    res_list = []
    for future in todo_iter:
        res = await future
        res_list.append(res)
        # status_list.append(res.status)
    return len(res_list)




def download_many(cc_list):
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(download_coro(cc_list))
    # loop.run_forever()
    import time
    time.sleep(.1)
    loop.close()
    # return len(res)
    return res



if __name__ == '__main__':
    main(download_many)

