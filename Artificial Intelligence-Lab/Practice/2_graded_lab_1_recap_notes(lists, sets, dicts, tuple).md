# 1. Lists — `list`

A list is ordered, mutable, and allows duplicates.

```
nums = [10, 20, 30, 20]
```

## Main list methods

| Method             | Example                 | What it does                                    |
| ------------------ | ----------------------- | ----------------------------------------------- |
| `append(x)`        | `nums.append(40)`       | Adds one element at the end                     |
| `extend(iterable)` | `nums.extend([40, 50])` | Adds multiple elements                          |
| `insert(i, x)`     | `nums.insert(1, 15)`    | Inserts at a specified index                    |
| `remove(x)`        | `nums.remove(20)`       | Removes the first matching value                |
| `pop([i])`         | `nums.pop()`            | Removes and returns the last element by default |
| `clear()`          | `nums.clear()`          | Removes all elements                            |
| `index(x)`         | `nums.index(30)`        | Returns the first matching index                |
| `count(x)`         | `nums.count(20)`        | Counts occurrences                              |
| `sort()`           | `nums.sort()`           | Sorts the list in place                         |
| `reverse()`        | `nums.reverse()`        | Reverses the list in place                      |
| `copy()`           | `other = nums.copy()`   | Creates a shallow copy                          |

## Examples you should know

```
nums = [10, 20, 30]nums.append(40)print(nums)          # [10, 20, 30, 40]nums.extend([50, 60])print(nums)          # [10, 20, 30, 40, 50, 60]nums.insert(1, 15)print(nums)          # [10, 15, 20, 30, 40, 50, 60]
```

Removing elements:

```
nums = [10, 20, 30, 20]nums.remove(20)print(nums)          # [10, 30, 20]x = nums.pop()print(x)             # 20print(nums)          # [10, 30]
```

Searching and counting:

```
nums = [10, 20, 30, 20]print(nums.index(20))  # 1print(nums.count(20))  # 2
```

Sorting and reversing:

```
nums = [30, 10, 20]nums.sort()print(nums)          # [10, 20, 30]nums.reverse()print(nums)          # [30, 20, 10]
```

Important: `sort()` changes the original list and returns `None`. To create a new sorted list, use `sorted(nums)`.

# 2. Tuples — `tuple`

A tuple is ordered and immutable. You cannot add, remove, or replace its elements after creation.

```
t = (10, 20, 10, 30)
```

Tuples have only two built-in methods for working with their elements.

| Method     | Example       | What it does                     |
| ---------- | ------------- | -------------------------------- |
| `count(x)` | `t.count(10)` | Counts occurrences               |
| `index(x)` | `t.index(20)` | Returns the first matching index |

Examples:

```
t = (10, 20, 10, 30)print(t.count(10))  # 2print(t.index(20))  # 1
```

## Other useful tuple operations

These aren't tuple methods, but you'll use them frequently.

```
t = (10, 20, 30, 40)print(len(t))       # 4print(t[0])         # 10print(t[-1])        # 40print(t[1:3])       # (20, 30)print(20 in t)      # True
```

Tuple unpacking:

```
student = ("Imran", 20, "CS")name, age, department = studentprint(name)         # Imranprint(age)          # 20print(department)   # CS
```

Remember: tuples are immutable, but if a tuple contains a mutable object such as a list, that inner list can still be modified.

# 3. Sets — `set`

A set is a mutable collection of unique elements. It doesn't support indexing and doesn't guarantee positional order.

```
s = {10, 20, 30, 20}print(s)  # {10, 20, 30} (display order may vary)
```

## A. Main set methods

| Method             | Example              | What it does                             |
| ------------------ | -------------------- | ---------------------------------------- |
| `add(x)`           | `s.add(40)`          | Adds one element                         |
| `update(iterable)` | `s.update([40, 50])` | Adds multiple elements                   |
| `remove(x)`        | `s.remove(20)`       | Removes an element; errors if missing    |
| `discard(x)`       | `s.discard(99)`      | Removes an element; no error if missing  |
| `pop()`            | `s.pop()`            | Removes and returns an arbitrary element |
| `clear()`          | `s.clear()`          | Removes all elements                     |
| `copy()`           | `other = s.copy()`   | Creates a shallow copy                   |

