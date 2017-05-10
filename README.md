# RoundRobinCPUScheduler
Round-robin is one of the algorithms employed by process and network schedulers in
computing. As the term is generally used, time quantums are assigned to each process in equal
portions and in circular order, handling all processes without priority. Round-robin scheduling is
easy to implement and starvation-free . The name of the algorithm comes from the round-robin
principle known from other fields, where each person takes an equal share of something in turn.
The CPU utilization of such algorithm in ideal conditions would be 100% as there is
always a process that is being run (in reality it is something like 99.9999% due to context
switches taking time to complete). I’ve written my program in Python due to how little code it
needs to run.

I’ve used the following CSV file:
id arrival burst
1 0 12
2 1 8
3 3 3
4 3 7
5 4 5
6 5 9
7 6 2
8 7 1
9 9 11
10 11 4

Example output for time quantum 2:

----------------------------------------------------------------------
ID: 1 took 49 units to complete and out of that waited for 37

ID: 2 took 44 units to complete and out of that waited for 36

ID: 3 took 20 units to complete and out of that waited for 17

ID: 4 took 50 units to complete and out of that waited for 43

ID: 5 took 40 units to complete and out of that waited for 35

ID: 6 took 53 units to complete and out of that waited for 44

ID: 7 took 12 units to complete and out of that waited for 10

ID: 8 took 15 units to complete and out of that waited for 14

ID: 9 took 52 units to complete and out of that waited for 41

ID: 10 took 31 units to complete and out of that waited for 27

----------------------------------------------------------------------
Average completion time was 36.60 and average wait time was 30.40

Final outputs for time quantums 1, 3, 5, and 10 respectively:
----------------------------------------------------------------------
ID: 1 took 56 units to complete and out of that waited for 44

ID: 2 took 46 units to complete and out of that waited for 38

ID: 3 took 18 units to complete and out of that waited for 15

ID: 4 took 46 units to complete and out of that waited for 39

ID: 5 took 35 units to complete and out of that waited for 30

ID: 6 took 53 units to complete and out of that waited for 44

ID: 7 took 16 units to complete and out of that waited for 14

ID: 8 took 7 units to complete and out of that waited for 6

ID: 9 took 52 units to complete and out of that waited for 41

ID: 10 took 32 units to complete and out of that waited for 28

----------------------------------------------------------------------
Average completion time was 36.10 and average wait time was 29.90
----------------------------------------------------------------------
ID: 1 took 39 units to complete and out of that waited for 27

ID: 2 took 46 units to complete and out of that waited for 38

ID: 3 took 6 units to complete and out of that waited for 3

ID: 4 took 50 units to complete and out of that waited for 43

ID: 5 took 38 units to complete and out of that waited for 33

ID: 6 took 49 units to complete and out of that waited for 40

ID: 7 took 18 units to complete and out of that waited for 16

ID: 8 took 22 units to complete and out of that waited for 21

ID: 9 took 51 units to complete and out of that waited for 40

ID: 10 took 41 units to complete and out of that waited for 37

----------------------------------------------------------------------
Average completion time was 36.00 and average wait time was 29.80
----------------------------------------------------------------------
ID: 1 took 33 units to complete and out of that waited for 21

ID: 2 took 42 units to complete and out of that waited for 34

ID: 3 took 12 units to complete and out of that waited for 9

ID: 4 took 47 units to complete and out of that waited for 40

ID: 5 took 19 units to complete and out of that waited for 14

ID: 6 took 47 units to complete and out of that waited for 38

ID: 7 took 29 units to complete and out of that waited for 27

ID: 8 took 30 units to complete and out of that waited for 29

ID: 9 took 52 units to complete and out of that waited for 41

ID: 10 took 35 units to complete and out of that waited for 31

----------------------------------------------------------------------
Average completion time was 34.60 and average wait time was 28.40
----------------------------------------------------------------------
ID: 1 took 10 units to complete and out of that waited for 0

ID: 2 took 11 units to complete and out of that waited for 3

ID: 3 took 17 units to complete and out of that waited for 14

ID: 4 took 20 units to complete and out of that waited for 13

ID: 5 took 26 units to complete and out of that waited for 21

ID: 6 took 30 units to complete and out of that waited for 21

ID: 7 took 38 units to complete and out of that waited for 36

ID: 8 took 39 units to complete and out of that waited for 38

ID: 9 took 52 units to complete and out of that waited for 41

ID: 10 took 46 units to complete and out of that waited for 42

----------------------------------------------------------------------
Average completion time was 28.90 and average wait time was 22.70

Out of this limited data we can conclude that the higher time quantum would ideally lead to
lower completion and wait times.
