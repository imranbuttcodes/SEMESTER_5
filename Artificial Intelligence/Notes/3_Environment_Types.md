This is an **important AI topic** because once we define an agent using PEAS, we need to understand **what kind of environment that agent operates in**.

There are **six major environment properties** you should know.

# AI Environment Types

```text
                TASK ENVIRONMENT
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 Observable       Deterministic    Episodic
 vs Partial       vs Stochastic    vs Sequential
       │              │              │
       └──────────────┼──────────────┘
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Static vs       Discrete vs    Single vs
   Dynamic         Continuous     Multi-Agent
```

Let's understand **why each distinction exists**, rather than memorizing definitions.

---

# 1. Fully Observable vs Partially Observable

The question is:

> **Can the agent perceive the complete state of the environment?**

## Fully Observable

An environment is **fully observable** when the agent's sensors provide all the information needed to determine the current state relevant to decision-making.

Example: **Chess**

The entire board is visible:

```text
┌─────────────────┐
│ ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ │
│ ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ │
│                 │
│      BOARD      │
│                 │
│ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ │
│ ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ │
└─────────────────┘
```

The player can see:

- Every piece
- Every position
- Whose turn it is

So chess is **fully observable**.

---

## Partially Observable

The agent **cannot access the complete state**.

Example: **Self-driving car**

The car cannot know everything happening around it.

There could be:

- A vehicle behind another vehicle
- A pedestrian hidden behind a truck
- An obstacle around a corner
- Poor visibility because of fog

So:

```text
Reality:
┌───────────────────────────┐
│ 🚗      🚚       🚶      │
│           ?               │
└───────────────────────────┘
             ↑
       Agent can't see
       everything
```

Therefore:

\[
\boxed{\text{Self-driving} = \text{Partially Observable}}
\]

### Remember:

**Fully observable → agent sees the relevant state.**

**Partially observable → agent has incomplete information.**

---

# 2. Deterministic vs Stochastic

Now a completely different question:

> **Does the current state + action completely determine what happens next?**

## Deterministic

If the same action in the same state always produces the same result, the environment is deterministic.

Example:

### Chess

Suppose:

```text
Position = X
Action = Move pawn E2 → E4
```

The resulting position is predictable.

There isn't a random mechanism that sometimes moves your pawn somewhere else.

Therefore chess is **deterministic**.

---

## Stochastic

A stochastic environment involves **uncertainty/randomness**.

Example:

### Self-driving

The car decides:

> "Move forward."

But what happens next isn't completely predictable.

Another car might:

- Brake
- Accelerate
- Change lane
- Turn

A pedestrian might suddenly cross.

Therefore the result isn't completely determined by your action.

\[
\boxed{\text{Self-driving environment} \rightarrow \text{Stochastic}}
\]

### Simple distinction

```text
Deterministic:

State + Action
      │
      ▼
   One known
     result


Stochastic:

State + Action
      │
      ▼
 ┌────┼────┐
 ▼    ▼    ▼
 R1   R2   R3
(probabilities)
```

---

# 3. Episodic vs Sequential

This one is often confusing.

The question is:

> **Does the current decision affect future decisions?**

## Episodic

The agent's experience can be divided into independent **episodes**.

Each episode:

```text
Percept → Action → Result
```

doesn't significantly affect the next episode.

### Example: Image classification

Suppose an AI classifies images:

```text
Image 1 → Cat
Image 2 → Dog
Image 3 → Car
Image 4 → Bird
```

Getting Image 1 wrong doesn't change Image 2.

Therefore the tasks are independent.

\[
\boxed{\text{Image classification} = \text{Episodic}}
\]

---

## Sequential

In a sequential environment:

> **A current action affects future states and decisions.**

Chess is a perfect example.

```text
Move 1
  ↓
Board state 2
  ↓
Move 2
  ↓
Board state 3
  ↓
Move 3
  ↓
...
```

If you make a bad move now, it can affect the entire future game.

Therefore:

\[
\boxed{\text{Chess} = \text{Sequential}}
\]

### Remember:

> **Episodic = each decision is mostly independent.**

> **Sequential = decisions are connected through time.**

---

# 4. Static vs Dynamic

Question:

> **Can the environment change while the agent is deciding?**

## Static

A **static environment** doesn't change while the agent is thinking.

Classic example:

### Crossword puzzle

