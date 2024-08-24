# Databases with ORM in Python

## Overview
This guide covers the essential concepts and advanced features of using Object-Relational Mapping (ORM) in Python. We'll explore how Python objects can be mapped to database tables, how to perform CRUD operations, and how to work with fields and models using Peewee, a lightweight ORM for Python.

## Table of Contents
- [Introduction to ORM](#introduction-to-orm)
  - [What is ORM?](#what-is-orm)
  - [Installing Peewee](#installing-peewee)
- [Modeling Your Data](#modeling-your-data)
  - [Defining Models](#defining-models)
  - [Working with Fields](#working-with-fields)
- [CRUD Operations](#crud-operations)
  - [Create](#create)
  - [Read](#read)
  - [Update](#update)
  - [Delete](#delete)
- [Advanced ORM Features](#advanced-orm-features)
  - [Querying with Filters](#querying-with-filters)
  - [Handling Relationships](#handling-relationships)
- [Built-in Python Containers](#built-in-python-containers)
- [Docstrings and Documentation](#docstrings-and-documentation)

## Introduction to ORM

### What is ORM?
Object-Relational Mapping (ORM) is a technique that allows you to interact with your database using Python objects instead of writing raw SQL queries. In ORM, database tables are represented as Python classes, and rows in these tables are represented as instances of these classes.

### Installing Peewee
Peewee is a small, expressive ORM that simplifies database interactions in Python. It supports SQLite, MySQL, and PostgreSQL.

To install Peewee, use pip:

```bash
pip install peewee
```

If you are working with SQLite, you can use the built-in SQLite library in Python. For MySQL or PostgreSQL, you might need additional drivers.

## Modeling Your Data

### Defining Models
In ORM, a **Model** represents a table in your database. Each model is defined as a Python class, and each attribute in the class corresponds to a column in the table.

```python
from peewee import *

db = SqliteDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField()
    created_at = DateTimeField()

# Create the tables in the database
db.connect()
db.create_tables([User])
```

In this example:
- `User` is a model that corresponds to a `User` table in the database.
- `username`, `email`, and `created_at` are fields that represent columns in the `User` table.
- The `save()` method on an instance of `User` adds a new row to the database.

### Working with Fields
Fields define the types of data that can be stored in each column of the table. Peewee provides several field types, including:

- `CharField()` for short text.
- `TextField()` for larger text.
- `DateTimeField()` for storing dates and times.
- `IntegerField()` for integers.

```python
class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = FloatField()
    created_at = DateTimeField()

# Save a new product to the database
product = Product(name='Laptop', description='A powerful laptop', price=1299.99)
product.save()
```

## CRUD Operations

### Create
To add a new record to the database, create an instance of the model and call the `save()` method.

```python
new_user = User(username='john_doe', email='john@example.com')
new_user.save()
```

### Read
To retrieve data from the database, use the `select()` method on your model.

```python
all_users = User.select()
for user in all_users:
    print(user.username, user.email)
```

You can also filter your query results:

```python
user = User.get(User.username == 'john_doe')
print(user.email)
```

### Update
To update an existing record, modify the attributes of the model instance and call `save()`.

```python
user = User.get(User.username == 'john_doe')
user.email = 'new_email@example.com'
user.save()
```

### Delete
To delete a record from the database, use the `delete_instance()` method.

```python
user = User.get(User.username == 'john_doe')
user.delete_instance()
```

## Advanced ORM Features

### Querying with Filters
Peewee allows you to build complex queries with filters to retrieve specific data.

```python
recent_users = User.select().where(User.created_at > '2024-01-01')
for user in recent_users:
    print(user.username)
```

### Handling Relationships
ORMs allow you to define relationships between tables, such as `ForeignKeyField` for one-to-many relationships.

```python
class BlogPost(BaseModel):
    title = CharField()
    content = TextField()
    user = ForeignKeyField(User, backref='posts')
    created_at = DateTimeField()

# Create a blog post associated with a user
user = User.get(User.username == 'john_doe')
post = BlogPost(title='My First Post', content='This is the content', user=user)
post.save()
```

## Built-in Python Containers
Python provides four built-in containers that are often used when working with databases and ORMs:
- **`dict`**: Stores key-value pairs, useful for mapping field names to values.
- **`list`**: An ordered collection, useful for handling multiple rows of data.
- **`set`**: An unordered collection of unique elements, useful for filtering duplicates.
- **`tuple`**: An immutable, ordered collection, useful for fixed data sets.

## Docstrings and Documentation
In Python, the `None` keyword represents the absence of a value. It's also important to document your code using docstrings to make it easier to understand and maintain.

```python
def create_user(username: str, email: str) -> None:
    """
    Create a new user and save it to the database.

    Args:
        username (str): The username of the new user.
        email (str): The email of the new user.

    Returns:
        None
    """
    user = User(username=username, email=email)
    user.save()
```

Docstrings provide an explanation of the function's purpose, its arguments, and its return value, helping others (and your future self) understand your code better.

## Conclusion
This guide provides an overview of using ORM in Python, particularly with the Peewee ORM. By mapping Python objects to database tables, you can perform complex database operations with minimal SQL, focusing instead on writing clean and maintainable Python code. The examples provided should help you implement ORM effectively in your projects.
