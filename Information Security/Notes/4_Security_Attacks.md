# Security Attacks: Passive vs Active

At the highest level:

$$
\boxed{\text{Security Attacks} = \text{Passive} + \text{Active}}
$$

The fundamental difference is:

> **Passive = attacker observes.** 👀
> **Active = attacker changes/disrupts.** 💥

---

# 1. Passive Attack

A **passive attack** happens when the attacker **only monitors, listens to, or collects information**.

The attacker does **not modify the data** and generally doesn't directly disrupt the system.

Think:

> **"I'm just watching."**

### Example

Suppose you're sending:

```text
Imran ────────────────► Server
       "My password is ABC123"
```

An attacker secretly monitors the network:

```text
                 👀
                 │
Imran ───────────┼──────────► Server
                 │
              Attacker
```

The attacker reads/captures the communication but doesn't change it.

That's a:

$$
\boxed{\text{Passive Attack}}
$$

---

# 2. Main Types of Passive Attacks

There are two major examples you should know.

## A. Eavesdropping / Interception

The attacker **listens to communication** to obtain information.

Example:

You're using an unsecured network:

```text
Your Laptop ─────────► Server
             │
             └──────► Attacker 👀
```

The attacker captures things such as:

* Messages
* Credentials
* Emails
* Network traffic
* Sensitive information

### Goal:

**Steal information without modifying it.**

This primarily attacks:

$$
\boxed{\text{Confidentiality}}
$$

---

## B. Traffic Analysis

Here's a slightly more interesting one.

Suppose the communication is encrypted:

```text
Alice ──🔐 encrypted data ──► Bob
```

The attacker can't read the actual message.

But they can observe things like:

* Who is communicating
* When they communicate
* How frequently
* How much data is transmitted
* Communication patterns

For example:

```text
Alice ───────────────► Bob
      10:00 AM

Alice ───────────────► Bob
      10:02 AM

Alice ─────────────────────► Bob
      10:05 AM
```

Even though the content is encrypted, the **pattern itself can reveal information**.

That's **traffic analysis**.

---

# 3. Active Attack

Now the attacker doesn't just watch.

They **do something to the communication/system**.

Think:

> **"I'm going to interfere with it."**

For example:

```text
Alice ───────────────► Bob
          ↑
       Attacker
          │
       modifies
       message
```

The attacker could:

* Modify data
* Delete data
* Insert fake data
* Replay old messages
* Impersonate someone
* Crash/disrupt a service

That's an:

$$
\boxed{\text{Active Attack}}
$$

---

# 4. Main Types of Active Attacks

There are four classic categories you should know.

---

## A. Modification

Attacker **changes the original information**.

Suppose Alice sends:

```text
"Transfer 1,000 PKR"
```

Attacker changes it to:

```text
"Transfer 100,000 PKR"
```

Then sends it to the server.

```text
Alice
 │
 │ "Transfer 1,000"
 ▼
Attacker
 │
 │ changes it
 ▼
Server
 │
 └── "Transfer 100,000"
```

That's an active attack because the attacker **modified the data**.

Main CIA violation:

$$
\boxed{\text{Integrity}}
$$

---

# B. Fabrication

The attacker **creates fake information** and sends it as if it were legitimate.

Example:

The attacker sends:

```text
"Transfer 50,000 PKR to Attacker"
```

even though Alice never requested it.

```text
Attacker
    │
    │ FAKE MESSAGE
    ▼
 Server
```

That's **fabrication**.

The attacker is essentially **injecting fake data** into the system.

---

# C. Replay Attack

This one is extremely important.

The attacker captures a legitimate message:

```text
Alice ──► Server

"Transfer 5,000 PKR"
```

The attacker records it:

```text
Attacker 👀
      │
      └── saves message
```

Later, the attacker sends the **same legitimate message again**:

```text
Attacker ──► Server

"Transfer 5,000 PKR"
```

The attacker didn't necessarily modify the original message.

Instead, they **reused it**.

That's a:

$$
\boxed{\text{Replay Attack}}
$$

This is why systems use things like:

* Nonces
* Timestamps
* Sequence numbers
* Session tokens

to ensure an old message can't simply be reused.

---

# D. Denial of Service (DoS)

This attack focuses on **availability**.

The attacker overwhelms or disrupts a service so legitimate users can't access it.

For example:

```text
        Attacker
       ↙ ↓ ↓ ↓ ↘
      ↙  ↓ ↓ ↓  ↘
     ┌─────────────┐
     │   Server    │
     │  💥💥💥💥   │
     └─────────────┘
           ❌
      Legitimate user
        can't access
```

Example:

**DDoS attack**

Thousands/millions of malicious requests are sent to a server.

The server becomes overloaded.

Therefore:

$$
\boxed{\text{Availability is violated}}
$$

---

# 5. Passive vs Active — The Big Difference

Here's the table I'd memorize:

|                           | Passive            | Active                |
| ------------------------- | ------------------ | --------------------- |
| Attacker observes?        | ✅                  | Sometimes             |
| Attacker modifies data?   | ❌                  | ✅                     |
| Attacker disrupts system? | ❌                  | ✅                     |
| Main goal                 | Obtain information | Alter/disrupt/deceive |
| Example                   | Eavesdropping      | Modification          |
| Example                   | Traffic analysis   | Replay                |
| Example                   | —                  | DoS                   |

---

# 6. Connect it to CIA

This is where your previous topic becomes useful.

### Passive attacks

Generally target:

$$
\boxed{\text{Confidentiality}}
$$

Because the attacker is trying to **learn information**.

```text
Passive
   ↓
"I want to SEE"
   ↓
Confidentiality 🔒
```

### Active attacks

Often target:

$$
\boxed{\text{Integrity + Availability}}
$$

because the attacker can:

* Change information → **Integrity**
* Disrupt service → **Availability**

```text
Active
   ↓
"I want to CHANGE / DISRUPT"
   ↓
Integrity 🛡️
Availability ⚡
```

---

# 🔥 The easiest way to identify them in an exam

Ask yourself:

### **Did the attacker only WATCH?**

→ **Passive**

### **Did the attacker CHANGE, INSERT, REPLAY, or DISRUPT something?**

→ **Active**

For example:

> "An attacker captures network traffic but doesn't modify it."

**Passive** ✅

> "An attacker changes the amount in a transaction."

**Active** ✅

> "An attacker records a valid transaction and sends it again."

**Active — Replay** ✅

> "An attacker floods a server with requests so users cannot access it."

**Active — DoS/DDoS** ✅

---

## One sentence to lock it in 🧠

> **Passive attack = "I watch you."** 👀
> **Active attack = "I interfere with you."** 💥
