from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    # path('cbvindex/',views.Tasklistview.as_view(),name="cbvindex"), #class based ListView
    # path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name="cbvdetail"), #class based DetailView id = pk = Primary key #/<int:id>/
    # path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    # path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name="cbvdelete"),

]