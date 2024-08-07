# middleware.py
""" 
import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin

class SessionIdleTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        current_datetime = datetime.datetime.now()
        last_activity_str = request.session.get('last_activity', current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
        last_activity = datetime.datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S')
        idle_time = (current_datetime - last_activity).total_seconds()

        if idle_time > settings.SESSION_IDLE_TIMEOUT:
            logout(request)
        else:
            request.session['last_activity'] = current_datetime.strftime('%Y-%m-%d %H:%M:%S') """
