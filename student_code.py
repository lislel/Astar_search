#code structure taken from A* pseudocode on wikipedia
#use of Priority Code based on suggestion from last review


import math
from queue import PriorityQueue


def reconstruct_path(cameFrom, current):
    #create empty list 
    total_path = []
    #add current value to list
    total_path.append(current)
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    #reverse so total_path goes from start to finish
    total_path.reverse()
    return(total_path)

def cost(node, M, goal):
    #get x,y coord of goal and node
    goal_coord =M.intersections[goal]
    value = M.intersections[node]
    #determine difference between x's and y's of goal and node
    delta_x = goal_coord[0] - value[0]
    delta_y = goal_coord[1] - value[1]
    #calculate straight line difference, based on a^2 + b^2 = c^2
    value = (math.sqrt((delta_x**2) + (delta_y**2)))
    return(value)


def shortest_path(M,start,goal):

#initialize variables
    #set of nodes already evaluated
    closedSet = set()
    
    #set of currently discovered nodes that aren't evaluated yet
    openSet = set()
    openSet.add(start)
    
    #dictionary, where the key is each node, and the value is where the node came from most efficiently
    cameFrom = dict()
    
    #dictionary, where key is each node, and value is cost to get to that node from start
    gScore = dict()
    
    #initialize gScore for the start value. Cost to get to start from start = 0
    gScore[start] = 0
    
    #Priority Queue, the total cost of g+h, where g is path cost, and h is distance from goal
    fScore = PriorityQueue()
    
    #initialize cost for start node, which will be entirely h.
    fScore.put((cost(start,M,goal), start))

    #initialize gScore
    neighbor = M.roads[start]
    for place in neighbor:
        gScore[place] = cost(place, M, start)
    
    #set flag for goal being found to false. 
    goal_achieved = False

    
#function
    while goal_achieved == False:
        
        #get the lowest scoring node
        current_t = fScore.get()
        current = current_t[1]

        #if the current node is equal to the goal node, return the path to get to goal and break
        if current == goal:
            goal_achieved = True
            return reconstruct_path(cameFrom, current)

        #otherwise, remove the current node from the open set and add it to the closed set
        openSet.remove(current)
        closedSet.add(current)
        
        #get nearest neighbors of current node, and store in list
        neighbor = M.roads[current]

        
        for place in neighbor:
            #if node is "closed", skip and move on to next node in neighbor list
            if place in closedSet:
                continue
            #if node is not in already in the openset, add node to the open set
            if place not in openSet:
                openSet.add(place)
            #calcualte the tentative gscore of expanding to this node, by adding cost of current node from start, and the distance between current node and THIS neighborng node
            tent_gScore = gScore[current] + cost(current, M, place)

            # if the gScore has already been calculated, compare to previous gScore. If the tentative gScore is greater than the current gScore, this path is not efficient as the previous path to get to this node. So, we should skip this path, and move on to the next neighbor.
            if place in gScore.keys() and tent_gScore > gScore[place]:
                continue
            else:
                # if the gScore for this place hasn't already been calculated, set the Gscore as the Gscore for this node
                gScore[place] = tent_gScore
                # for each node in neighbor, set current as where the node came from
            #for each node in neighbor, set current as where the node came from
            cameFrom[place] = current
            gScore[place] = tent_gScore
            #set the total cost for node to equal g_h, aka total cost from start to node + total distance from node to goal, and store in fScore
            total = gScore[place] + cost(place, M, goal)
            fScore.put((total, place))

        

    
    
    
    