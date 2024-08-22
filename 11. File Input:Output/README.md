# Python Input and Output

## Fancier Output Formatting

Python provides several ways to format output for better readability and presentation. Here are the key methods:

### Formatted String Literals (f-strings)

Formatted string literals, introduced in Python 3.6, allow you to embed expressions directly within strings, prefixed with `f` or `F`. This makes it easy to insert variables and perform basic formatting.

```python
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')  # Output: Results of the 2016 Referendum
```

### `str.format()` Method

The `str.format()` method provides more manual control over formatting. You use `{}` placeholders to mark where values should be inserted, and then pass the values as arguments.

```python
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))  # Output:  42572654 YES votes  49.67%
```

### Manual String Formatting

You can also manually format strings using string slicing, concatenation, and methods like `str.rjust()`, `str.ljust()`, and `str.zfill()`.

```python
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
```

## Reading and Writing Files

Python's built-in `open()` function is used to open files. It returns a file object that can be used to read from or write to the file.

```python
# Open a file for writing
f = open('workfile', 'w', encoding="utf-8")

# Write to the file
f.write('This is a test\n')

# Close the file
f.close()
```

It's recommended to use the `with` statement when working with files, as it ensures the file is properly closed even if an exception occurs.

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
```

### File Object Methods

Some common file object methods include:

- `f.read(size)`: Reads and returns up to `size` characters (or bytes in binary mode).
- `f.readline()`: Reads and returns one line from the file.
- `f.readlines()`: Reads and returns all lines from the file as a list.
- `f.write(string)`: Writes the contents of `string` to the file, returning the number of characters written.
- `f.tell()`: Returns the file object's current position.
- `f.seek(offset, whence)`: Changes the file object's position.

### Saving Structured Data with `json`

Python's built-in `json` module provides a convenient way to serialize and deserialize complex data structures like lists and dictionaries to and from a text-based format.

```python
import json

data = [1, 'simple', 'list']
json_string = json.dumps(data)  # Serialize to JSON
new_data = json.loads(json_string)  # Deserialize from JSON
```

The `json.dump()` and `json.load()` functions can be used to write and read JSON data directly to/from files.


## Reading and Writing Files

Python's built-in `open()` function is used to open files. It returns a file object that can be used to read from or write to the file.

The `open()` function takes three arguments:
1. `filename`: A string representing the file path.
2. `mode`: A string specifying the mode in which to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
3. `encoding` (optional): The text encoding to use when opening the file in text mode.

```python
# Open a file for writing
f = open('workfile', 'w', encoding="utf-8")

# Write to the file
f.write('This is a test\n')

# Close the file
f.close()
```

It's recommended to use the `with` statement when working with files, as it ensures the file is properly closed even if an exception occurs.

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
```

The `with` statement automatically calls `f.close()` when the block of code inside the `with` statement is finished executing.

### File Modes

The `mode` argument to `open()` specifies how the file will be used:

- `'r'`: Read mode (the default)
- `'w'`: Write mode (overwrites the file if it already exists)
- `'a'`: Append mode (adds to the end of the file if it already exists)
- `'x'`: Exclusive creation mode (fails if the file already exists)
- `'b'`: Binary mode (for non-text files)
- `'t'`: Text mode (the default)
- `'+'`: Open the file for updating (reading and writing)

For example, `'rb'` opens the file in binary read mode, and `'w+'` opens the file in text read/write mode.

### File Object Methods

Some common file object methods include:

- `f.read(size)`: Reads and returns up to `size` characters (or bytes in binary mode).
- `f.readline()`: Reads and returns one line from the file.
- `f.readlines()`: Reads and returns all lines from the file as a list.
- `f.write(string)`: Writes the contents of `string` to the file, returning the number of characters written.
- `f.writelines(sequence)`: Writes a sequence of strings to the file.
- `f.tell()`: Returns the file object's current position.
- `f.seek(offset, whence)`: Changes the file object's position.
  - `whence=0` (default): Seek from the beginning of the file.
  - `whence=1`: Seek from the current position.
  - `whence=2`: Seek from the end of the file.

When you're done with a file, it's important to call `f.close()` to release the system resources used by the file. This is particularly important when working with large files or in long-running programs.