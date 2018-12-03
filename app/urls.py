from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name='double'),
    path('subtract/', views.Subtract.as_view(), name='subtract'),
    path('multThree/', views.MultThree.as_view(), name='multThree'),
    path('earnings/', views.Earnings.as_view(), name='earnings'),
    path('both/', views.Both.as_view(), name='both'),
    path('walkordrive/', views.WalkOrDrive.as_view(), name='walkordrive'),
]