Examples:

```
s = {10, 20, 30}s.add(40)print(s)                 # {10, 20, 30, 40}s.update([50, 60])print(s)                 # Contains 10, 20, 30, 40, 50, 60s.remove(20)s.discard(99)            # No errorprint(s)
```

## B. Set operation methods

These are especially important for mathematical and coding interview problems.

Let:

```
A = {1, 2, 3, 4}B = {3, 4, 5, 6}
```

| Method                          | Example                            | Result                                  |
| ------------------------------- | ---------------------------------- | --------------------------------------- |
| `union()`                       | `A.union(B)`                       | `{1, 2, 3, 4, 5, 6}`                    |
| `intersection()`                | `A.intersection(B)`                | `{3, 4}`                                |
| `difference()`                  | `A.difference(B)`                  | `{1, 2}`                                |
| `symmetric_difference()`        | `A.symmetric_difference(B)`        | `{1, 2, 5, 6}`                          |
| `intersection_update()`         | `A.intersection_update(B)`         | Keeps only common elements in `A`       |
| `difference_update()`           | `A.difference_update(B)`           | Removes elements of `B` from `A`        |
| `symmetric_difference_update()` | `A.symmetric_difference_update(B)` | Keeps elements found in exactly one set |
| `update()`                      | `A.update(B)`                      | Adds elements from `B` to `A`           |

The first four return a result without changing the original set. The `*_update()` methods modify the original set.

Example:

```
A = {1, 2, 3, 4}B = {3, 4, 5, 6}print(A.union(B))                 # {1, 2, 3, 4, 5, 6}print(A.intersection(B))          # {3, 4}print(A.difference(B))            # {1, 2}print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```

You can also use operators:

```
print(A | B)   # Unionprint(A & B)   # Intersectionprint(A - B)   # Differenceprint(A ^ B)   # Symmetric difference
```

## C. Set relationship methods

| Method         | Example                     | Meaning                              |
| -------------- | --------------------------- | ------------------------------------ |
| `issubset()`   | `{1, 2}.issubset(A)`        | Are all elements contained in `A`?   |
| `issuperset()` | `A.issuperset({1, 2})`      | Does `A` contain every element?      |
| `isdisjoint()` | `{1, 2}.isdisjoint({5, 6})` | Do the sets have no common elements? |

Example:

```
A = {1, 2, 3, 4}print({1, 2}.issubset(A))      # Trueprint(A.issuperset({1, 2}))    # Trueprint(A.isdisjoint({5, 6}))    # True
```

Useful extra: `in` checks membership, and `len()` counts elements.

```
print(3 in A)     # Trueprint(len(A))     # 4
```

# 4. Dictionaries — `dict`

A dictionary stores data as key-value pairs. It is mutable, preserves insertion order, and requires unique, hashable keys.

```
student = {    "name": "Imran",    "age": 20,    "department": "CS"}
```

## A. Main dictionary methods

| Method         | Example                            | What it does                                                 |
| -------------- | ---------------------------------- | ------------------------------------------------------------ |
| `get(key)`     | `student.get("age")`               | Returns the value, or `None` if missing                      |
| `keys()`       | `student.keys()`                   | Returns a view of all keys                                   |
| `values()`     | `student.values()`                 | Returns a view of all values                                 |
| `items()`      | `student.items()`                  | Returns a view of key-value pairs                            |
| `update()`     | `student.update({"age": 21})`      | Adds or updates entries                                      |
| `pop(key)`     | `student.pop("age")`               | Removes a key and returns its value                          |
| `popitem()`    | `student.popitem()`                | Removes and returns the last inserted pair                   |
| `setdefault()` | `student.setdefault("grade", "A")` | Returns the value; inserts the default if the key is missing |
| `copy()`       | `other = student.copy()`           | Creates a shallow copy                                       |
| `clear()`      | `student.clear()`                  | Removes all entries                                          |
| `fromkeys()`   | `dict.fromkeys(["a", "b"], 0)`     | Creates a dictionary from keys with a shared initial value   |

