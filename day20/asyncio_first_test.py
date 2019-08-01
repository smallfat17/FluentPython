import asyncio
import sys
import itertools



async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
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
    return 42


async def supervisor():
    snipper = asyncio.ensure_future(spin('thinking!'))
    print('snipper object: ', snipper)
    result = await slow()
    snipper.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    print('Answer: ',result)


if __name__ == '__main__':
    main()
    a = supervisor()
    print(type(a)) #<class 'coroutine'
    snipper = asyncio.ensure_future(spin('thinking!')) #<class '_asyncio.Task'>
    print(type(snipper))

