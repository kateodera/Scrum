from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_ScrumMaster = models.BooleanField(default=False)
    is_Developer = models.BooleanField(default=False)


class Sprint(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('resolved', 'Resolved'),
        ('feedback', 'Feedback'),
        ('closed', 'Closed'),
        ('rejected', 'Rejected'),
        ('product_backlog_item', 'Product_Backlog_Item')
    )
    STATUS_CHOICE = ('developer', 'Developer')
    title = models.CharField(max_length=255)
    StartDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, verbose_name="Status", default="New")
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='sprintowner',
                              blank=True,
                              null=True)

    class Meta:
        ordering = ('-status',)




class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('resolved', 'Resolved'),
        ('feedback', 'Feedback'),
        ('closed', 'Closed'),
        ('rejected', 'Rejected')
    )

    title = models.CharField(max_length=250)
    sprint = models.ForeignKey(Sprint,
                               on_delete=models.CASCADE,
                               related_name='task',
                               )
    StartDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, verbose_name="Status", default="New")
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='taskowner',
                              blank=True,
                              null=True)

    class Meta:
        ordering = ('-status',)

    def __str__(self):
        return self.title
