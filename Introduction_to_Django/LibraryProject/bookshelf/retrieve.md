### retrieve book model

>>> mybook = Book.objects.get(title="1984");print(mybook.title);print(mybook.author);print(mybook.publication_year)
1984
George Orwell
1949
>>> 