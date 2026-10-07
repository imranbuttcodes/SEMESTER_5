# 1. What is an Agent?

In AI, an **agent** is something that:

> **perceives its environment and takes actions in that environment.**

The simplest model is:

```text
Environment
    │
    │ percept
    ▼
┌─────────┐
│  AGENT  │
└─────────┘
    │
    │ action
    ▼
Environment
```

There are two important words here:

### Percept

A **percept** is what the agent receives from its environment through its sensors.

For example, imagine a self-driving car:

```text
Environment
     │
     ▼
 Cameras, GPS, LiDAR, sensors
     │
     ▼
   Agent
```

The agent might perceive:

* Red traffic light
* Car ahead
* Pedestrian crossing
* Current speed
* GPS position

### Action

An **action** is what the agent does to affect the environment.

The car might:

* Brake
* Accelerate
* Turn left
* Turn right
* Change lanes

So:

$$
\boxed{\text{Agent} = \text{Perceives} + \text{Acts}}
$$

That's the fundamental idea.

---

# 2. What is an Intelligent Agent?

Now we add **intelligence**.

An **intelligent agent** is an agent that can:

> **perceive its environment and choose actions that help it achieve its goals.**

Think about a simple thermostat.

```text
Temperature Sensor
       │
       ▼
   Thermostat
       │
       ▼
 Heater ON/OFF
```

Suppose the desired temperature is:

$$
22^\circ C
$$

If the thermostat detects:

$$
18^\circ C
$$

it turns the heater ON.

If it detects:

$$
23^\circ C
$$

it turns the heater OFF.

It's not merely reacting randomly. It is using its perception to select an action according to a goal.

So:

```text
Agent
  │
  ├── Perceives environment
  │
  ├── Processes information
  │
  └── Takes action toward a goal
           ↓
       Intelligent Agent
```

---

# 3. What is a Rational Agent?

This is the **important one** in AI.

A **rational agent** is an agent that:

> **chooses the action expected to maximize its performance measure, given the information it has perceived and the knowledge it possesses.**

In simpler words:

> **A rational agent chooses the best action it can, based on what it currently knows.**

Notice the phrase:

### "based on what it currently knows"

This is extremely important.

A rational agent **doesn't have to be perfect**.

---

## Example

Imagine you're driving and suddenly see this:

```text
              Road
                │
                │
         🚗     │
                │
        🟢 Green light
                │
```

You know:

* Light is green
* Road is clear
* No pedestrian is crossing

A rational action is:

**Continue driving.**

Now imagine:

```text
         🚗
          │
          │
      🔴 Red light
          │
          │
      Pedestrian
```

A rational action is:

**Brake.**

The agent chooses actions based on its available information and its objective.

---

# The crucial difference

Let's put all three together.

| Term                  | Meaning                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Agent**             | Something that perceives and acts                                                                                    |
| **Intelligent Agent** | An agent that uses its perceptions to make decisions toward goals                                                    |
| **Rational Agent**    | An intelligent agent that chooses the action expected to produce the best outcome according to a performance measure |

So conceptually:

```text
                    AGENT
                      │
             perceives + acts
                      │
                      ▼
              INTELLIGENT AGENT
                      │
              goal-directed
                      │
                      ▼
                RATIONAL AGENT
                      │
             maximizes performance
```

---

# 4. Why do we say "rational" instead of "perfect"?

This is where many students get confused.

Suppose you're playing chess.

Your AI agent has this position:

```text
      Chess Position
            │
            ▼
       Analyze moves
        /    |    \
       A     B     C
       │     │     │
       ▼     ▼     ▼
     Result Result Result
```

The agent chooses the move it believes is best.

But suppose it chooses **B**, and later discovers that **A** would actually have won the game.

Was the agent irrational?

**Not necessarily.**

If, given everything the agent knew at the time, **B was the best expected action**, then it was rational.

That's why:

$$
\boxed{\text{Rational} \neq \text{Perfect}}
$$

Instead:

$$
\boxed{\text{Rational} = \text{Best expected action given available information}}
$$

---

# 5. The formal definition

This is the definition you'll probably encounter in your AI textbook:

> **A rational agent is one that, for each possible percept sequence, selects an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.**

There are four important components hiding inside that definition:

