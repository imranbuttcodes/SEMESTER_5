The key question behind this topic is:

How does an AI agent decide what action to take?

Different agents answer that question differently.

# 1. The big picture

There are five commonly studied agent architectures in introductory AI:

- Simple Reflex Agents
- Model-Based Reflex Agents
- Goal-Based Agents
- Utility-Based Agents
- Learning Agents

And Intelligent Agent is the broader concept that encompasses these approaches. It isn't simply a sixth architecture alongside the other five.

## Intelligent Agent

Perceives the environment and selects actions

Simple Reflex

Current percept → rule

Model-Based Reflex

Percept + internal state

Goal-Based

Choose actions to reach a goal

Utility-Based

Choose actions by desirability

Learning Agent

Improves its behavior through experience and feedback

Let's use one running example—a robot vacuum cleaner—to understand the differences. This makes the distinctions much easier to remember.

# 2. Simple Reflex Agent

## Definition

A Simple Reflex Agent selects an action based only on the current percept, usually through condition–action rules.

In plain English:

> "If I perceive X, then do Y."

It doesn't use a remembered history of previous percepts to decide what to do.

## How does it work?

Current percept

What do I sense right now?

Condition–action rule

Match the percept to a rule

Action

Execute the matching action

### Example: Robot vacuum

Suppose its rules are:

| Current percept   | Action       |
| ----------------- | ------------ |
| Dirt detected     | Suck dirt    |
| Obstacle detected | Turn         |
| No dirt detected  | Move forward |

Imagine the robot detects dirt.

1. Sensor reports: `Dirt = YES`.
2. The agent matches the rule: `IF dirt, THEN suck`.
3. It activates the vacuum motor.

It doesn't need to plan a route or remember what happened five minutes ago.

### Advantages

- Simple to implement.
- Fast decision-making.
- Requires little memory.

### Limitations

- Can fail in partially observable environments.
- May repeat the same actions.
- Cannot independently plan toward a distant goal.

Key phrase for exams: Current percept only; condition–action rules.

# 3. Model-Based Reflex Agent

## Definition

A Model-Based Reflex Agent maintains an internal state representing aspects of the environment that it cannot determine from its current percept alone.

It uses an internal model of how the world works to update that state.

In plain English:

> "I consider what I sense now and what I know about the world from previous observations."

## Why do we need it?

Imagine a vacuum robot operating in two rooms.

### Room A

Robot's current room

### Room B

Adjacent room

The robot cleans Room A. Its dirt sensor now reports that the current room is clean, but the sensor doesn't tell it whether Room B has been cleaned.

A simple reflex agent might keep moving forward or repeat an unhelpful action.

A model-based agent can maintain an internal state such as:

```
Current location: Room A
Room A: Clean
Room B: Unknown
```

After moving to Room B and detecting dirt, it updates the state:

```
Current location: Room B
Room A: Clean
Room B: Dirty
```

It can use that information to respond appropriately.

## Architecture

Current percept

Update internal state

Previous state + new percept + world model

Apply condition–action rules

Execute action

### Advantages

- Handles incomplete observations better.
- Remembers relevant information through its internal state.
- Can account for how the environment changes.

### Limitations

- Needs an accurate enough model.
- Maintaining internal state adds complexity.
- Memory alone does not mean it can plan toward arbitrary goals.

Key phrase for exams: Internal state + model of the world.

# 4. Goal-Based Agent

## Definition

A Goal-Based Agent selects actions by considering whether they help achieve a specified goal.

Unlike a reflex agent, it doesn't merely match the current situation to a fixed rule. It can consider future states and possible action sequences.

In plain English:

> "What do I want to achieve, and which actions can get me there?"

## Example: Robot vacuum

Suppose the goal is:

\\[ \text{Goal: All rooms are clean} \\]

The robot knows Room A is clean but Room B is dirty.

It considers its options:

- Stay in Room A.
- Move to Room B.
- Clean Room B.

