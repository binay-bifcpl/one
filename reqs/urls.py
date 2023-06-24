from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('create-requisition/', views.create_requisition, name='create_requisition'),
    path('requisition-list/', views.requisition_list, name='requisition_list'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('requisition/<int:pk>/edit/', views.edit_requisition, name='edit_requisition'),
    path('requisition/<int:pk>/delete/', views.delete_requisition, name='delete_requisition'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
