# ip_tracking/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def login_view(request):
    if request.method == 'POST':
        # Your login logic
        pass
    return render(request, 'login.html')

@login_required
@ratelimit(key='user', rate='10/m', block=True)
def sensitive_view(request):
    return render(request, 'sensitive.html')