#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    # We want to find the petrol pump with min_idx from where we can start the tour and visit all the petrol pumps,
    # using the gas given when travelling through the stations
    
    # petrolpumps shape: [(amount_petrol, distance)]
    # gas_per_km = 1
    
    num_stations = len(petrolpumps)
    
    start_station = 0   # assume we start on the first station
    
    cur_state = (0, 0)  # (total_gas, total_dist)
    
    for idx, station in enumerate(petrolpumps):
        amount_petrol, distance = station
        
        # add gas and distance from current station to the state
        cur_state = (cur_state[0]+amount_petrol, cur_state[1] + distance)
        
        # print("curr_state:", cur_state)
        
        # check if new state is valid
        # Total amount petrol must always be >= distance
        while cur_state[0] < cur_state[1]:
            # Remove the first station
            cur_state = (cur_state[0] - petrolpumps[start_station][0], cur_state[1] - petrolpumps[start_station][1])
            
            start_station += 1
            
            # check if all stations were tried
            if start_station >= num_stations:
                # tried to use all stations
                raise Exception("Impossible")
                
    # check if solution is still valid with the skipped stations
    for idx in range(start_station):
        amount_petrol, distance = petrolpumps[idx]
        
        # add gas and distance from current station to the state
        cur_state = (cur_state[0] + amount_petrol, cur_state[1] + distance)
    
    if cur_state[0] < cur_state[1]:
        raise Exception("Impossible 2")
        
    return start_station
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
