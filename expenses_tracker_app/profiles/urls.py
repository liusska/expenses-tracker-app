from django.urls import path
from expenses_tracker_app.profiles.views import profile_details
from expenses_tracker_app.profiles.views import delete_profile
from expenses_tracker_app.profiles.views import edit_profile
from expenses_tracker_app.profiles.views import create_profile

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('edit/<int:pk>', edit_profile, name='edit profile'),
    path('delete/<int:pk>', delete_profile, name='delete profile'),

]