from collections import namedtuple
from queue import PriorityQueue
from dataclasses import dataclass

import random
import collections
import queue
import argparse
import time
DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = namedtuple('Event', 'texi_id time action')

class Simulator:
    def __init__(self, taxi_map):
        self.events = PriorityQueue()
        self.taxis = dict(taxi_map)

    def run(self, endtime):
        for taxi_id in self.taxis:
            event = next(self.taxis[taxi_id])
            self.events.put(event)
        sim_time = 0
        while sim_time < endtime:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            texi_id, sim_time, previous_action = current_event
            print('{} {} {}'.format(sim_time, texi_id, previous_action))
            next_time = sim_time + compute_duration(previous_action)
            # next_time = sim_time + 5
            active_taxi = self.taxis[texi_id]
            try:
                next_event = active_taxi.send(next_time)
            except StopIteration:
                del self.taxis[texi_id]
            else:
                self.events.put(next_event)
        else:
            msg = '***all events end***'
            print(msg)

def compute_duration(previous_action):
    """使用指数分布计算操作的耗时"""
    if previous_action in ['leave garage', 'drop off passenger']:
    # 新状态是四处徘徊
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
    # 新状态是行程开始
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1



def taxi_process(taxi_id, trpis, start_time=0):
    time = yield Event(taxi_id, start_time, 'leave garage'.format(taxi_id))
    for _ in range(trpis):
        time = yield Event(taxi_id, time,  'pick up passenger')
        time = yield Event(taxi_id, time,  'drop off passenger')
    yield Event(taxi_id, time,  'going home')




if __name__ == '__main__':
    # taxi = taxi_process(1, 2, 0)
    # event = next(taxi)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    # event = taxi.send(event.time + 5)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    # event = taxi.send(event.time + 10)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    # event = taxi.send(event.time + 15)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    # event = taxi.send(event.time + 15)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    # event = taxi.send(event.time + 15)
    # print('time:{} taxi_{} {}'.format(event.time, event.texi_id, event.action))
    taxis = {i: taxi_process(i, (i+1) * 2, i * 5, ) for i in range(3)}
    sim = Simulator(taxis)
    sim.run(180)
    