## B. Examples of the important methods

### 1. `get()` — safely access values

```
student = {"name": "Imran", "age": 20}print(student.get("name"))       # Imranprint(student.get("grade"))      # Noneprint(student.get("grade", "N/A"))  # N/A
```

Unlike `student["grade"]`, `get()` doesn't raise a `KeyError` when the key is missing.

### 2. `keys()`, `values()`, and `items()`

```
student = {"name": "Imran", "age": 20}print(list(student.keys()))# ['name', 'age']print(list(student.values()))# ['Imran', 20]print(list(student.items()))# [('name', 'Imran'), ('age', 20)]
```

These methods return dictionary views, not lists. Here, `list()` converts each view into a list.

### 3. `update()` — add or modify entries

```
student = {"name": "Imran", "age": 20}student.update({"age": 21, "grade": "A"})print(student)# {'name': 'Imran', 'age': 21, 'grade': 'A'}
```

### 4. `pop()` and `popitem()`

```
student = {"name": "Imran", "age": 20}age = student.pop("age")print(age)       # 20print(student)   # {'name': 'Imran'}item = student.popitem()print(item)      # ('name', 'Imran')
```

`pop(key)` removes a specific entry. `popitem()` removes the last inserted entry.

### 5. `setdefault()` — insert only if missing

```
student = {"name": "Imran"}student.setdefault("age", 20)student.setdefault("name", "Ali")print(student)# {'name': 'Imran', 'age': 20}
```

The existing `"name"` value remains `"Imran"`. The missing `"age"` key is inserted with value `20`.

### 6. `copy()` and `clear()`

```
student = {"name": "Imran", "age": 20}other = student.copy()other["age"] = 21print(student["age"])  # 20print(other["age"])    # 21student.clear()print(student)         # {}
```

`copy()` creates a shallow copy, while `clear()` empties the dictionary.

### 7. `fromkeys()`

```
keys = ["math", "physics", "cs"]marks = dict.fromkeys(keys, 0)print(marks)# {'math': 0, 'physics': 0, 'cs': 0}
```

It initializes every specified key with the same value.

## C. Other essential dictionary operations

```
student = {"name": "Imran", "age": 20}# Add a new entrystudent["grade"] = "A"# Update an entrystudent["age"] = 21# Check if a key existsprint("name" in student)     # True# Number of entriesprint(len(student))          # 3# Delete an entrydel student["grade"]# Loop through key-value pairsfor key, value in student.items():    print(key, value)
```

# 5. Master comparison table

Here's the quick revision table, bro.

| Operation    | List                | Tuple                               | Set                              | Dictionary                                   |
| ------------ | ------------------- | ----------------------------------- | -------------------------------- | -------------------------------------------- |
| Add          | `append()`          | Not supported                       | `add()`                          | `d[key] = value`                             |
| Add multiple | `extend()`          | Not supported                       | `update()`                       | `update()`                                   |
| Remove       | `remove()`, `pop()` | Not supported                       | `remove()`, `discard()`, `pop()` | `pop()`, `popitem()`                         |
| Clear        | `clear()`           | Not supported                       | `clear()`                        | `clear()`                                    |
| Search       | `index()`           | `index()`                           | `in`                             | `in` checks keys                             |
| Count        | `count()`           | `count()`                           | No `count()` method              | No `count()` method                          |
| Sort         | `sort()`            | `sorted()` returns a list           | `sorted()` returns a list        | `sorted()` returns a list of keys by default |
| Copy         | `copy()`            | `tuple(t)` may reuse the same tuple | `copy()`                         | `copy()`                                     |
| Length       | `len()`             | `len()`                             | `len()`                          | `len()`                                      |

One crucial distinction: methods belong to particular data types. For example, `append()` belongs to lists, not tuples or sets.

## 6. Quick revision challenge

Question 1 of 5

0/5 answered

## Which list method adds multiple elements?

append()

extend()

insert()

add()

PreviousCheck answer

