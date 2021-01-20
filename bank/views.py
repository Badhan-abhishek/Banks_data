from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Branches, Banks
from .serializers import BranchesSerializer, BanksSerializer


# Listing all the data from Branches.
# @api_view(['GET', ])
# def branch_list(request):
#     try:
#         branches = Branches.objects.all()
#     except Branches.DoesNotExist:
#         return HttpResponse(status=404)
#     # Check for request method
#     if request.method == 'GET':
#         # Pass model to serializer
#         serializer = BranchesSerializer(branches, many=True)
#         return JsonResponse(serializer.data, safe= False)
#     else:
#         return HttpResponse("<h1>Nothing here</h1>")

class BranchList(ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

class CompleteSearch(ListAPIView):
    queryset = Branches.objects.order_by('ifsc')
    serializer_class = BranchesSerializer
    # Limit and Offset: Default 10
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('ifsc', 'bank__name', 'branch', 'address', 'city', 'district', 'state',)

class AutocompleteSearch(ListAPIView):
    queryset = Branches.objects.all().order_by('ifsc')
    serializer_class = BranchesSerializer
    # Limit and Offset: Default 10
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter)
    # $ for regex operation, remove to perform plain search 
    search_fields = ('$branch',)