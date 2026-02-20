from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    speciality = models.ForeignKey('tickets.IssueCategory', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name