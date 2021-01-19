from django.db import models
from datetime import datetime



class Project(models.Model):

    project_name =models.CharField(max_length=200, default=" ")
    project_category = models.CharField(max_length = 100, default=" " )
    project_status = models.CharField(max_length=100, default=" ")
    project_country = models.CharField(max_length=100, default=" ")
    project_start_date = models.DateTimeField(default=datetime.now)
    project_due_date = models.DateTimeField(default=datetime.now)




    def __str__(self):

        return self.project_name
