### update book model
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
### after update
>>> mybook = Book.objects.get(title="Ninteen Eighty-Four");print(mybook.title);print(mybook.author);print(mybook.publication_year)
Ninteen Eighty-Four
George Orwell
1949