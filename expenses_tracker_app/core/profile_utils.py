from expenses_tracker_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
