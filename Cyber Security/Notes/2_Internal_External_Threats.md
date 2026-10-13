Bro, let's focus specifically on Internal Threats in Cyber Security. 🔐

# 1. What is an Internal Threat?

An internal threat is a potential security risk that originates from within an organization's environment, involving people, accounts, devices, or systems that have internal access or trust.

In simple words:

> An internal threat comes from someone or something that already has access to, or a trusted position within, an organization.

An internal threat may involve an employee, a system administrator, a contractor, or even an external attacker who has compromised an employee's account.

## 2. Real-world example

Imagine your university has a portal containing students' personal information, grades, and fee records.

[How Can You Improve Cybersecurity for Higher Ed?](https://images.openai.com/static-rsc-4/rm3hm0KqaRkKZHH-Oy8n5gSk9IHUJPiUo2sy73vwpTgpp0N6sQrPV1SohUqJ8TVHuoUQxlD23z7jISZg76SCNZ6YxslPvAhfwsnQuOqkE8qu-HViK6uJjCbzNGg9765dZEXM4D4mxQn03-iTuhDJwdk1fn8MEGWo-yWfihIwlHA?purpose=inline)

[apporto.com](https://www.apporto.com/cyber-security-how-higher-ed-aim-to-meet-the-rising-demand)

Scenario: A university employee has authorized access to student records.

1. The employee can legitimately access the database.
2. The employee downloads students' private information.
3. The employee sells that information to someone else.

This is a malicious insider threat.

Why? Because the person uses their internal access to compromise confidentiality.

Notice that the employee doesn't necessarily need to hack the system. They already have legitimate access.

# 3. Types of Internal Threats

There are three important categories to understand.

[Insider Threats and the False Sense of Security](https://images.openai.com/static-rsc-4/YlSi9omAhu5CE91S8bMkXQEJFnBRoB_p9KvY3LeQGbb8Mon_KsdtfvaGm5LG7qXtcy-SmD0O8CZ_yc5Hfa1jJMjJ3UL4NewmdTpy05X0wTUH3lqwnUaUbc4gwbu6F834DF4RjczXEwGSuVMfbWNEvyYoljMdl8DzZICzvYrcH2k?purpose=inline)

1\. Malicious insider

A person intentionally abuses their access to cause harm or gain an unauthorized benefit.

Examples:

- A system administrator steals customer records.
- An employee deliberately deletes important files.
- A developer secretly inserts a backdoor into company software.

[📅 Day 5: The Email I Sent to the Wrong Person (And Survived)](https://images.openai.com/static-rsc-4/DBzXxC3VQWFDLvknThiVJVmzyZ4c6lYts1s6uiLIn7xZo9p8vlB4KvgkfB7CPgFmA8hxn51Ybnvg1A8eKwJcawLqftgHE6UTdh06l4g3lXE3CEcP5MxH3FYglaAePWeuSDJdeOQ9iTBw4CteZXnyD7DQNvBCDu_bOvP3Es3t7y8?purpose=inline)

2\. Negligent or accidental insider

A trusted person unintentionally creates a security weakness or incident.

Examples:

- An employee clicks a phishing link.
- A developer accidentally exposes an API key on GitHub.
- An administrator misconfigures database permissions.

[Cuando el enemigo ya está dentro de la empresa: la amenaza cyber de los "insiders" y cómo contenerla - Yahoo Noticias](https://images.openai.com/static-rsc-4/RihZcHFrqOXkDWxVwZXg1-IyBVnr3PkOpN3Nei_PIOHna3aVBRKD_TSPqKZkRstNutPu_MOCuwGbtUV3V5uvt6FvnCe2EVDV2HABcOajMxykYE-sFFCs3KDAYvpdzD5H6aHEbZ-_Xc-bhnf_oN33sdn9fGWFbYdJiViWFm4i0-g?purpose=inline)

3\. Compromised insider account

An external attacker steals or takes control of an internal user's account and abuses its privileges.

Examples:

- An attacker steals an employee's password.
- The attacker logs into the company's VPN.
- The attacker uses the employee's permissions to access confidential files.

Important distinction: A compromised account is not necessarily a malicious insider. The actual attacker may be external, even though the attack uses trusted internal credentials.

# 4. Why are internal threats dangerous?

The key issue is trust and access.

An external attacker may first need to bypass a firewall, exploit a vulnerability, or steal credentials.

An insider may already possess:

- Valid login credentials.
- Access to confidential files.
- Database permissions.
- Knowledge of internal systems.
- Access to administrative tools.

This can make certain attacks easier to carry out or harder to detect.

# 5. How can organizations prevent internal threats?

| Countermeasure                    | Purpose                                                  |
| --------------------------------- | -------------------------------------------------------- |
| Least privilege                   | Give each user only the permissions they need.           |
| Role-Based Access Control (RBAC)  | Assign permissions according to job roles.               |
| Multi-Factor Authentication (MFA) | Require additional proof of identity.                    |
| Audit logs and monitoring         | Record and investigate suspicious activity.              |
| Data Loss Prevention (DLP)        | Detect or restrict unauthorized data transfers.          |
| Employee security awareness       | Reduce phishing and accidental mistakes.                 |
| Separation of duties              | Prevent one person from controlling every critical step. |
| Timely access revocation          | Remove access when someone changes roles or leaves.      |

For example, a university receptionist might need to view student registration details but should not automatically have permission to export the entire student database.

That's the principle of least privilege.

## 6. Quick knowledge check

An employee clicks a phishing link. An external attacker steals the employee's credentials and accesses the university database. Which statement is most accurate?

The employee is necessarily a malicious insider.

It is an external attack using a compromised internal account.

It is a natural threat.

It cannot be an internal security risk because the attacker is external.


Alright bro! 🔐 We've covered Internal Threats, so now let's understand their counterpart: External Threats.

# 1. What is an External Threat?

An external threat is a potential security danger originating outside an organization's trusted environment, where an outside actor or source attempts to compromise its systems, networks, applications, or data.

In simple words:

> An external threat comes from outside the organization and may attempt to gain unauthorized access, steal information, damage systems, or disrupt services.

For example, ABC University operates a student portal. A hacker sitting in another country attempts to break into that portal over the internet. This is a potential external threat.

[Firewall corporativo: a primeira linha de defesa da rede da sua empresa](https://images.openai.com/static-rsc-4/_7bfwuNevkI7tkfz8FRoCrwOU3XP3qsTVZP3t1XUYonCLrFNqTQ0-WeIlVGjkOSFBqIgOcKkKW6QcvWRy0Z59Q3FcgKf7fBKCdzK_TXzoiBNdHCbLXOhael3EjVlk_4RQJO3l8IUajfgcyjMNA0OmWRGoBqn7DIEHHuBxSPoIYg?purpose=inline)

[zsinformatica.com.br](https://www.zsinformatica.com.br/post/firewall-corporativo-a-primeira-linha-de-defesa-da-rede-da-sua-empresa)

# 2. Types of External Threats

## 1. Hackers and unauthorized attackers

Individuals or groups attempt to access systems without permission.

Examples:

- Exploiting vulnerable web applications.
- Attempting to access exposed databases.
- Guessing or stealing passwords.
- Exploiting unpatched server software.

University example: An attacker exploits a vulnerability in the student portal to access examination records.

## 2. Phishing and social engineering

Attackers manipulate people into revealing sensitive information or performing unsafe actions.

Examples:

- Fake university login pages.
- Fraudulent emails requesting passwords.
- Messages containing malicious links or attachments.
- Impersonating IT support staff.

University example: An attacker emails a finance employee a fake payroll login page to steal their credentials.

## 3. Malware attacks

An external attacker may attempt to deliver malicious software to a system.

Common examples include:

- Ransomware: Encrypts files and demands payment.
- Spyware: Secretly collects information.
- Trojan: Disguises malicious functionality as legitimate software.
- Worm: Spreads between systems, often automatically.

University example: An employee downloads a malicious attachment, allowing ransomware to infect university computers.

## 4. Denial-of-Service (DoS and DDoS)

Attackers attempt to make a service unavailable to legitimate users by overwhelming or disrupting it.

- DoS: An attack from a single source or system, conceptually.
- DDoS: An attack distributed across multiple systems.

University example: Attackers flood the examination portal with traffic during final exams, preventing students from checking their results.

## 5. Password and credential attacks

External attackers attempt to obtain or misuse login credentials.

Examples:

- Brute-force attacks.
- Password spraying.
- Credential stuffing.
- Using credentials stolen through phishing.

University example: An attacker uses passwords leaked from another website to try logging into university accounts.

## 6. Network attacks

Attackers target communications or network infrastructure.

Examples:

- Man-in-the-Middle (MITM) attacks.
- DNS spoofing.
- Network eavesdropping.
- Exploiting exposed network services.

University example: An attacker intercepts inadequately protected communications to obtain sensitive information.

## 7. Supply-chain attacks

An attacker compromises a trusted external supplier, software package, or service to reach the target organization.

University example: A university installs a compromised software update from a vendor, introducing malicious code into its network.

# 3. Internal Threats vs. External Threats

| Feature         | Internal threat                                              | External threat                                  |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------ |
| Origin          | Inside the trusted environment or through internal access    | Outside the organization's trusted environment   |
| Typical actors  | Employees, contractors, administrators, compromised insiders | External hackers, cybercriminals, hostile groups |
| Access          | May already have legitimate access                           | Often needs an entry point or stolen credentials |
| Example         | An administrator deliberately leaks payroll data             | An internet attacker exploits a vulnerable API   |
| Common defenses | Least privilege, audits, access reviews                      | Firewalls, patching, MFA, IDS/IPS                |

Important nuance: An external attacker can steal an employee's credentials and then operate through an internal account. The attacker remains external even though they are using trusted credentials.

# 4. How external attacks happen

Let's connect this to the concepts you learned earlier: vulnerability, attack vector, exploit, and payload.

External attacker

Outside the university

Attack vector

Phishing email or exposed web application

Exploit or credential abuse

Abuses a weakness or uses stolen credentials

Unauthorized access or payload execution

Depends on the attack

Impact

Data theft, altered records, or service disruption

This is a possible attack sequence, not a requirement for every attack. For example, a DDoS attack does not necessarily involve exploiting a software vulnerability or delivering a payload.

# 5. How can organizations defend against external threats?

- Firewalls: Control network traffic according to security rules.
- Multi-factor authentication (MFA): Add another layer of login protection.
- Patching: Fix known software vulnerabilities.
- IDS/IPS: Detect or block suspicious network activity.
- Encryption: Protect sensitive data during storage and transmission.
- Security awareness: Help employees recognize phishing and social engineering.
- Backups: Support recovery after ransomware or destructive attacks.
- Rate limiting: Restrict excessive requests to protect applications and APIs.

No single defense stops every threat. Organizations use multiple layers of protection.

## 6. Test yourself, bro

1\. An attacker from outside the university exploits a vulnerable student portal. What type of threat is this?

Internal threat

External threat

Natural threat

2\. A criminal steals a finance employee's password through a fake login page. What is the technique used to trick the employee?

Phishing

DDoS

Hardware failure

3\. A software vendor distributes a compromised update to a university. What is this called?

Insider negligence

Supply-chain attack

Natural disaster

Reset quiz

Next concept: We can study structured vs. unstructured threats, and targeted vs. opportunistic attacks—another useful way to classify external threats, depending on your course syllabus.