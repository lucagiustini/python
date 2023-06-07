from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def is_done(self):
        return self.done

    def __str__(self):
        return f"{self.title} ({self.done})"
    


    