from django.contrib import admin
from django.urls import path
from .views import BranchList, AutocompleteSearch, CompleteSearch

urlpatterns = [
    path("", BranchList.as_view(), name="list"),
    path('branches', CompleteSearch.as_view(), name="search"),
    path('branches/autocomplete', AutocompleteSearch.as_view(), name="autocomplete")
    
]
