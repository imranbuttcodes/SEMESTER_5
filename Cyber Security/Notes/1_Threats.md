# 1. What is a Security Threat?

A security threat is a potential cause of an unwanted security incident that could harm a system, compromise data, or disrupt a service.

In simple words:

> A threat is something that could cause damage to your system or compromise its security.

For example, imagine you have a university portal that stores students' names, grades, passwords, and fee records.

Potential threats include:

- An attacker stealing student passwords.
- Malware infecting the university server.
- A fire destroying the server room.
- A power outage interrupting the portal.
- An employee accidentally deleting student records.

Notice something important: a threat doesn't have to be a hacker or even a human. Natural disasters, technical failures, and accidental mistakes can also pose threats.

## 2. Threat vs. Vulnerability vs. Attack vs. Risk

Before learning the types, let's distinguish these terms.

Threat — Potential danger

Someone might steal your database.

Vulnerability — Weakness

Your database is publicly accessible without authentication.

Attack — Action

An attacker accesses and downloads the database.

Risk — Possibility of loss

The organization faces a chance of data exposure, financial loss, or legal consequences.

A threat can exist even when a vulnerability has not been identified. Likewise, an attack doesn't always require exploiting a software vulnerability—for example, an attacker could trick an employee into revealing a password.

# 3. Types of Security Threats

There are several ways to classify threats. Different textbooks and syllabi use different taxonomies, so we'll cover the major classifications you are likely to encounter.

## Type 1: Natural threats

