import asyncio
import time


async  def download_one(time, semaphore):

    async with semaphore:
        time = await slp(time)
        print('time: {} finished'.format(time))
    return time


async def slp(time):
    print('slp: {}'.format(time))
    await asyncio.sleep(time)
    return time


async def download_coro(concur_req):
    semaphore = asyncio.Semaphore(concur_req)
    tasks = [download_one(time, semaphore) for time in sorted(range(1, 5))]

    todo_iter = asyncio.as_completed(tasks)
    for future in todo_iter:
        print('wait for ', future)
        res = await future
        print('finished ', future, 'result: ', res)


def download_many():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_coro(2))
    loop.close()


if __name__ == '__main__':
    download_many()


