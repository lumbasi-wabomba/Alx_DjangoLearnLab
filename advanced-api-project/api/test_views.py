from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from api.models import Author, Book  

User = get_user_model()


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user and token
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.token = Token.objects.create(user=self.user)
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {self.token.key}"}

        # Authors
        self.author1 = Author.objects.create(name="Andrew Pinkham")
        self.author2 = Author.objects.create(name="Mark Lutz")

        # Books
        self.book1 = Book.objects.create(title="Django Unleashed", publication_year=2015, author=self.author1)
        self.book2 = Book.objects.create(title="Learning Python", publication_year=2013, author=self.author2)

    def test_list_books_public(self):
        """Anyone can list books."""
        url = reverse("list-books")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 2)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book."""
        url = reverse("create-book")
        payload = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        resp = self.client.post(url, payload, format="json", **self.auth_headers)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book."""
        url = reverse("create-book")
        payload = {
            "title": "Another Book",
            "publication_year": 2021,
            "author": self.author2.id
        }
        resp = self.client.post(url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book_public(self):
        """Anyone can retrieve a single book."""
        url = reverse("list-detailed-books", args=[self.book1.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get("title"), self.book1.title)

    def test_update_book_authenticated(self):
        """Authenticated user can update a book."""
        url = reverse("update-book", args=[self.book1.id])
        payload = {"title": "Updated Django Book"}
        resp = self.client.patch(url, payload, format="json", **self.auth_headers)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_update_book_unauthenticated(self):
        """Unauthenticated user cannot update a book."""
        url = reverse("update-book", args=[self.book1.id])
        payload = {"title": "Fail Update"}
        resp = self.client.patch(url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book."""
        url = reverse("delete-book", args=[self.book2.id])
        resp = self.client.delete(url, **self.auth_headers)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        """Unauthenticated user cannot delete a book."""
        url = reverse("delete-book", args=[self.book1.id])
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_books(self):
        """Search filter works on title."""
        url = reverse("list-books")
        resp = self.client.get(url, {"search": "Django"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        found_titles = [book["title"] for book in resp.data]
        self.assertTrue(any("Django" in title for title in found_titles))

    def test_order_books_by_year_desc(self):
        """Ordering works on publication_year."""
        url = reverse("list-books")
        resp = self.client.get(url, {"ordering": "-publication_year"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in resp.data]
        self.assertEqual(years, sorted(years, reverse=True))
