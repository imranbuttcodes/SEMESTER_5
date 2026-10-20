# 1. What is the Playfair Cipher?

The Playfair Cipher is a classical encryption technique that encrypts two letters at a time instead of encrypting one letter at a time like the Caesar Cipher.

It uses a 5 × 5 matrix of letters generated from a keyword.

- Plaintext → the original message.
- Ciphertext → the encrypted message.
- Key → the word used to generate the matrix.

Since the English alphabet has 26 letters but the matrix has only 25 cells, I and J are usually combined into one cell.

# 2. Step 1 — Generate the 5 × 5 matrix

Let's use the keyword `MONARCHY`.

Rule: Write the keyword first, remove duplicate letters, and then fill the remaining spaces with unused letters of the alphabet, excluding J.

KEYWORD: MONARCHY

## M

## O

## N

## A

## R

## C

## H

## Y

## B

## D

## E

## F

## G

## I

## K

## L

## P

## Q

## S

## T

## U

## V

## W

## X

## Z

Blue cells contain the unique letters of the keyword. The remaining cells contain the unused alphabet letters.

Notice that:

- `MONARCHY` contains 8 unique letters.
- We add the remaining letters of the alphabet.
- J is omitted, so I and J share a cell.

# 3. Step 2 — Prepare the plaintext

Suppose our message is:

`INSTRUMENTS`

Before encryption, we split the message into pairs of letters, called digraphs.

Rules for preparing the message:

1. If both letters in a pair are the same, insert `X` between them.
2. If one letter remains at the end, add `X`.
3. Otherwise, keep the letters together in pairs.

For our example:

`INSTRUMENTS` → `IN ST RU ME NT SX`

Why `SX` at the end? Because the message has an odd number of letters, so we add X.

# 4. Step 3 — Encryption rules

There are three important rules. Memorize these, bro!

[Simple ciphers: Polygraphic ciphers](https://images.openai.com/static-rsc-4/Om4w3fR2S2gsV7BzYTprNoprvLqmsknbZMh7liIb98iR2A18f5e6QW0e0Z0tq54ZLAJpIbVZU_dgImH_ij-KMvD0MImXjmhJ4GdhaT_1ovna3gqUadkTzO5kd4MYhdI6JlfGZO-k_qgPGpNlc9gCnno789JisnNQ_6yHqSQMSt4?purpose=inline)

Rule 1: Same row

Replace each letter with the letter immediately to its right. Wrap around to the beginning if necessary.

[Unit 1 | PDF](https://images.openai.com/static-rsc-4/WQ3Jf_SdDl4hCcMzYUkrU5EHeh55lqvtcMcs-1gkaH93yFq3V1wy4ZtlOW-wsxb0D70d7WEbdyh-7Ka3Ivsnab_JI41CBr-3fOo3J1qIhBU_AA8I8S5KNLoSt6qJOjs6mLBPly4stcgIUAt6TaxjXeHxy5myzRCz-1q2B7m1JAI?purpose=inline)

Rule 2: Same column

Replace each letter with the letter immediately below it. Wrap around to the top if necessary.

[Cracking Playfair Ciphers](https://images.openai.com/static-rsc-4/7eAUg_KKKo8P_5B5eb4VBnUl6m7F9gSkiN1xl58QdSxFxsOjiQeCrQbdnzVG_XL_fg76gZEM0tR8HRMR38E5dTlHZLDwvIVFBeblR2BXIJajWMaiGDs35cgXeUlsoTjLz9rdft-cPwVgZ1UvNf0-fbcKHdiW3-m7rzb0ikx52dc?purpose=inline)

Rule 3: Rectangle

If the letters are in different rows and columns, form a rectangle. Replace each letter with the letter in the same row but the other letter's column.

## 5. Step 4 — Encrypt our example

Key: `MONARCHY`

Plaintext pairs: `IN ST RU ME NT SX`

Let's encrypt the first pair: `IN`.

- I is at row 4, column 4.
- N is at row 1, column 3.
- They form a rectangle.
- I becomes G (row 4, column 3).
- N becomes K (row 1, column 4).

Therefore, `IN → GK`.

Let's see the complete encryption.

| Pair | Rule        | Ciphertext |
| ---- | ----------- | ---------- |
| IN   | Rectangle   | GK         |
| ST   | Same column | TL         |
| RU   | Rectangle   | MZ         |
| ME   | Rectangle   | CL         |
| NT   | Rectangle   | RQ         |
| SX   | Rectangle   | QV         |

So the final ciphertext is:

`GK TLMZCLRQQV`

Correction to keep the pairs clear: concatenating the encrypted pairs gives `GK TLMZCLRQQV`, with the pairs `GK TL MZ CL RQ QV`.

# 6. How decryption works

Decryption reverses the rules:

| Situation   | Encryption   | Decryption   |
| ----------- | ------------ | ------------ |
| Same row    | Move right   | Move left    |
| Same column | Move down    | Move up      |
| Rectangle   | Swap columns | Swap columns |

For example, decrypt `GK`:

- G and K form a rectangle.
- Swap their columns while keeping their rows unchanged.
- G becomes I, and K becomes N.

Therefore, `GK → IN`.

Important: Decryption usually restores the prepared plaintext, including any filler X characters. You may need to remove filler X characters manually to recover the original message.

# 7. Your turn, bro! 💪

Let's test your understanding.

Using the `MONARCHY` matrix, encrypt the pair `MO`.

Where are M and O in the matrix?

Same row

Same column

Rectangle

Check answer

Once you understand these three rules, you can encrypt and decrypt any Playfair Cipher message using a keyword.