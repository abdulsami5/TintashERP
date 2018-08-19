from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import os
import json


@csrf_exempt
@api_view(['GET',])
def get_swagger_json(request):
    """This Api endpoint is to get json specs for api documentation."""
    json_data = open("swagger.json")
    print(json_data)
    data1 = json.load(json_data)
#    print(data1)
    return Response(data1, status=status.HTTP_200_OK)
