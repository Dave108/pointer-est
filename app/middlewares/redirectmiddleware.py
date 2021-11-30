# import urlparse
from django.shortcuts import HttpResponseRedirect


def redirect_middleware(get_response):
    # One-time configuration and initialization.
    print("1st initialization")

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("asijfbaib")
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'], "path----")
        response = get_response(request)
        print("after view", returnUrl)
        return response

    return middleware