You can sit there and think:

```text
Think...
Think...
Think...
```

The crossword doesn't suddenly change because you took 10 seconds.

Therefore it's static.

---

## Dynamic

A **dynamic environment** can change while the agent is making its decision.

Example:

### Driving

You're deciding:

> "Should I turn left?"

While you're thinking:

```text
🚗 ← another car moves
🚶 ← pedestrian moves
🚦 ← traffic light changes
```

The environment changed.

Therefore:

\[
\boxed{\text{Driving} = \text{Dynamic}}
\]

### Important subtlety

There is also a term **semidynamic**.

The environment itself may not change, but the **performance measure changes with time**.

For example, chess with a timer:

```text
Board → unchanged
Clock → keeps running
```

The board is static, but your performance gets worse if you take too long.

---

# 5. Discrete vs Continuous

Question:

> **Are the states/actions/time represented as distinct values or continuously varying values?**

## Discrete

There are distinct, countable states or actions.

### Chess

Possible actions are individual moves:

```text
Move A
Move B
Move C
...
```

The board also consists of discrete squares.

Therefore chess is largely **discrete**.

---

## Continuous

Values can change continuously.

### Self-driving car

Consider:

- Speed = 47.23 km/h
- Steering angle = 13.72°
- Position = continuous coordinates
- Time = continuous

There are essentially infinitely many possible values.

Therefore driving is a **continuous environment**.

```text
Speed

0 ──────── 20 ──────── 40 ──────── 60
          ↑
       23.718...
```

### Remember:

> **Discrete = separate/countable states.**

> **Continuous = values can vary smoothly.**

---

# 6. Single-Agent vs Multi-Agent

Question:

> **Is there only one agent making decisions, or are there other agents whose behavior matters?**

## Single-Agent

Only one agent is acting.

Example:

### Sudoku-solving AI

```text
Environment
     │
     ▼
  AI Agent
```

There isn't another intelligent opponent trying to defeat it.

---

## Multi-Agent

Multiple agents interact.

Example:

### Chess

```text
      Environment
          │
     ┌────┴────┐
     ▼         ▼
  Player 1   Player 2
    Agent      Agent
```

Each player's decisions affect the other.

Therefore chess is a **multi-agent environment**.

Self-driving is also multi-agent because there are many autonomous/intelligent actors interacting on the road.

---

# Let's put everything together

Now let's classify some famous environments.

| Environment | Observable | Deterministic | Episodic | Static | Discrete | Agents |
|---|---|---|---|---|---|---|
| **Chess** | Fully | Deterministic | Sequential | Static* | Discrete | Multi |
| **Self-driving** | Partial | Stochastic | Sequential | Dynamic | Continuous | Multi |
| **Image classification** | Fully | Deterministic | Episodic | Static | Discrete | Single |
| **Sudoku** | Fully | Deterministic | Sequential | Static | Discrete | Single |
| **Robot vacuum** | Partial | Stochastic | Sequential | Dynamic | Continuous | Single/Multi depending on setup |

\*Chess becomes **semidynamic** when a clock affects the performance measure.

---

# The easiest way to solve exam questions

Don't memorize the table.

Ask **six questions**:

```text
1. Can I see everything?
       ↓
   Observable / Partial

2. Is the result predictable?
       ↓
   Deterministic / Stochastic

3. Does this action affect the future?
       ↓
   Episodic / Sequential

4. Can the world change while I think?
       ↓
   Static / Dynamic

5. Are states/actions distinct or continuous?
       ↓
   Discrete / Continuous

6. Am I alone or interacting with other agents?
       ↓
   Single / Multi-Agent
```

### The mental model

```text
             ENVIRONMENT
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 "Can I see?"  "Can I predict?" "Does it affect
                                  the future?"
     │            │            │
  Observable   Deterministic  Episodic
     │          /Stochastic   /Sequential
     │
     └────────────────────────────────┐
                                      │
                           "Does it change?"
                                      │
                                Static/Dynamic
                                      │
                              "Discrete values?"
                                      │
                              Discrete/Continuous
                                      │
                              "Other agents?"
                                      │
                              Single/Multi
```

**These properties describe the nature of the task environment in which an intelligent agent operates.** Once you understand them, the next concept—**types of intelligent agents (simple reflex, model-based, goal-based, utility-based, and learning agents)**—will make much more sense.