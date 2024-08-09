""" # web/middleware.py

from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = timezone.now()
            last_activity = request.session.get('last_activity')

            if last_activity:
                last_activity = datetime.fromisoformat(last_activity)
                elapsed_time = current_time - last_activity
                if elapsed_time > timedelta(seconds=settings.SESSION_EXPIRE_SECONDS):
                    messages.add_message(request, messages.INFO, 'Your session has expired due to inactivity.')
                    return redirect(reverse('logout'))

            request.session['last_activity'] = current_time.isoformat()

        response = self.get_response(request)
        return response
 """