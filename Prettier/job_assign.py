import heapq
import numpy as np
from copy import deepcopy

class Node:

    def __init__(self, cost_matrix, assigned_positions=None, level=0):
        
        self.cost_matrix = cost_matrix
        
        if assigned_positions:
            self.assigned_positions = assigned_positions
        else:
            self.assigned_positions = []

        self.level = level
        
        self.lowerbound = self.calculate_lowerbound()



    def __lt__ (self, other):
        return self.lowerbound < other.lowerbound
        

    def calculate_lowerbound(self):
            
        cost=0

        # calculate the cost of assigned positions till now
        for i, j in self.assigned_positions:
            cost = cost + self.cost_matrix[i][j]

        # create a temp copy of cost_matrix
        temp_matrix = deepcopy(self.cost_matrix)

        #  mark the assigned positions row & col as infinity
        for i, j in self.assigned_positions:
            for k in range(len(temp_matrix)):
                temp_matrix[i][k] = float("inf")
                temp_matrix[k][j] = float("inf")

        # add minimum cost for unassigned rows from i level to all j
        for i in range(self.level, len(temp_matrix)):
                
            min_val = float("inf")

            for j in range(len(temp_matrix)):
                    
                if temp_matrix[i][j] < min_val:
                    min_val = temp_matrix[i][j]

        # add assigned and unassigned cost
            if min_val!= float("inf"):
                cost = cost + min_val

        return cost
    

def solve_assignment(cost_matrix):

    n = len(cost_matrix)
    pq = []  # priority queue

    root = Node(cost_matrix)

    # this sets the root level=0 and assignment=None
    heapq.heappush(pq, root)

    min_cost = float("inf")
    best_assignment = None

    while pq:

        current = heapq.heappop(pq)

        if current.lowerbound >= min_cost:
            continue
        
        # take lvl 0 for 1st time
        level = current.level

        #  first check if we assigned all jobs n got best sol
        if level==n:
            if current.lowerbound < min_cost:
                min_cost = current.lowerbound
                best_assignment = current.assigned_positions
            continue

        # get all assigned jobs
        assigned_job = [j for j in current.assigned_positions]

        #  now try to assign remaining jobs
        for job in range(n):

            if job in assigned_job:
                continue

            new_assigned = current.assigned_positions + [(level, job)]

            child = Node(cost_matrix, new_assigned, level+1)

            if child.lowerbound < min_cost:
                heapq.heappush(pq, child)
    
    return min_cost, best_assignment
        

if __name__=="__main__":

    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    
    min_cost, assignment = solve_assignment(cost_matrix)
    print(f"Minimum Cost: {min_cost}")
    print("Assignments:") 

    for person, job in sorted(assignment):
        print(f"Person {person} -> Job {job}   ( Cost : {cost_matrix[person][job]})")
