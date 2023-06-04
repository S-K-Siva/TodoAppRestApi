from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home_page,name="homepage"),
    path('createTask',views.createTask,name="createTask"),
    path('detailTask/<str:pk>',views.detailTask,name="detailTask"),
    path('updateTask/<str:pk>',views.updateTask,name="updateTask"),
    path('deleteTask/<str:pk>',views.deleteTask,name="deleteTask"),
    path('createTag',views.createTag,name="createTag"),
    path('updateTag/<str:pk>',views.updateTag,name="updateTag"),
    path('deleteTag/<str:pk>',views.deleteTag,name="deleteTag"),
    path('tags',views.allTags,name="homepageTags"),
    path('apis/',include('api.urls')),
]