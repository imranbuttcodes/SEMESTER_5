# 1. First, imagine you're solving a maze

You're standing at the entrance of a maze. Your goal is to reach the exit.

🚪

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

⬜

🏁

Imagine that every reachable position is a state. You need to find a route from the entrance to the finish.

At every position, you might have several possible moves. You need a systematic way to decide:

- Where can I go next?
- Which places have I already checked?
- Have I reached the exit?

That is exactly the kind of problem a search algorithm solves.

# 2. What the hell is a frontier?

The frontier is the collection of discovered states that are waiting to be explored.

That's it, bro. This is the most important definition.

Imagine you're exploring a building:

- You have discovered three rooms.
- You've already inspected one room.
- Two other discovered rooms are waiting for you to inspect them.

Those two rooms are your frontier.

In AI search, a frontier is also called the open list or fringe.

There are three important things to distinguish:

Frontier

States discovered but not yet explored.

Explored set

States whose successors have already been examined.

Goal state

The state we're trying to reach.

Think of it this way:

- Frontier: What should I explore next?
- Explored set: What have I already explored?
- Goal test: Have I found what I'm looking for?

Now let's see why your slide needs all those steps.

# 3. Understand the algorithm with a tiny graph

Suppose our search problem is represented by this graph:

A = Start

G = Goal

The connections are A → B, A → C, B → G, and C → G.

For this example, we'll use a simple search strategy that removes the oldest discovered node first. This is Breadth-First Search (BFS). Your slide gives a general search procedure; the rule for choosing the next frontier node determines which search algorithm you get.

## Step 1: Start with the initial state in the frontier

Initially, we haven't explored anything.

| Frontier | Explored set |
| -------- | ------------ |
| A        | Empty        |

Why?

Because A is where we start. It has been discovered, but we haven't explored its successors yet.

## Step 2: Remove a node from the frontier

We remove A.

| Frontier | Explored set |
| -------- | ------------ |
| Empty    | Empty        |

Now A is the node we're actively processing.

## Step 3: Check whether A is the goal

Is A equal to G?

No.

So we continue.

## Step 4: Add A to the explored set

We've now processed A.

| Frontier | Explored set |
| -------- | ------------ |
| Empty    | A            |

## Step 5: Expand A

Expand means generate the immediate successor states of a node.

A has two successors: B and C.

We add both to the frontier because neither has been discovered or explored yet.

| Frontier | Explored set |
| -------- | ------------ |
| B, C     | A            |

Now we have two discovered states waiting to be explored.

THAT is the frontier! B and C are waiting their turn.

## Step 6: Remove B and expand it

B is the oldest state in the frontier, so we remove it and check whether it's the goal.

B isn't G, so we add B to the explored set. Its successor is G, which is neither in the frontier nor in the explored set. Add G to the frontier.

| Frontier | Explored set |
| -------- | ------------ |
| C, G     | A, B         |

Notice something: C is still waiting. We don't forget it just because we explored B.

## Step 7: Remove C and expand it

C isn't the goal, so we add C to the explored set.

C also leads to G. But G is already in the frontier!

We don't add G a second time.

| Frontier | Explored set |
| -------- | ------------ |
| G        | A, B, C      |

## Step 8: Remove G and check the goal

We remove G from the frontier.

Is G the goal? Yes!

The algorithm stops and returns a solution path: A → B → G.

### The whole search, at a glance

| Step     | Frontier | Explored |
| -------- | -------- | -------- |
| Start    | A        | —        |
| Expand A | B, C     | A        |
| Expand B | C, G     | A, B     |
| Expand C | G        | A, B, C  |
| Select G | —        | A, B, C  |

Goal found: A → B → G

# 4. Now, why does every step exist?

Let's translate your slide into normal English.

### 1

Put the initial state in the frontier.

The algorithm needs somewhere to begin.

### 2

Start with an empty explored set.

At the beginning, no states have been fully explored.

### 3

If the frontier is empty, there is no solution to report.

Nothing remains to explore, and no goal has been found. This assumes the search is complete for the problem and no other states remain to be considered.

### 4

Remove a node from the frontier.

Choose the next state to process. BFS chooses the oldest; DFS chooses the newest. Other algorithms use different rules.

### 5

Check the goal.

If this node is the goal, stop and return the path used to reach it.

### 6

Add the node to the explored set.

Record that you've processed its successors, helping avoid repeated work.

### 7

Expand it and add new states to the frontier.

Discover its successors, but skip states already waiting in the frontier or already explored. This helps avoid duplicate work and cycles.

## 5. One subtle but important detail

Your slide says to check whether the node contains the goal state after removing it from the frontier.

That means a node can sit in the frontier for a while before the algorithm selects it. Being discovered is not the same as being explored, and neither automatically means the goal has been reached.

Also, a search node should retain enough information about its parent (or path) to reconstruct the solution when the goal is found. The frontier is not just a bag of state names; implementations often store search nodes containing the state, parent, action, and sometimes path cost.

## Quick check, bro

Suppose:

- Frontier = `[B, C, D]`
- Explored set = `{A}`
- The algorithm removes B and expands it.
- B produces successors A, C, and E.

Which successors should be added to the frontier?

A, C, and E

Only E

C and E

Once this clicks, you're ready for the next concept: how changing the frontier's removal rule gives us BFS versus DFS.