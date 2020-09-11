from django.urls import path
from . import views

urlpatterns=[
    path('',views.Arti_view.as_view(),name='home'),
    path('article/<int:pk>/',views.Arti_Detail_View.as_view(),name='detail'),
    path('article/new/',views.Arti_Create_View.as_view(),name='new'),
    path('article/<int:pk>/edit',views.Arti_Update_View.as_view(),name='edit'),
    path('article/<int:pk>/delete',views.Arti_Delete_view.as_view(),name='delete'),

]