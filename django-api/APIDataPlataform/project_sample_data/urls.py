from django.urls import path
from .views import read_csv_file

urlpatterns = [
    path('', read_csv_file.as_view(),),
]
