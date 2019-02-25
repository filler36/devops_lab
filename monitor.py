#!/usr/bin/python
import psutil
import json
import datetime
import threading
import settings


class Mon:
    def __init__(self):
        self.name = "Python Monitor by Filip"
        self.version = "v0.1"
        self.counter = 0

    def dump(self):
        cpu_load = psutil.cpu_percent()
        mem_total = psutil.virtual_memory().total / 1024 ** 3
        mem_used = psutil.virtual_memory().used / 1024 ** 3
        disk_io = psutil.disk_io_counters()
        net_stat = psutil.net_io_counters()
        timestamp = datetime.datetime.now().strftime(settings.TIME_FORMAT)
        threading.Timer(settings.INTERVAL, self.dump).start()
        self.counter += 1
        with open('data.json', 'a') as outfile:
            json.dump({'SNAPSHOT ' + str(self.counter): timestamp,
                       'CPU_LOAD_%': cpu_load,
                       'MEM_TOTAL_IN_GB': float("{:.2f}".format(mem_total)),
                       'MEM_USED_IN_GB': float("{:.2f}".format(mem_used)),
                       'READ_COUNT': disk_io[0],
                       'WRITE_COUNT': disk_io[1],
                       'BYTES_SENT': net_stat[0],
                       'BYTES_RECEIVED': net_stat[1]}, outfile, indent=1)


MONITOR = Mon()
MONITOR.dump()
