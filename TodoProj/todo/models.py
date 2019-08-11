from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):

    task = models.CharField(max_length=50)
    state = models.PositiveSmallIntegerField(default=0)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

    def get_state(self):
        if self.state == 1:
            return "success"
        elif self.state == 2:
            return "warning"
        else:
            return "danger"

    def set_state(self):
        if self.state == 1:
            return "Could"
        elif self.state == 2:
            return "Should"
        else:
            return "MUST"