```text
                 Rational Agent
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Percepts       Knowledge     Performance
                                    Measure
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                   Action
```

The agent asks, essentially:

> **"Given what I've observed and what I know, which action should I take to maximize my performance?"**

---

# 6. One example to connect everything

Consider a **vacuum-cleaning robot**.

![Image](https://images.openai.com/static-rsc-4/MYZ_zXPByRsfcaNH3W7-pWo4l3LB5pBoDu1qrbGY1XCqw2Ns3YNXlON_WVRWNO-dVwBLecslYDThJPbz5SuHLdvJJW9NKJ8D5CwBYF5DsoEIHAC2lJPl3h6wxof_m67I4WU3adwWI8i6SE8f_UXneKiJtfFCxdWzFuqo1SUqqFw8CF6cb0GAwzB7583URpK6?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YKFqQsHmOqti1xR0I80jsRzNCqirV555iSMo_EEVFStNUBSEeuLS5ze1pYuHd5oK_1J-BvKvVSvre0TMzM5lVXpkrbNFU14k2fpQwNapKOdcAwfc_sakZaKb8y1uS0w4-hASYIEgHoTkxFDmquXJe4GyibhH6MT-TZEG638QYDSomqSYU9n7w1jMb7FeEOcx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/EQpom4OT7WLDvvoujDhSMYb7483vlZLFTOyQIvOmjlBZnwWL015u4DhwJnqCVa1SBta2ml2jSE8GBptHYOvclauJrEAlpF-kGJSryadF4a6ubmrANeULK8yVy1P0e8l8qfGett7Id28TUTWVL1db1vBefYQlvex7E4PSkdRnBF12kiqjoqQvEx67qUcvgysa?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/hTC5mIWqM6UwPhvTvBF10YN-9bVPx-ZDJ9dYbqHOt6QyEFQ2Wy0SmbHGaey8aqT3GL490k_oQms07pAX_n9S5OU-a8SYRmDashxL9emWCFA4QWS2aEnpWocbiFms7y_ZXUigRyE-sigZqtuQfIPpHPI_fgicOI5XJG7PTUjnfnp6rdJqJ-BoVnOFDr-PzTgE?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QsZimjulSIPRBKkK8IUPwf1mct59gvUchxJSdrmIoBEhFXjqEhMZKzgfs-cuLPBzk2DgHAdgPsJVr3L9AZbxq0hFucdX2W-CZODTFhPpnqYaVRlJfZ6YE1a43V89beOKBuT5l_S7QmGF1X3_pwIdejeNu_CyvHQ1HtFWDT3fplYVYpd-Sx_1sLPLgJ1hkYBQ?purpose=fullsize)

Environment:

```text
┌─────────────┬─────────────┐
│             │             │
│   Room A    │   Room B    │
│    🗑️       │    🧹       │
│             │             │
└─────────────┴─────────────┘
```

The robot has sensors.

It perceives:

```text
Current location = A
Dirt detected = YES
```

It can perform actions:

```text
SUCK
MOVE LEFT
MOVE RIGHT
```

### Agent

It senses the room and performs actions.

### Intelligent agent

It uses the information to decide what to do.

### Rational agent

It chooses actions that maximize its **performance measure**, perhaps:

> Clean as much dirt as possible while minimizing time and energy.

So if it detects dirt:

```text
Percept:
"A + Dirt"

        ↓

Action:
"SUCK"
```

If room A is clean:

```text
Percept:
"A + Clean"

        ↓

Action:
"Move to B"
```

And if the performance measure rewards cleanliness and penalizes wasted movement, the agent has to balance both.

---

# The key idea to remember

Don't memorize three isolated definitions.

Think of the progression:

```text
AGENT
"I can perceive and act."

        ↓

INTELLIGENT AGENT
"I can use what I perceive to make
goal-directed decisions."

        ↓

RATIONAL AGENT
"I will choose the action that I
expect will give me the best performance,
given what I currently know."
```

And **rationality is one of the central ideas of AI** because a huge portion of AI can be framed as:

$$
\boxed{
\text{Perceive}
\rightarrow
\text{Reason/Decide}
\rightarrow
\text{Act}
}
$$

That's the foundation we'll build on before getting into **PEAS and task environments**, which naturally comes next.