[Power Distribution Station with Lightning Strike.](https://images.openai.com/static-rsc-4/43kuJkqE818xFYJOoT8mZd0llxjQ6gsrpNPMnIsQct3I4Ub6Bfv151UjmOMr_rWn8UssKVVwCL38sNcmg7Z4DhLVv5lYC2QyXf1ELke-hTzt0eZaya6klkYWDIKjeQ-qGLHSyI9OzlqBZm7SsoAphpXUCccQjDg4o0hrqh21NGKisA1yQCtL58MUmB-FeP2S?purpose=inline)

[Why Backup and Disaster Recovery Are Not the Same Thing](https://images.openai.com/static-rsc-4/hHuSjZCuA4DxtMO39j5x7vsKt5fUEtO6SDfBJuOM-jHcFgFOgFs2Y0nGNXEPosjcqfFeIkvpaINaf8ANYr7vGG7YWRaBkET59JNf_Z-pZrrTTig9hT8siZrtNv6plxfsINGItMlbipjG2rgK21bOjA94vK_4c0tM4N3Gd1ib3RE?purpose=inline)

[IBC: Only 8% of Quebec residents believe their home is at risk due to earthquakes | Insurance Business](https://images.openai.com/static-rsc-4/xfRA5s_icMM8QYhbPH2N3-cD03-ZxZLd8huA62yXiIXYSZbzExcMeHzO05MSmb6TVGHmkjjtRYexVSwV_3MiNNK30q2lAUl9kKjrW0y639evk4EAPTF5bvOmiZgTvseqIJUHGSCzbvWjdbCz_MsW0xva9iOGvnqbqPzqzSNNoo8?purpose=inline)

These originate from natural events beyond an organization's direct control.

Examples:

- Earthquakes
- Floods
- Lightning strikes
- Hurricanes and severe storms
- Extreme temperatures

Cybersecurity example: A flood damages a data center, making the university portal unavailable.

Security property affected: Availability.

## Type 2: Human threats

These originate from human actions. They can be intentional or accidental.

### A. Intentional threats

Someone deliberately attempts to compromise security.

Examples:

- Hacking
- Phishing
- Ransomware attacks
- Insider sabotage
- Denial-of-Service (DoS) attacks
- Theft of confidential information

Example: An attacker deliberately exploits a vulnerable API to access private student records.

### B. Accidental threats

Someone unintentionally causes a security incident.

Examples:

- Deleting important files by mistake
- Sending confidential information to the wrong recipient
- Misconfiguring a firewall
- Publishing an API key in a public GitHub repository
- Accidentally granting excessive database permissions

Example: A developer commits a production database password to a public repository.

Nobody needs to attack the application directly; the accidental exposure itself creates a security problem.

## Type 3: Technical threats

These arise from failures or weaknesses in hardware, software, networks, or other technical components.

Examples:

- Hardware failure
- Software bugs
- Operating system vulnerabilities
- Network equipment failure
- Power supply failure
- Incorrect system configurations

Example: An SSD fails, and the university loses data because it has no usable backup.

One subtle point: a technical failure is not always a cyberattack, but it can still threaten information security.

## Type 4: Cyber threats

These are threats directed at computers, networks, applications, or digital information.

Common examples include:

[Phishing envelope cybersecurity](https://images.openai.com/static-rsc-4/BnS8upx0p8iBhyPuxMrdw14CduzALqlB6JT_Jv7mgh-E69zNDeUVYZzUWnXEPDbSxfX8vcQ6aEjMwriBU9EpIKWSSwRgnaYXqMleeIcklpUR9vXtbPR3Sc-RifRYlm66lVbGc4B55z18xzc2bE5-Ei5fENjOVC9FBJIEWgGB-Js?purpose=inline)

1\. Phishing

Deceiving users into revealing credentials or other sensitive information.

[Malicious Code Trend: AI-Driven Ransomware Escalates - AI CERTs News](https://images.openai.com/static-rsc-4/XzrbZKqgKDwuAekKrYvBC6j7frAb9VX8pWdnpGoU2_kKIHPUV4jGskabqj_FuSub5BxrEMVldzQdQdF9xd3ECjuSMIe9HOtM1WAnEn7k2ULGAan_US0y4pOsTaWHcdDf7u1T9U7VDFV5WaLQBFmKoTo084wPkqfZ5TzegqzJ48s?purpose=inline)

2\. Malware

Malicious software, including ransomware, spyware, and trojans.

[DDoS Attack Trends for Q4 2021](https://images.openai.com/static-rsc-4/yqkm_lcR9mk2LHiSAuk0XU04c2WYgPjDnZxgPhzeQAGeQxogH-7P4LRC80CqDPO8DaFbxkViU0jkz8eKPDWrPczy5-MegPdVpzSrHzLIWDaW9qX_VkQLNMe6Ahnqf8OXamyR2EpbBfX8CYzxyenMq4EGNndZaKusgZibUzREL3Q?purpose=inline)

3\. Denial of Service (DoS)

Overwhelming or disrupting a service so legitimate users cannot access it.

[Man-in-the-middle attack: Definition and types](https://images.openai.com/static-rsc-4/4c0-3MxOAa84qBi7Se9lSd05wD8YGcrzUPCFH_gUm0nDUnldoH8ERldUlyYfpnPxsIMD146w-ABnSUZpg16rc9XeLk7MenUFO0wH0P8qgMeGhpa2qWcjTvAaAP1iokv6UtNjHOMpO-vHMW1s1ulQFeIdMgx99dzBTr2oSl6yLRY?purpose=inline)

4\. Man-in-the-Middle (MITM)

Intercepting communications between parties, potentially reading or altering them.

[Medium](https://images.openai.com/static-rsc-4/8Gq4GPSYXCrElqH9oQeSn2XHXOP6Z3fttI9juFs4tmih96R09jj0f-bYlXstaFsNCVYfhJjcJrAHrNL39rDjL-XqxR4sRkzVJUvUZd91KE14mBb8EBTnzQs8ydWb6uzRjz_aG1WENWtlnrMm19rIHo4HXc0kVct-P7UnqkbBPvk?purpose=inline)

5\. Injection attacks

Supplying crafted input that causes an application to interpret unintended commands or queries.

These cyber threats can overlap with the human and technical categories. For example, phishing is a cyber threat involving intentional human action, while malware can exploit a technical vulnerability.

# 4. Another important classification: Passive vs. Active threats

This connects directly to the passive and active attacks we discussed earlier.

| Passive threats                                                | Active threats                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Involve unauthorized observation or collection of information. | Involve attempts to alter, disrupt, inject, or destroy information or services. |
| Often target confidentiality.                                  | Often target integrity, authenticity, or availability.                          |
| Examples: eavesdropping, traffic analysis.                     | Examples: message modification, replay, impersonation, DoS.                     |

Remember: passive and active are primarily classifications of attacks in traditional security models. Textbooks may also describe the associated threats as passive or active.

# 5. Threats classified by their source

Another common classification distinguishes who or what is responsible.

- External threats: Originate outside the organization, such as an internet-based attacker.
- Internal threats: Originate from people or compromised systems inside the organization, such as a malicious employee or an employee whose account has been compromised.
- Third-party threats: Originate through vendors, service providers, software suppliers, or other external partners.

For example, if a university's software vendor is compromised and attackers use a malicious software update to reach the university, that is a supply-chain threat.

# 6. Test your understanding

Let's check whether you can classify threats rather than merely memorize definitions.

1\. A lightning strike destroys a university's network equipment. Which category best describes the threat?

Natural

Intentional human

Passive cyber

2\. A developer accidentally publishes a secret API key on GitHub. Which category best describes the cause?

Natural threat

Accidental human threat

Passive attack

3\. An attacker secretly monitors unencrypted network traffic without modifying it. Which attack classification applies?

Active

Passive

Natural

4\. A malicious employee deliberately deletes the university's database. Which category best fits?

Accidental technical threat

Intentional human threat

Natural threat

Reset quiz

What comes next? We can study the relationship between threats, vulnerabilities, likelihood, impact, and risk exposure in depth, including how to calculate risk and choose countermeasures.