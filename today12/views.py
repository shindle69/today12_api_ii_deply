from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from today12.models import Today12
from today12.serializers import Today12Serializer


@api_view()
def today12(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        today_12 = Today12.objects.get(pk=pk)
    except Today12.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Today12Serializer(today_12)
        return Response(serializer.data)

