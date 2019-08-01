from time import perf_counter
import asyncio

def speak(pattern):
    print(pattern, 'start to listen')
    while True:
        line = yield
        print(line)

if __name__ == '__main__':

    g = speak('python')
    g.send(None)
    g.send('hello')
    g.send('hello1')
    g.send('hello2')


