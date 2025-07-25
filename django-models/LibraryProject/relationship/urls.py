from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('accounts/', include('relationship_app.urls')),
  # root is now handled by the app
]
