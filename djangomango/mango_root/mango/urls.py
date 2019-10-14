from django.urls import path, re_path
from . import views
from .apiviews import about_list, about_detail

urlpatterns = [
    path('', views.search, name='search'),
    path('addproject/', views.addproject, name='addproject'),
    path('instructions/', views.instruction, name='instruction'),
    path('about/', views.add_about, name='about_list'),
#    path("about/", about_list().as_view(), name="about_list"),
#    path("about/<int:pk>/", about_detail().as_view(), name="about_detail")
]
