from django.db import models
import uuid

class Tags(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=1000,null=True,blank=True)
    tags = models.ManyToManyField('Tags')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    STATUS_CHOICES = (
        ('OPEN', 'OPEN'),
        ('WORKING', 'WORKING'),
        ('DONE', 'DONE'),
        ('OVERDUE','OVERDUE')
    )
    status = models.CharField(max_length=7,choices=STATUS_CHOICES,default='OPEN')

    def __str__(self):
        return self.title
