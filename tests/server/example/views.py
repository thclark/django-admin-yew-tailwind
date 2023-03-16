from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def do_something(_):
    """A simple view, demonstrating how to do something"""
    return JsonResponse({"did": "something"}, status=201)
