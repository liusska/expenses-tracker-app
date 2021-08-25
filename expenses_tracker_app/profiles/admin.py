from django.contrib import admin
from expenses_tracker_app.expenses.models import Expense
from expenses_tracker_app.profiles.models import Profile


admin.site.register(Profile)
admin.site.register(Expense)
