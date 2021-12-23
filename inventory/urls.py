from django.urls import path
from .views import *
app_name='inventory'    #namespace

urlpatterns = [
    path('',index ,name='index'),
    path('display_laptop', display_laptops,name='display_laptops'),
    path('display_desktop', display_desktops,name='display_desktops'),
    path('display_mobile', display_mobiles,name='display_mobiles'),

    path('add_laptop', add_laptop,name='add_laptop'),
    path('add_desktop', add_desktop,name='add_desktop'),
    path('add_mobile', add_mobile,name='add_mobile'),

    path('edit_laptop/(?P<pk>\d+)', edit_laptop,name='edit_laptop'),
    path('edit_desktop/(?P<pk>\d+)', edit_desktop,name='edit_desktop'),
    path('edit_mobile/(?P<pk>\d+)', edit_mobile,name='edit_mobile'),

    path('delete_laptop/(?P<pk>\d+)', delete_laptop,name='delete_laptop'),
    path('delete_desktop/(?P<pk>\d+)', delete_desktop,name='delete_desktop'),
    path('delete_mobile/(?P<pk>\d+)', delete_mobile,name='delete_mobile'),
    
]
