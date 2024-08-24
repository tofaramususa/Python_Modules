## **README.md**

### **Regular Expressions in Python: Mastering the `re` Library**

#### **Introduction**

Regular expressions, often referred to as regex, are powerful tools for pattern matching and text manipulation. Python's `re` module provides a comprehensive interface for working with regular expressions, offering a wide range of functions and features.

#### **Basic Concepts**

- **Regular Expression Syntax:** Regular expressions use a combination of ordinary characters and special metacharacters to define patterns.
- **Matching:** A regular expression matches a string if the string conforms to the specified pattern.
- **Metacharacters:** Special characters that have specific meanings in regular expressions, such as:

  - `.` (any character)
  - `^` (start of string)
  - `$` (end of string)
  - `*` (zero or more occurrences)
  - `+` (one or more occurrences)
  - `?` (zero or one occurrence)
  - `[]` (character set)
  - `|` (alternation)
  - `()` (grouping)
  - `\` (escape character)

#### **Key Functions and Methods**

- **`re.compile()`:** Creates a compiled regular expression object for efficient reuse.
- **`re.search()`:** Searches for a pattern within a string and returns a match object if found.
- **`re.match()`:** Matches a pattern only at the beginning of a string.
- **`re.findall()`:** Returns a list of all non-overlapping matches of a pattern in a string.
- **`re.sub()`:** Replaces occurrences of a pattern with a replacement string.
- **`re.split()`:** Splits a string into a list of substrings based on a pattern.

#### **Examples**

**Basic matching:**

```python
import re

pattern = r"hello"
text = "Hello, world!"
match = re.search(pattern, text)

if match:
    print("Match found!")
```

**Using metacharacters:**

```python
pattern = r"\d{3}-\d{3}-\d{4}"  # Matches a phone number
phone_number = "123-456-7890"

if re.match(pattern, phone_number):
    print("Valid phone number")
```

**Character sets:**

```python
pattern = r"[a-zA-Z0-9_]+"  # Matches a word consisting of letters, numbers, and underscores
word = "hello_world123"

if re.match(pattern, word):
    print("Valid word")
```

**Grouping and capturing:**

```python
pattern = r"(Hello|Goodbye), (world|everyone)"
text = "Hello, world!"

match = re.search(pattern, text)
if match:
    print("Greeting:", match.group(1))
    print("Target:", match.group(2))
```

**Substitution:**

```python
new_text = re.sub(r"world", "universe", text)
print(new_text)
```

#### **Advanced Topics**

- **Flags:** Modify the behavior of regular expressions, such as:
  - `re.IGNORECASE` for case-insensitive matching
  - `re.DOTALL` for dot matching newline characters
- **Lookarounds:** Assertions that match positions within a string without consuming characters:
  - `(?=...)` (positive lookahead)
  - `(?!...)` (negative lookahead)
- **Greedy and Non-Greedy Quantifiers:** Control the behavior of quantifiers, such as `*` and `+`, to match the longest or shortest possible substring.
- **Backreferences:** Refer to captured groups within a regular expression.

By mastering regular expressions and the `re` library, you can efficiently perform tasks like data validation, text extraction, and pattern recognition in your Python applications.
