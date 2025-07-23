from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TeacherProfile
from .models import StudentProfile


class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            TeacherProfile.objects.create(user=user)
        return user


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash password
        user.is_staff = False  # Make sure this is not a teacher/admin
        if commit:
            user.save()
            # ✅ Prevent duplicate StudentProfile
            if not hasattr(user, 'studentprofile'):
                StudentProfile.objects.create(user=user)
        return user



