# Risk Reduction Leverage (RRL)

The basic question is:

> **"How much risk am I removing for every dollar I spend on the security control?"**

That's the whole idea.

---

## 1. First, remember our previous example

Suppose:

* Asset = **$100,000**
* Exposure Factor = **40%**
* SLE = **$40,000**
* Probability of attack = **20%**

So:

$$
Risk\ Exposure = 40,000 \times 0.20
$$

$$
= \$8,000
$$

So **before implementing any security control**, our expected risk exposure is:

$$
\boxed{\$8,000}
$$

---

# 2. Now we buy a security control

Suppose we install a security solution that reduces the probability of the attack.

After implementing it, our expected risk exposure falls to:

$$
\$2,000
$$

So how much risk did we reduce?

$$
Risk\ Reduction = 8,000 - 2,000
$$

$$
\boxed{\$6,000}
$$

We've reduced our expected loss by **$6,000**.

---

# 3. But the security control costs money

Suppose the security control costs:

$$
\$2,000
$$

Now we ask:

> "Was spending $2,000 worth it to reduce $6,000 of risk?"

That's where **Risk Reduction Leverage** comes in.

### Formula

$$
\boxed{
RRL =
\frac{Risk\ Reduction}{Cost\ of\ Safeguard}
}
$$

So:

$$
RRL = \frac{6,000}{2,000}
$$

$$
\boxed{RRL = 3}
$$

---

# 4. What does RRL = 3 mean?

This is the important part.

It means:

> **For every $1 spent on the security control, we reduce approximately $3 of expected risk.**

So:

```text
             $2,000
              spent
                │
                ▼
        Security Control
                │
                ▼
       $6,000 risk reduction
```

Therefore:

$$
\frac{\$6,000}{\$2,000}=3
$$

**RRL = 3**

---

# 5. Let's make it even simpler

Imagine three security controls:

| Control    |   Cost | Risk Reduction |   RRL |
| ---------- | -----: | -------------: | ----: |
| Firewall A | $2,000 |         $6,000 | **3** |
| Firewall B | $5,000 |        $10,000 | **2** |
| Firewall C | $4,000 |         $4,000 | **1** |

### Firewall A

$$
RRL = \frac{6000}{2000}=3
$$

Every $1 spent → $3 risk reduction.

### Firewall B

$$
RRL = \frac{10000}{5000}=2
$$

Every $1 spent → $2 risk reduction.

### Firewall C

$$
RRL = \frac{4000}{4000}=1
$$

Every $1 spent → $1 risk reduction.

So **A gives us the greatest risk reduction per dollar.**

---

# 6. The formula you should remember

$$
\boxed{
RRL =
\frac{Risk\ Exposure_{before}-Risk\ Exposure_{after}}
{Cost\ of\ Safeguard}
}
$$

Or simply:

$$
\boxed{
RRL = \frac{Risk\ Reduction}{Safeguard\ Cost}
}
$$

---

## 🔥 The mental model

Remember what you just learned:

**Risk Exposure:**

> "How much expected loss am I facing?"

**Risk Reduction:**

> "How much of that expected loss did my security control remove?"

**Risk Reduction Leverage:**

> **"How much risk did I remove per dollar I spent?"**

```text
       BEFORE CONTROL
       Risk = $8,000
             │
             │ Security Control
             │ Cost = $2,000
             ▼
       AFTER CONTROL
       Risk = $2,000
             │
             ▼
       Risk reduced = $6,000

       RRL = $6,000 / $2,000
           = 3
```

So if your exam gives you **before risk, after risk, and safeguard cost**, don't panic.

Just:

$$
\boxed{
\text{Before Risk} - \text{After Risk}
}
$$

then divide by:

$$
\boxed{\text{Safeguard Cost}}
$$

That's **Risk Reduction Leverage**.
