from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes,name="allRoutesAPI"),
    path('tasks',views.getTasks,name="allTasksAPI"),
    path('task/<str:pk>',views.getTask,name="getTaskAPI"),
    path('createTag',views.createTag,name="createTagAPI"),
    path('createTask',views.createTask,name="createTaskAPI"),
    path('updateTag/<str:pk>',views.updateTag,name="updateTagAPI"),
    path('updateTask/<str:pk>',views.updateTask,name="updateTaskAPI"),
    path('deleteTag/<str:pk>',views.deleteTag,name="deleteTagAPI"),
    path('deleteTask/<str:pk>',views.deleteTask,name="deleteTaskAPI"),
    path('tags',views.getTags,name="allTagsAPI"),
    path('tag/<str:pk>',views.getTag,name="getTagAPI"),
]