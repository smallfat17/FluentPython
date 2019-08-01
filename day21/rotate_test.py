import sys
import time
import asyncio
import itertools


async def rotate(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' +msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write('\x08' * len(status))


async def slow():
    await asyncio.sleep(3)
    return 'smallfat'


async def supervisor():
    spinner = asyncio.ensure_future(rotate('thinking!'))
    print('spinner start')
    result = await slow()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', result)


if __name__ == '__main__':
    main()