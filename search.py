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

def depthFirstSearch(problem: SearchProblem):
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
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    reached = util.Stack()
    return search(problem, frontier, reached, strategy="DFS")
    # # 栈，存储待扩展的状态和路径
    # frontier = util.Stack()
    # # 起始状态和空路径
    # frontier.push((problem.getStartState(), []))
    # reached = util.Stack()  # 栈，存储已经访问过的状态
    #
    # # 栈不为空时
    # while not frontier.isEmpty():
    #     # 从栈中弹出一个状态和路径
    #     (currentState, route) = frontier.pop()
    #     # 如果是目标，返回路径
    #     if problem.isGoalState(currentState):
    #         return route
    #     # 没有访问过， 继续扩展
    #     elif currentState not in reached.list:
    #         reached.push(currentState)  # 标记为已访问
    #         successors = problem.getSuccessors(currentState)
    #         for successor in successors:    # 遍历所有后续状态，压入栈中
    #             frontier.push((successor[0], route + [successor[1]]))


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))
    reached = util.Queue()
    return search(problem, frontier, reached, strategy="BFS")
    # # 相对于DFS，只是将栈改为队列
    # frontier = util.Queue()
    # frontier.push((problem.getStartState(), []))
    # reached = util.Queue()
    #
    # while not frontier.isEmpty():
    #     (currentState, route) = frontier.pop()
    #
    #     if problem.isGoalState(currentState):
    #         return route
    #
    #     elif currentState not in reached.list:
    #         reached.push(currentState)
    #         successors = problem.getSuccessors(currentState)
    #         for successor in successors:
    #             frontier.push((successor[0], route + [successor[1]]))



def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)
    reached = util.Queue()
    return search(problem, frontier, reached, strategy="UCS")
    # # 这里使用PriorityQueue，优先队列
    # frontier = util.PriorityQueue()
    # frontier.push((problem.getStartState(), [], 0), 0)
    # reached = util.Queue()
    #
    # while not frontier.isEmpty():
    #     (currentState, route, cost) = frontier.pop()
    #
    #     if problem.isGoalState(currentState):
    #         return route
    #
    #     elif currentState not in reached.list:
    #         reached.push(currentState)
    #         successors = problem.getSuccessors(currentState)
    #         for successor in successors:
    #             # 表示一个包含新状态、路径和总代价的元组(state, action, cost)， 优先级
    #             frontier.push((successor[0], route + [successor[1]], cost + successor[2]), cost + successor[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)
    reached = util.Queue()
    return search(problem, frontier, reached, strategy="A*", heuristic=heuristic)
    # # 使用优先队列，并初始化
    # frontier = util.PriorityQueue()
    # frontier.push((problem.getStartState(), [], 0), 0)
    # reached = util.Queue()  # 队列， 记录已经访问的状态
    #
    # while not frontier.isEmpty():
    #     (currentState, route, f) = frontier.pop()  # f = g + h
    #     # 通过 f 值减去启发式函数值 h，得到当前状态的代价 g
    #     g = f - heuristic(currentState, problem)  # g: cost
    #
    #     if problem.isGoalState(currentState):
    #         return route
    #
    #     elif currentState not in reached.list:
    #         reached.push(currentState)
    #         successors = problem.getSuccessors(currentState)
    #         for successor in successors:
    #             # 计算后继状态的启发式代价 h
    #             h = heuristic(successor[0], problem)
    #             # 将后继状态、更新后的路径和总代价推入优先队列
    #             # g + successor[2] 是到达后继状态的代价，h 是启发式代价，g + successor[2] + h 是 f 值
    #             frontier.push((successor[0], route + [successor[1]], g + successor[2] + h), g + successor[2] + h)


def search(problem: SearchProblem, frontier, reached, strategy="DFS", heuristic=nullHeuristic):
    """
    通用搜索框架，用于DFS, BFS, UCS 和 A*。

    参数:
        problem: 搜索问题实例
        frontier: 用于存储待扩展状态的容器（栈、队列或优先队列）
        reached: 用于存储已访问状态的容器
        strategy: 搜索策略（DFS, BFS, UCS, A*）
        heuristic: A*搜索的启发式函数，默认是nullHeuristic

    返回:
        路径（动作列表）
    """
    while not frontier.isEmpty():
        if strategy == "DFS" or strategy == "BFS":
            (currentState, route) = frontier.pop()  # 从frontier中弹出状态和路径
        elif strategy == "UCS":
            (currentState, route, cost) = frontier.pop()  # 从frontier中弹出状态和路径
        elif strategy == "A*":
            (currentState, route, f) = frontier.pop()  # f = g + h

        # 如果是目标状态，返回路径
        if problem.isGoalState(currentState):
            return route

        # 如果当前状态没有访问过，则继续扩展
        if currentState not in reached.list:
            reached.push(currentState)
            successors = problem.getSuccessors(currentState)  # 获取当前状态的后继状态

            for successor in successors:
                if strategy == "DFS" or strategy == "BFS":
                    # 对于DFS和BFS，直接将后继状态和路径推入frontier
                    frontier.push((successor[0], route + [successor[1]]))
                elif strategy == "UCS":
                    # 对于统一代价搜索，推入后继状态、路径和当前代价
                    frontier.push((successor[0], route + [successor[1]], cost + successor[2]),
                                  cost + successor[2])
                elif strategy == "A*":
                    # 对于A*搜索，计算实际代价g和启发式代价h，得到f = g + h
                    g = f - heuristic(currentState, problem)  # g: cost
                    h = heuristic(successor[0], problem)  # 启发式代价
                    # 将后继状态、更新后的路径和总代价f推入优先队列
                    frontier.push((successor[0], route + [successor[1]], g + successor[2] + h), g + successor[2] + h)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
