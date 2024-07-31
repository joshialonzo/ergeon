# Take Home Test from Ergeon

## Task 1

Describe in your own words what is GIL in python, and the pros and cons of it.

## Task 2

Write a decorator in python that will count how many times the decorated function was called. It should print
the number every time the decorated function is executed. Each function should be counted separately.

## Task 3

If you see that a SQL SELECT query is slow - what would you do to improve it?

## Task 4

What are the differences between “arrow” and “traditional” functions in javascript?

## Task 5

Write a basic React component showing number of clicks on it’s button, use images below as example, allow to configure initial value of click count.

________________
|Click Count: 1|
----------------

(Mouse click on button happens)

________________
|Click Count: 2|
----------------

## Task 6

Let’s say we have the following models in Django project:

```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```


```python
>>> leo_tolstoy = Author.objects.create(name=”Leo Tolstoy”)
>>> alexandre_dumas = Author.objects.create(name=”Alexandre Dumas”)
>>> Book.objects.create(title=”War and Peace”, author=leo_tolstoy)
>>> Book.objects.create(title=”Anna Karenina”, author=leo_tolstoy)
>>> Book.objects.create(title=”Resurrection”, author=leo_tolstoy)
>>> Book.objects.create(title=”The Three Musketeer”, author=alexandre_dumas)
>>> Book.objects.create(title=”The Count of Monte Cristo”, author=alexandre_dumas)
```

Assume we have ~100 books and ~25 authors in our database.
Try to write efficient queries, keep in mind how many requests the ORM can make to the database.

### 6.1

Using Django ORM, write a function that will print the book title and the author name (who wrote it) for all the books we have in the database. Like this:

“War and Peace”. Leo Tolstoy
“Anna Karenina”. Leo Tolstoy
“Resurrection”. Leo Tolstoy
“The Three Musketeers”. Alexandre Dumas
“The Count of Monte Cristo”. Alexandre Dumas

### 6.2

Write another function that will print the author’s name and all the books he wrote. For all the authors we have in the database. Like this:

Leo Tolstoy: “War and Peace”, “Anna Karenina”, “Resurrection”
Alexandre Dumas: “The Three Musketeers”, “The Count of Monte Cristo”

### 6.3

Implement the third function, it should print the author’s name and the number of books he wrote. Order by the number of books written, descending. Like this:

Leo Tolstoy: 3
Alexandre Dumas: 2
