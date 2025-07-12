### delete book model
>>> mybook = Book.objects.get(title="Ninteen Eighty-Four")
>>> mybook.delete()
(1, {'bookshelf.Book': 1})


### after delete
>>> mybook = Book.objects.get(title="Ninteen Eighty-Four");print(mybook.title);print(mybook.author);print(mybook.publication_year)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/penguin/python/alx_django/venv/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/penguin/python/alx_django/venv/lib/python3.12/site-packages/django/db/models/query.py", line 633, in get
    raise self.model.DoesNotExist(
bookshelf.models.Book.DoesNotExist: Book matching query does not exist.
>>> 