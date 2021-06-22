from django.urls import path
from . import views
urlpatterns = [
    path('', views.showAllMembers, name='isp-all-members'),
    path('add_users/', views.addUsers, name='isp-add-users'),
    path('edit_users/', views.editUsers, name='isp-edit-users'),
    path('packages/', views.packages, name='isp-packages'),
    path('add_packages/', views.addPackages, name='isp-packages'),
    path('invoice/', views.generateInvoice, name = 'isp-invoice'),
    path('login_check', views.login_check, name='cheking-login'),
    path('logout', views.logout, name='logout'),
    path('choose_package', views.choose_package, name='choosing-package')
]
