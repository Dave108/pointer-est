# import urlparse
from django.shortcuts import HttpResponseRedirect


def subdomain_middleware(get_response):
    # One-time configuration and initialization.
    print("1st initialization")

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # print("before view")
        domain_list = ['accounts']
        # print(request.META['HTTP_HOST'])
        if request.META['HTTP_HOST'].split('.')[0] in domain_list:
            # print(domain_list)
            # print(request.META['HTTP_HOST'].split('.'))
            request.urlconf = 'accounts.urls'  # to redirect it to the accounts app's urls

        response = get_response(request)
        # print("after view")

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
