from django.db.models import Count

from .models import Author
from .models import Book


def print_books_with_authors():
    """
    This function will print the book title and the author name (who wrote it)
    for all the books we have in the database. Like this:

    “War and Peace". Leo Tolstoy
    “Anna Karenina". Leo Tolstoy
    “Resurrection". Leo Tolstoy
    “The Three Musketeers". Alexandre Dumas
    “The Count of Monte Cristo". Alexandre Dumas
    """

    books = Book.objects.select_related('author').all()

    for book in books:
        print(f'"{book.title}". {book.author.name}')


def print_authors_with_books():
    """
    This function will print the author’s name and all the books he wrote.
    For all the authors we have in the database. Like this:

    Leo Tolstoy: “War and Peace", “Anna Karenina", “Resurrection"
    Alexandre Dumas: “The Three Musketeers", “The Count of Monte Cristo"
    """
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        books = author.book_set.all()
        book_titles = ", ".join([f'"{book.title}"' for book in books])
        print(f'{author.name}: {book_titles}')


def print_authors_by_book_count():
    """
    This function will print the author’s name and the number of books he wrote.
    Order by the number of books written, descending. Like this:

    Leo Tolstoy: 3
    Alexandre Dumas: 2
    """
    authors = Author.objects.annotate(num_books=Count('book')).order_by('-num_books')

    for author in authors:
        print(f'{author.name}: {author.num_books}')
