# Pacman AI · Search Algorithms and Path Planning

[简体中文](README.md) | [English](README_EN.md)

Explore classical AI search in Pacman mazes: from single-goal planning to visiting four corners and collecting all food, comparing strategies through path cost and search effort.

Built on the **UC Berkeley Pacman AI** teaching framework, with a focus on search implementation, task-state representation and heuristic design.

## Highlights

- **Four search strategies**: DFS, BFS, Uniform Cost Search and A*.
- **Shared search logic**: stacks, queues and priority queues organise the frontier within a common search loop.
- **Multiple-goal representations**: position plus corner-visit flags for the Corners Problem; position plus a food grid for Food Search.
- **Map-aware heuristics**: BFS computes exact maze distances, with the maximum distance to remaining food guiding A*.
- **Greedy food collection**: repeated closest-food searches build a complete action sequence, contrasting local decisions with global planning.
- **Visualisation and evaluation**: graphical/text displays, a course autograder and bundled tests.

## Algorithms and tasks

| Module | Method | Focus |
| --- | --- | --- |
| Single-goal search | DFS / BFS | Depth-first versus level-order expansion |
| Cost-based search | UCS | Cumulative path-cost ordering |
| Heuristic search | A* | Path cost combined with a goal-distance estimate |
| Corners task | CornersProblem + A* | Multiple-goal state representation and heuristics |
| All-food task | FoodSearchProblem + A* | Remaining-goal representation and maze distance |
| Closest-food strategy | ClosestDotSearchAgent + BFS | Repeated local searches and route composition |

The corners heuristic combines Euclidean distance to the closest unvisited corner with a term based on remaining corners and map dimensions. The food heuristic uses shortest-path distances that account for walls.

## Usage

Requires **Python 3**. Graphical rendering uses Tkinter and a desktop display; use `-q` for terminal runs.

```bash
git clone https://github.com/VincentLucifer/AI-Lab1-Pacman.git
cd AI-Lab1-Pacman
python -m pip install networkx

# BFS: single-goal maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -q

# A*: Manhattan heuristic
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -q

# Visit all corners
python pacman.py -l tinyCorners -p AStarCornersAgent -q

# Collect all food
python pacman.py -l smallSearch -p AStarFoodSearchAgent -q

# Repeated closest-food search
python pacman.py -l smallSearch -p ClosestDotSearchAgent -q
```

Replace `fn=bfs` with `fn=dfs` or `fn=ucs` to compare strategies. Remove `-q` for graphics, or run `python pacman.py` for manual play using arrow keys or WASD.

## Search comparison

A terminal run on `mediumMaze` produced:

| Algorithm | Path cost | Expanded nodes |
| --- | ---: | ---: |
| DFS | 130 | 146 |
| BFS | 68 | 269 |
| UCS | 68 | 269 |
| A* + Manhattan | 68 | 221 |

On this layout, A* matches the BFS/UCS path cost while expanding fewer nodes. This illustrates search behaviour rather than establishing performance across all layouts.

## Code map

| Path | Contents |
| --- | --- |
| `search.py` | Search interface, four algorithms and shared search loop |
| `searchAgents.py` | Agents, task states, heuristics and maze distance |
| `pacman.py` / `game.py` | CLI entry point and game execution |
| `util.py` | Stack, queue, priority queue and other structures |
| `layouts/` | Maze layouts |
| `autograder.py` / `test_cases/` | Grader and q1–q8 tests |
| `graphicsDisplay.py` / `textDisplay.py` | Display components |

`SearchAgent` constructs a search problem and plans an action sequence during initialisation, then lets the game execute it step by step, separating planning from environment execution.

## Automated evaluation

```bash
python autograder.py --no-graphics
python autograder.py -q q1 --no-graphics
```

## Acknowledgements

The environment and grading framework come from [UC Berkeley Pacman AI Projects](http://ai.berkeley.edu), with core contributions from John DeNero and Dan Klein. This repository builds its search experiments on that teaching framework. Use and redistribution follow the original source notices.

## Related labs

[Lab 2 · Deep Learning](https://github.com/VincentLucifer/AI-Lab2-DeepLearning) · [Lab 3 · Reinforcement Learning](https://github.com/VincentLucifer/AI-Lab3-ReinforcementLearning)
