from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import get_language
from django.conf import settings

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None


def index(request):
    user_id = request.GET.get('login_as')
    user = get_user(user_id)

    # Optional: override timezone dynamically
    if user and user.get('timezone'):
        try:
            timezone.activate(user['timezone'])
        except Exception:
            timezone.activate(settings.TIME_ZONE)

    context = {
        "user": user,
        "language": get_language(),
    }
    return render(request, "index.html", context)
