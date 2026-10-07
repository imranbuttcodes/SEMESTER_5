**PEAS** is one of the first things you should properly understand in Intelligent Agents because it gives us a systematic way to **define an agent's task environment**.

# PEAS

**PEAS** stands for:

$$
\boxed{\text{P = Performance Measure}}
$$

$$
\boxed{\text{E = Environment}}
$$

$$
\boxed{\text{A = Actuators}}
$$

$$
\boxed{\text{S = Sensors}}
$$

The idea is simple:

> Before designing an intelligent agent, we need to clearly define **what success means, where the agent operates, how it can act, and what it can perceive.**

---

# 1. P — Performance Measure

The **Performance Measure** tells us:

> **How do we determine whether the agent is doing a good job?**

This is extremely important because a rational agent is trying to **maximize its performance measure**.

For example, consider a **self-driving car**.

What would make it successful?

* Avoid accidents
* Reach destination
* Follow traffic rules
* Minimize travel time
* Minimize fuel/energy consumption
* Provide passenger comfort

Those become part of its performance measure.

```text
             SELF-DRIVING CAR
                    │
                    ▼
           Performance Measure
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Safety       Time       Traffic Rules
```

### Important distinction

**Performance measure ≠ goal stated in natural language only.**

It's the criterion by which we **evaluate the agent's behavior**.

---

# 2. E — Environment

The **Environment** is:

> **Everything external to the agent that it interacts with.**

For our self-driving car:

```text
Environment
├── Roads
├── Other vehicles
├── Pedestrians
├── Traffic lights
├── Buildings
├── Weather
├── Road signs
└── Road conditions
```

The car doesn't control all of these things.

It has to **operate within this environment**.

---

# 3. A — Actuators

Actuators are:

> **The mechanisms through which the agent performs actions on the environment.**

For a self-driving car:

```text
Agent
 │
 ├── Steering
 ├── Accelerator
 ├── Brakes
 ├── Gear system
 └── Turn signals
```

These allow the agent to physically affect the environment.

Think:

> **Actuator = How can the agent act?**

---

# 4. S — Sensors

Sensors are:

> **The mechanisms through which the agent obtains information about its environment.**

For a self-driving car:

```text
Sensors
├── Cameras
├── LiDAR
├── Radar
├── GPS
├── Ultrasonic sensors
└── IMU
```

Think:

> **Sensor = How can the agent perceive?**

---

# Putting PEAS together

Let's take the complete self-driving-car example.

| PEAS                | Self-driving car                                           |
| ------------------- | ---------------------------------------------------------- |
| **P — Performance** | Safety, obey laws, reach destination, minimize time/energy |
| **E — Environment** | Roads, traffic, pedestrians, weather, traffic lights       |
| **A — Actuators**   | Steering, brakes, accelerator, gears, indicators           |
| **S — Sensors**     | Cameras, LiDAR, radar, GPS, IMU                            |

So we can represent it as:

```text
                 SELF-DRIVING CAR
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   PERFORMANCE    ENVIRONMENT     SENSORS
        │              │              │
        │              │              ▼
        │              │         Percepts
        │              │              │
        │              ▼              │
        │         Physical World      │
        │              ▲              │
        │              │              │
        └──────────────┼──────────────┘
                       ▲
                       │
                  ACTUATORS
```

---

# Why do we need PEAS?

Suppose someone says:

> "Let's build an AI agent for driving."

That's too vague.

We need to ask:

### What does success mean?

→ **Performance**

### Where does it operate?

→ **Environment**

### How can it act?

→ **Actuators**

### What can it observe?

→ **Sensors**

That's exactly what PEAS gives us.

---

# Another example: Vacuum Cleaner Agent

This is a very common AI exam question.

### PEAS for a vacuum-cleaning robot

**P — Performance**

* Maximum cleanliness
* Minimum time
* Minimum energy consumption
* Avoid collisions

**E — Environment**

* Rooms
* Floors
* Walls
* Furniture
* Dirt

**A — Actuators**

* Wheels
* Vacuum motor
* Brush mechanism

**S — Sensors**

* Dirt sensor
* Camera
* Distance sensor
* Position sensor

So:

```text
P → Clean efficiently
E → Rooms/floors/furniture
A → Wheels + vacuum motor
S → Dirt + distance + camera sensors
```

---

# The trick for remembering PEAS

Think of it as four questions:

```text
P → "How do I know I'm doing well?"
E → "Where am I operating?"
A → "How can I affect the world?"
S → "How can I observe the world?"
```

Or even simpler:

> **P = Success**
> **E = World**
> **A = Action**
> **S = Perception**

And notice how this connects everything we've learned:

```text
              ENVIRONMENT
                   │
                   │ percepts
                   ▼
                SENSORS
                   │
                   ▼
             INTELLIGENT
                AGENT
                   │
              decision
                   │
                   ▼
               ACTUATORS
                   │
                   │ actions
                   ▼
              ENVIRONMENT

          P = How we judge
              the agent
```

**PEAS defines the task environment of an agent.**

That's the core idea. Next, the natural step is **Task Environment Properties** — things like **fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, and single/multi-agent**. These are heavily connected to PEAS and are very common exam material.
