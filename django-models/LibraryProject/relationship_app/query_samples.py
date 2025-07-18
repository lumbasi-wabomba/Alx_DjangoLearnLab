Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>>author_name = "James Peterson"
>>> author = Author.objects.get(name=author_name)
>>> books = Book.objects.filter(author=author)
>>> for book in books:
...     print(book.title)
... 
the fairytale
the journey
>>>
>>>library_name = "Kenedy's Library"
>>>  mylibrary = Library.objects.get(name=library_name)
>>> librarybooks = mylibrary.books.all()
>>> for librarybook in librarybooks:
...     print(librarybook.title)
... 
the journey
the fairytale
>>>
>>> print(mylibrary.librarian.name)
johnstone pearson
