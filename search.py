# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Adopted for EMU COSC 461/561
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    initial_state = problem.getStartState()
    # expanded = []
    expanded = set()
    fringe = util.Stack()
    fringe.push((initial_state,[]))
    # expanded.append(initial_state)
    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        if problem.isGoalState(current_state):
            return path
        if current_state in expanded:
        	continue
        for successor, action, stepCost in problem.getSuccessors(current_state):
            if successor not in expanded:               
                fringe.push((successor, path + [action]))
        expanded.add(current_state)
    return []                                                                          

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    initial_state = problem.getStartState()
    expanded = set()
    fringe = util.Queue()
    fringe.push((initial_state,[]))
    
    while not fringe.isEmpty():
        current_state, path = fringe.pop()
        if problem.isGoalState(current_state):
            return path
        if current_state in expanded:
            continue
        for successor, action, stepCost in problem.getSuccessors(current_state):
            if successor not in expanded:
                fringe.push((successor, path + [action]))
        expanded.add(current_state)  
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    initial_state = problem.getStartState()
    expanded = set()
    fringe = util.PriorityQueue()
    fringe.push((initial_state,[], 0), 0)  # (state, path_to_start, cost)
    while not fringe.isEmpty():
    	current_state, path, cost = fringe.pop()
    	if problem.isGoalState(current_state):
    		return path
    	if current_state in expanded:
    		continue
    	for successor, action, stepCost in problem.getSuccessors(current_state):
    		if successor not in expanded:
    			# push successors onto the fringe in the order provided by getSuccessors
    			# succ = (successor, action, stepCost)
    			fringe.push((successor, path + [action], cost + stepCost), cost + stepCost)
    	expanded.add(current_state)
    return [] 



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    initial_state = problem.getStartState()
    # cost + stepcost is the g value
    # cost + stepcost + heuristic() is the f value
    expanded = set()
    fringe = util.PriorityQueue()
    fringe.push((initial_state,[], 0), 0 + heuristic(initial_state, problem))  # (state, path_to_start, cost)
    
    while not fringe.isEmpty():
    	current_state, path, cost = fringe.pop()
    	if problem.isGoalState(current_state):
    		return path
    	if current_state in expanded:
    		continue
    	for successor, action, stepCost in problem.getSuccessors(current_state):
    		if successor not in expanded:
    			# push successors onto the fringe in the order provided by getSuccessors
    			# succ = (successor, action, stepCost)
    			fringe.push((successor, path + [action], cost + stepCost), cost + stepCost + heuristic(successor, problem))
    	expanded.add(current_state)
    return [] 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
