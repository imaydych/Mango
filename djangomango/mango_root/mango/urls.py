from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'AddProject', views.ListAddProject)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # static pages
    path('', views.search, name='search'),
    path('addprojects/', views.addproject, name='addproject'),
    path('instructions/', views.instruction, name='instruction'),
    path('about/', views.add_about, name='about_list'),
    # API list
    path('addproj/', views.ListAddProject.as_view()),
    # API objects by id's
    path('addproj/<int:pk>/', views.DetailAddProject.as_view()),
    # login/logout/registration
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
