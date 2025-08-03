# Django Permissions and Groups Setup

## Overview

This app uses Django's built-in `groups` and `permissions` to restrict access to the `Book` model.

## Permissions

Custom permissions added to the `Book` model:

- `can_view`: View book list/details.
- `can_create`: Add a new book.
- `can_edit`: Edit book details.
- `can_delete`: Delete a book.

## Groups

- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

## How to Assign Permissions

You can use Django Admin or run:

```bash
python manage.py setup_permissions
