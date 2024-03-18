from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

class PreviousPageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated and request.path != reverse('login'):
            request.session['previous_page'] = request.path
