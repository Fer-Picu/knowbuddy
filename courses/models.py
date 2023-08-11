from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    open_subscription = models.BooleanField(default=False)

    def __str__(self):
        super().__str__()
        return self.title