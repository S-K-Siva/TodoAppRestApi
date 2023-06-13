from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TaskForm, TagForm
from .models import Task,Tags

def home_page(request):
    tasks = Task.objects.all()[::-1]
    
    return render(request,'frontEnd/index.html',{'tasks':tasks})


def createTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        all_tags = Tags.objects.get_or_create(name=request.POST.get('new_tag'))

        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'frontEnd/task_form.html',{'form':form})

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.tags = request.POST.get('tags')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')
        task.save()
        return redirect('homepage')
    return render(request,'frontEnd/task_form.html',{'task':task,'form':form})
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
            task.delete()
            return redirect('homepage')
    return render(request,'frontEnd/delete_task.html',{'task':task})


def detailTask(request,pk):
    task = Task.objects.get(id=pk)
    return render(request,'frontEnd/task_detail.html',{'task':task})



def createTag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'frontEnd/tag_form.html',{'form':form})

def updateTag(request,pk):
    tag = Tags.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == "POST":
        tag.name = request.POST.get('name')
        tag.save()
        return redirect('homepageTags')
    return render(request,'frontEnd/tag_form.html',{'form':form})

def deleteTag(request,pk):
    tag = Tags.objects.get(id=pk)
    if request.method == "POST":
            tag.delete()
            return redirect('homepageTags')

    return render(request,'frontEnd/delete_tag.html',{'tag':tag})

def allTags(request):
    tags = Tags.objects.all()[::-1]
    return render(request,'frontEnd/tags.html',{'tags':tags})