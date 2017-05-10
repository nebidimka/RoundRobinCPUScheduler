# Aleksandr Skidelskiy
# CSCI330
# New York Institute of Technology
import csv
from collections import deque


class Process:  # Defining Process
    def __init__(self, id, arr, bur):
        self.id = id
        self.arr = arr
        self.bur = bur
        self.originalbur = bur
        self.complete = 0

    def __str__(self):
        return 'id: {:3d}   arrival: {:3d}    burst: {:3d}'.format(self.id, self.arr, self.bur)


class Simulator:  # Building Simulator
    def __init__(self, tq=2):
        self.tq = tq  # Time Quantum
        self.timer = 0
        self.plist = []
        self.delay = 0  # delay to account for time quantum subtraction
        self.q = deque()  # data collection queue

    def addprocess(self, id, arr, bur):
        proc = Process(id, arr, bur)
        self.plist.append(proc)

    def schedule(self):  # churn through list of processes
        while self.timer < 100:  # imaginary timer
            # processes from list to queue
            for proc in self.plist:
                if proc.arr == self.timer:
                    self.q.append(proc)  # add process that matches arrival time
                    print('Adding process', proc.id, ' to queue at', self.timer, ': 00 ')
            # see if there is no delay pending, if true, subtract time quantum
            if self.q and self.delay == 0:
                proc = self.q.popleft()
                if not proc.bur <= 0:
                    print(proc)
                    if proc.bur < self.tq:
                        self.delay = proc.bur - 1  # if the burst left is smaller than time quantum
                    else:
                        self.delay = self.tq-1  # make delay to compensate for seconds ahead
                    proc.bur -= self.tq  # subtract the time quantum
                    if not proc.bur <= 0:
                        self.q.append(proc)  # if the task is not done, add back to queue
                    else:
                        proc.complete = self.timer - proc.arr  #calculate time to complete

            else:
                self.delay -= 1  # if there is a delay, decrease by 1 unit of time passed

            self.timer += 1

    def analyze(self):
        avcomp = 0  # average completion sum
        avwait = 0  # average wait sum
        print('----------------------------------------------------------------------')
        for proc in self.plist:
            avcomp += proc.complete
            avwait += (proc.complete - proc.originalbur)
            print('ID: {:3d} took {:3d} units to complete and out of that waited for{:3d}'.format(proc.id, proc.complete, proc.complete - proc.originalbur))
        print('----------------------------------------------------------------------')
        print('Average completion time was {:0.2f} and average wait time was {:0.2f}'.format(avcomp/len(self.plist), avwait/len(self.plist)))

sim = Simulator()

with open('process.csv', newline='') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
        pid = int(row[0])
        arrival = int(row[1])
        burst = int(row[2])
        sim.addprocess(pid, arrival, burst)

    print('List of processes')
    for proc in sim.plist:
        print(proc)

print('STARTING SIMULATION')

sim.schedule()
sim.analyze()

