from django.contrib.auth.models import User
from django.db import models



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)  # Optional: admin can approve teachers

    def __str__(self):
        return f"{self.user.username} (Teacher)"




class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - Student"
    


