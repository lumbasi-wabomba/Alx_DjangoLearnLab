## User Permissions & Groups

### Custom Permissions (Defined in `Article` model):
- `can_view`: Can view articles
- `can_create`: Can create new articles
- `can_edit`: Can edit existing articles
- `can_delete`: Can delete articles

### User Groups
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

### How Permissions Are Enforced
Views are protected using `@permission_required('app_name.permission_codename')` decorators. Unauthorized users will receive a 403 error.

To test, assign users to groups via Django Admin and log in as them to verify access control works.