To achieve its goal, it chooses to move to Room B and then clean it.

Initial state

A = Clean, B = Dirty

Plan

Move to B → Suck dirt

Goal state

A = Clean, B = Clean

The goal-based agent evaluates possible future states and selects actions that help it reach the goal.

### What makes it different from a model-based reflex agent?

A model-based reflex agent maintains an internal state but may still act through fixed rules.

A goal-based agent uses its goal to guide its decision-making. It may need search or planning algorithms to determine which actions lead to the desired state.

For example, a goal-based agent could use BFS, DFS, or A\* to find a route to a destination.

### Advantages

- Can plan ahead.
- Can consider different action sequences.
- Can adapt its choice of actions when the goal or current state changes.

### Limitations

- Planning can be computationally expensive.
- Reaching a goal doesn't necessarily mean reaching it efficiently.
- It needs a way to represent goals and evaluate possible states.

Key phrase for exams: Goal-directed decision-making and planning.

# 5. Utility-Based Agent

## Definition

A Utility-Based Agent uses a utility function to evaluate how desirable different outcomes are and selects actions to maximize expected utility.

In plain English:

> "Several outcomes may achieve my goal, but which outcome is best?"

This is an important distinction: a goal tells the agent what it wants to achieve; utility helps it compare how desirable different outcomes are.

## Example: Robot vacuum

Suppose the robot has two ways to clean a room.

| Option  | Time  | Energy | Cleanliness |
| ------- | ----- | ------ | ----------- |
| Route A | 5 min | Low    | High        |
| Route B | 3 min | High   | High        |

Both routes achieve the goal of cleaning the room, but they have different costs.

A utility-based agent can evaluate the trade-off between time and energy.

For example, imagine we define:

\\[ U = 100C - 2T - 10E \\]

Where:

- \\(C\\) = cleanliness score
- \\(T\\) = time in minutes
- \\(E\\) = energy consumed in some defined units
- \\(U\\) = utility score

These numbers are illustrative, not a universal formula.

The agent calculates the utility of each possible outcome and prefers the one with the higher score.

If Route A has a utility of 80 and Route B has a utility of 65, it chooses Route A.

The point is not the particular numbers. The point is that the agent can compare outcomes instead of merely checking whether the goal was achieved.

## What about uncertainty?

Suppose a self-driving car must choose between two routes:

- Route A is short but has a high probability of traffic.
- Route B is longer but is usually clear.

A utility-based agent can compare the expected utility of the alternatives.

\\[ EU(a)=\sum_i P(s_i\mid a)\\,U(s_i) \\]

Here:

- \\(a\\) = an action
- \\(s_i\\) = a possible outcome
- \\(P(s_i\mid a)\\) = probability of that outcome after taking the action
- \\(U(s_i)\\) = utility of that outcome

The agent weighs both the desirability of an outcome and how likely it is to occur.

### Advantages

- Handles trade-offs between competing objectives.
- Can compare multiple successful outcomes.
- Can make decisions under uncertainty using expected utility.

### Limitations

- Designing a useful utility function can be difficult.
- Incorrect utility values can produce undesirable choices.
- Evaluating many possible outcomes can be expensive.

Key phrase for exams: Utility function, preferences, trade-offs, and expected utility.

# 6. Learning Agent

## Definition

A Learning Agent improves its behavior through experience.

Instead of relying entirely on behavior specified in advance, it can learn from feedback and modify its decision-making over time.

In plain English:

> "I will learn from my experience and try to perform better in the future."

A classic learning-agent architecture contains four components.

## Learning Agent

Four interacting components

1\. Learning Element

Improves the agent's behavior using experience and feedback.

2\. Performance Element

Selects actions based on the agent's current knowledge.

3\. Critic

Evaluates how well the agent is performing and provides feedback to the learning element.

4\. Problem Generator

Suggests exploratory actions that can help the agent discover better behavior.

These components are particularly important for exams.

