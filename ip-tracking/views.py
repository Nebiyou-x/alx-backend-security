from ratelimit.decorators import ratelimit
from django.http import HttpResponse

@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def authenticated_view(request):
    return HttpResponse("Authenticated OK")

@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def anonymous_view(request):
    return HttpResponse("Anonymous OK")
