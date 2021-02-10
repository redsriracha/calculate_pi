# calculate_pi

## RUN
mpiexec -mca btl ^openib --hostfile mpihosts -n 4 python -m mpi4py calcpi.py
