from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializers,TagSerializers
from frontEnd.models import Task,Tags
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getRoutes(request,format=None):
    routes = [
        'GET /apis/',
        'GET /apis/tags/',
        'GET /apis/tasks/',
        'POST /apis/createTask/',
        'POST /apis/createTag/',
        'GET /apis/task/:id',
        'GET /apis/tag/:id',
        'PUT /apis/updateTag/:id',
        'PUT /apis/updateTask/:id',
        'DELETE /apis/deleteTask/:id',
        'DELETE /apis/deleteTag/:id',
    ]
    return Response(routes)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['CREATE','POST'])
def createTask(request,format=None):
    serializer = TaskSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT','POST'])
def updateTask(request,pk,format=None):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def deleteTask(request,pk,format=None):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Has been deleted successfully!")

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['CREATE','POST'])
def createTag(request,format=None):
    serializer = TagSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT','POST'])
def updateTag(request,pk,format=None):
    tag = Tags.objects.get(id=pk)
    serializer = TagSerializers(instance = tag, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def deleteTag(request,pk,format=None):
    tag = Tags.objects.get(id=pk)
    tag.delete()
    return Response("Task Has been deleted successfully!")
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getTasks(request,format=None):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks,many=True)
    return Response(serializer.data)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getTask(request,pk,format=None):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task,many=False)
    return Response(serializer.data)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getTags(request,format=None):
    tags = Tags.objects.all()
    serializer = TagSerializers(tags,many=True)
    return Response(serializer.data)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getTag(request,pk,format=None):
    tag = Tags.objects.get(id=pk)
    serializer = TagSerializers(tag,many=False)
    return Response(serializer.data)

