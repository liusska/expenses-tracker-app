from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses_tracker_app.expenses.urls')),
    path('profile/', include('expenses_tracker_app.profiles.urls')),
]
