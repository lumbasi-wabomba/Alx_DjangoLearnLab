Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> myauthor = Author.objects.get(name="James Peterson")
>>> books = myauthor.book.all()
>>> for book in books:
...     print(book.title)
... 
the fairytale
the journey
>>>
>>>  Library.objects.get(name="Kenedy's Library")
>>> librarybooks = mylibrary.books.all()
>>> for librarybook in librarybooks:
...     print(librarybook.title)
... 
the journey
the fairytale
>>>
>>> print(mylibrary.librarian.name)
johnstone pearson
