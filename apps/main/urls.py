from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('Home', HomeListAPI.as_view(), name="Home list api"),
    path('Personal', PersonalListAPI.as_view(), name="Personal list api"),
    path('create/', PersonalCreateAPI.as_view(), name="Personal create api"),
    path('<int:pk>/', PersonalRetrieveAPI.as_view(), name="Personal retrieve api"),
    path('update/<int:pk>/', PersonalUpdateAPI.as_view(), name="Personal update api"),
    path('delete/<int:pk>/', PersonalDestroyAPI.as_view(), name="Personal delete api"),
    path('list_create/', PersonalListCreateAPI.as_view(), name="Personal create and list api"),
    path('multi/<int:pk>/', PersonalMultiAPI.as_view(), name="Personal multi api"),
]
