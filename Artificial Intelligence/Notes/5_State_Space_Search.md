Problem Solving Using Search.

Since we've already studied agents, environments, and the meaning of a state, we're ready for the next step. These concepts connect directly to State Space Search.

# 1. Problem Solving Using Search

Imagine you're playing the 8-puzzle game.

# 1

# 2

# 3

# 4

# 5

# 6

# 7

#

# 8

Initial state: the blank cell is represented by 0.

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

#

Goal state: tiles arranged in the desired order.

You know the starting arrangement and the desired arrangement. But how do you find the moves that transform one into the other?

You could try moving the blank cell randomly. However, that might take you away from the goal or make you repeat the same arrangements.

Problem-solving using search gives an AI agent a systematic way to explore possible actions and find a path from the initial state to the goal state.

## 2. What is State Space Search?

Let's define it properly.

State Space Search is a problem-solving technique in which an agent explores possible states of a problem by applying available actions until it finds a state that satisfies the goal.

Break that definition into four ideas:

- State: A particular situation or configuration of the problem.
- Action: A move that can be performed in a state.
- State space: The collection of states that can potentially be reached.
- Search: The process of exploring those states to find a solution.

For example, in the 8-puzzle:

| Concept       | Example                                      |
| ------------- | -------------------------------------------- |
| State         | Current arrangement of the tiles             |
| Action        | Move the blank cell up, down, left, or right |
| State space   | All reachable tile arrangements              |
| Initial state | The given starting arrangement               |
| Goal state    | The required final arrangement               |
| Solution      | A sequence of moves reaching the goal        |

## 3. How does the search work?

Consider this small example. An agent wants to travel from city A to city D.

Possible routes: A → B → D or A → C → D

The agent starts at A. It explores the available paths and checks whether it has reached D.

1. Start at A.
2. Explore a possible next state, B.
3. From B, explore D.
4. If D is the goal, stop and return the path A → B → D.

Another valid route is A → C → D.

Notice something important: search is not just about reaching the goal; the best path may depend on the problem's requirements. If the routes have different costs, the agent may need to find the cheapest route rather than simply the first route it discovers.

## 4. What exactly is a state space?

A state space is the set of all possible states relevant to solving a problem.

Think of it as a map of possibilities. Each state is a location on that map, and each legal action allows the agent to move from one state to another.

For example:

Initial state

State A

State B

State C

Goal state

This diagram is illustrative: from one state, there may be multiple possible next states, and different paths can lead to the same state.

## 5. How do we formulate a search problem?

In classical AI, a search problem is commonly defined using five components:

1. Initial state: Where the agent begins.
2. Actions: What the agent can do in each state.
3. Transition model: What state results from performing an action.
4. Goal test: How the agent checks whether the goal has been reached.
5. Path cost: The total cost of the actions taken along a path.

Let's apply them to the 8-puzzle.

| Component        | 8-puzzle example                                     |
| ---------------- | ---------------------------------------------------- |
| Initial state    | The starting tile arrangement                        |
| Actions          | Move the blank cell legally                          |
| Transition model | The resulting tile arrangement after a move          |
| Goal test        | Check whether the tiles match the target arrangement |
| Path cost        | Number of moves, if every move costs 1               |

These five components tell the search algorithm where to start, what it can do, how the world changes, when to stop, and how to evaluate a solution.

## Quick check before we continue

Question: In the 8-puzzle, suppose the blank cell moves one position to the left. What does the resulting arrangement represent?

The action

A new state

The entire state space

The goal test

Check answer

Correct!

The action is moving the blank cell left. The new state is the resulting arrangement after that move.

Once this distinction is clear, the next natural topic in your slides is usually search trees, nodes, and the difference between a state space and a search tree.