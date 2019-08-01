import sys
import asyncio

from charfindler import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'smallfat ?> '

index = UnicodeNameIndex()

async def handle_quires(reader, writer):
    while True:
        writer.write(PROMPT)
        await writer.drain()
        data = await reader.readline()
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00'
        client = writer.get_extra_info('peername')
        print('Received from {}: {!r}'.format(client, query))
        if query:
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)

        await writer.drain()
        print('Sent {} results'.format(len(lines)))

    print('Close the client socket')
    writer.close()


def main(address='192.168.1.102', port=2323):
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_quires, address, port, loop=loop)
    server = loop.run_until_complete(server_coro)
    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    print('Server shutting down')
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
