# Pacman AI · 搜索算法与路径规划

[简体中文](README.md) | [English](README_EN.md)

在 Pacman 迷宫中探索经典人工智能搜索：从单目标路径规划，到访问四个角落与收集全部食物，比较不同搜索策略在路径代价和搜索规模上的表现。

基于 **UC Berkeley Pacman AI** 教学框架，重点实现搜索算法、任务状态建模与启发式函数。

## 项目亮点

- **四种搜索策略**：DFS、BFS、Uniform Cost Search 与 A*。
- **共享搜索逻辑**：使用栈、队列、优先队列组织 frontier，在同一搜索循环中处理不同策略。
- **多目标状态建模**：用“位置 + 四角访问标记”表示 Corners Problem，用“位置 + 食物网格”表示 Food Search Problem。
- **地图感知启发式**：利用 BFS 计算真实迷宫距离，以到剩余食物的最大距离引导 A*。
- **贪心收集策略**：反复搜索最近食物并拼接动作序列，对比局部决策与整体规划。
- **可视化与评估**：支持图形/文本显示，并包含课程自动评分器和测试用例。

## 算法与任务

| 模块 | 方法 | 关注点 |
| --- | --- | --- |
| 单目标搜索 | DFS / BFS | 深度优先与层次扩展 |
| 带代价搜索 | UCS | 按累计路径代价排序 |
| 启发式搜索 | A* | 联合路径代价与目标距离估计 |
| 四角任务 | CornersProblem + A* | 多目标访问状态与启发式设计 |
| 全食物任务 | FoodSearchProblem + A* | 剩余目标建模与迷宫距离 |
| 最近食物策略 | ClosestDotSearchAgent + BFS | 连续局部搜索与路线拼接 |

四角启发式结合最近未访问角落的欧氏距离与剩余角落数量、地图尺寸；食物启发式使用考虑墙体的最短路距离。

## 运行方式

需要 **Python 3**。图形显示使用 Tkinter，需要可用桌面环境；终端运行可使用 `-q`。

```bash
git clone https://github.com/VincentLucifer/AI-Lab1-Pacman.git
cd AI-Lab1-Pacman
python -m pip install networkx

# BFS：单目标迷宫
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -q

# A*：Manhattan 启发式
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -q

# 四角访问
python pacman.py -l tinyCorners -p AStarCornersAgent -q

# 收集全部食物
python pacman.py -l smallSearch -p AStarFoodSearchAgent -q

# 逐个寻找最近食物
python pacman.py -l smallSearch -p ClosestDotSearchAgent -q
```

将 `fn=bfs` 替换为 `fn=dfs` 或 `fn=ucs` 可比较其他策略。去掉 `-q` 使用图形显示；运行 `python pacman.py` 可用方向键或 WASD 手动游玩。

## 搜索对比

以下是 `mediumMaze` 的一次终端运行结果：

| 算法 | 路径代价 | 扩展节点数 |
| --- | ---: | ---: |
| DFS | 130 | 146 |
| BFS | 68 | 269 |
| UCS | 68 | 269 |
| A* + Manhattan | 68 | 221 |

在该地图中，A* 与 BFS/UCS 得到相同代价，同时减少节点扩展。该结果用于展示搜索行为，不代表所有地图上的性能结论。

## 代码导航

| 路径 | 内容 |
| --- | --- |
| `search.py` | 搜索问题接口、四种算法、通用搜索循环 |
| `searchAgents.py` | Agent、任务状态、启发式、迷宫距离 |
| `pacman.py` / `game.py` | 命令行入口与游戏运行逻辑 |
| `util.py` | 栈、队列、优先队列等数据结构 |
| `layouts/` | 迷宫布局 |
| `autograder.py` / `test_cases/` | 自动评分与 q1–q8 测试 |
| `graphicsDisplay.py` / `textDisplay.py` | 显示组件 |

`SearchAgent` 在初始化阶段建立搜索问题并生成动作序列，随后交给游戏引擎逐步执行，将规划逻辑与环境执行分开。

## 自动评估

```bash
python autograder.py --no-graphics
python autograder.py -q q1 --no-graphics
```

## 致谢

游戏环境及评分框架来自 [UC Berkeley Pacman AI Projects](http://ai.berkeley.edu)，核心作者包括 John DeNero 和 Dan Klein。项目在该教学框架基础上完成搜索实验；使用与再分发遵循源码中的原始声明。

## 相关实验

[Lab 2 · Deep Learning](https://github.com/VincentLucifer/AI-Lab2-DeepLearning) · [Lab 3 · Reinforcement Learning](https://github.com/VincentLucifer/AI-Lab3-ReinforcementLearning)
