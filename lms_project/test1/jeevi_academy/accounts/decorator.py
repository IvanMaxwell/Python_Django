from django.shortcuts import redirect

# This allows only TEACHERS to see a page
def teacher_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'teacherprofile'):
            return view_func(request, *args, **kwargs)
        return redirect('login')  # or show error page
    return _wrapped_view

# This allows only STUDENTS to see a page
def student_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'studentprofile'):
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return _wrapped_view
