from rest_framework.views import exception_handler
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import set_rollback
from rest_framework import exceptions



def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.
    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.
    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data ={'status':False,'message': exc.detail}
            # print('if')
        else:
            data = {'status':False,'message': exc.detail}
            # print('else')

        set_rollback()
        # print(data)
        return Response(data, status=exc.status_code, headers=headers)

    return None




# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.

#     response = exception_handler(exc, context)

#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status'] = 0
#         response.status_code = 200

#     return response    