### Let's understand them with an example

Imagine a robot vacuum that learns which cleaning routes are effective.

Step 1 — Performance element: The robot chooses a route and cleans the room.

Step 2 — Critic: It receives feedback about the cleaning quality, time taken, and energy used.

Step 3 — Learning element: It updates its route-selection strategy based on the feedback.

Step 4 — Problem generator: It may try a different route to discover whether that route performs better.

Over multiple attempts, the robot may discover more efficient cleaning strategies.

```
Choose action
     ↓
Observe result
     ↓
Evaluate performance
     ↓
Learn from feedback
     ↓
Improve future decisions
     ↺
```

This is a conceptual example; actual learning systems may use supervised learning, reinforcement learning, or other techniques.

### Advantages

- Can improve with experience.
- Can adapt to changing conditions.
- Can discover patterns that weren't explicitly programmed.

### Limitations

- Requires suitable data or feedback.
- Learning may be slow or computationally expensive.
- Poor data or feedback can lead to poor behavior.

Key phrase for exams: Experience, feedback, and improvement over time.

# 7. What exactly is an Intelligent Agent?

Let's return to the broader concept.

An Intelligent Agent perceives its environment through sensors and acts on it through actuators, selecting actions to achieve its objectives.

In AI, we often describe its behavior using an agent function:

\\[ f:\text{Percept Sequences}\rightarrow\text{Actions} \\]

This means the agent function maps the history of percepts available to the agent to an action.

For a simple reflex agent, the decision depends on the current percept. Other agents may also use internal state, goals, utility calculations, or learned knowledge.

An agent is considered rational when it selects actions expected to maximize its performance measure, given its percepts, knowledge, and available actions.

An intelligent agent may be implemented using any of the architectures we just studied. These categories describe different decision-making mechanisms; they are not mutually exclusive in every implementation. For example, an agent can be both goal-based and learning-based.

# 8. Final comparison — memorize this table

| Agent type         | Main basis for action                    | Internal state?                                        | Plans ahead?          | Learns from experience? |
| ------------------ | ---------------------------------------- | ------------------------------------------------------ | --------------------- | ----------------------- |
| Simple Reflex      | Current percept and rules                | Not required                                           | Not inherently        | Not inherently          |
| Model-Based Reflex | Percept, internal state, model, rules    | Yes                                                    | Not inherently        | Not inherently          |
| Goal-Based         | Goals and possible future states         | Often                                                  | Yes, often            | Not inherently          |
| Utility-Based      | Utility of possible outcomes             | Often                                                  | Often                 | Not inherently          |
| Learning Agent     | Current policy plus learned improvements | Usually some form of learned or maintained information | Depends on its design | Yes, by definition      |

Remember that "not inherently" means the architecture doesn't require that capability; it doesn't mean the capability could never be added.

## Test your understanding

## Quick quiz

0 of 4 answered

1\. A robot follows the rule: IF dirt is detected, THEN suck. Which agent is this?

Simple Reflex

Goal-Based

Utility-Based

2\. A robot remembers which rooms it has already cleaned, even when it cannot currently see those rooms. Which architecture best describes this?

Simple Reflex

Model-Based Reflex

Utility-Based

3\. An agent compares two routes that both reach its destination, preferring the one with the best balance of safety and travel time. Which architecture is most relevant?

Simple Reflex

Goal-Based only

Utility-Based

4\. A robot updates its route strategy after receiving feedback about cleaning quality. Which type is it?

Learning Agent

Simple Reflex only

Static agent

Reset quiz

Bro, the most important distinctions to carry forward are these:

- Simple reflex → What do I perceive right now?
- Model-based reflex → What do I know about the current state?
- Goal-based → How can I reach my goal?
- Utility-based → Which outcome is most desirable?
- Learning → How can I improve from experience?

Once these differences are clear, you're ready to study how these agents actually search for solutions using BFS, DFS, Uniform Cost Search, and A\*.