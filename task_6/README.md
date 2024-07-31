# Answer

## Instructions

Get into the root project folder:

`cd task_6`

Create virtual environment using Python 3.11 or 3.12:

`python3.11 -m venv venv`
`python3.12 -m venv venv`

Install Python dependencies:

`pip install -r requirements`

Run migrations:

`python manage.py migrate`

Open the Django Shell:

`python manage.py shell`

Copy and paste all these Python lines in the shell:

```python
from books.models import Author
from books.models import Book
leo_tolstoy = Author.objects.create(name="Leo Tolstoy")
alexandre_dumas = Author.objects.create(name="Alexandre Dumas")
Book.objects.create(title="War and Peace", author=leo_tolstoy)
Book.objects.create(title="Anna Karenina", author=leo_tolstoy)
Book.objects.create(title="Resurrection", author=leo_tolstoy)
Book.objects.create(title="The Three Musketeer", author=alexandre_dumas)
Book.objects.create(title="The Count of Monte Cristo", author=alexandre_dumas)
```

Verify we created 5 books and 2 authors:

```python
Book.objects.all().count()
Author.objects.all().count()
```

Run the different functions created for this project and verify the requested output:

```python
from books.services import *

print_books_with_authors()
print_authors_with_books()
print_authors_by_book_count()
```