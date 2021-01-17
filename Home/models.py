from django.db import models


class Project(models.Model):

    project_name =models.CharField(max_length=200, default=" ")
    project_category = models.CharField(max_length = 100, default=" " )
    project_status = models.CharField(max_length=100, default=" ")
    project_country = models.CharField(max_length=100, default=" ")




    def __str__(self):

        return self.project_name
