from mpi4py import MPI
import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
circle_count = 0
npoints = 1000000
num = int(npoints/size)

random.seed(rank)
for i in range(num):
    x = random.random()
    y = random.random()
    if (x*x)+(y*y) < 1:
        circle_count += 1

sum = comm.reduce(circle_count, op=MPI.SUM, root=0)

if rank == 0:
    pi = (4.0 * sum)/npoints
    print("value of pi =", pi)
