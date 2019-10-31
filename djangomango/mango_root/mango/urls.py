from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'MangoAbout', views.MangoAboutViewSet)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # static pages
    path('', views.search, name='search'),
    path('addproject/', views.addproject, name='addproject'),
    path('instructions/', views.instruction, name='instruction'),
    path('about/', views.add_about, name='about_list'),
    #path('', include(router.urls)),
    # API list and objects
    path('MangoAbout/', views.ListMangoAbout.as_view()),
    path('MangoAbout/<int:pk>/', views.DetailMangoAbout.as_view()),
    # login/logout/registration
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
