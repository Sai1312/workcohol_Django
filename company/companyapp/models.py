from django.db import models

class CompanyItem(models.Model):
    deptID = models.AutoField(primary_key=True)
    deptname = models.CharField(max_length=100)

    def __str__(self):
        return self.deptname
