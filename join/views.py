from django.shortcuts import render , HttpResponse , get_object_or_404 , redirect

# Create your views here.
from database.models import Student , Classes



def join(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        class_owner = get_object_or_404(Classes,class_code=code)
        student = Student()
        student.class_joined = class_owner.class_code
        print(student['class_joined'])
        print(student)
        # student.class_joined = class_owner.class_code
        # student.student_name = request.user
        # student.created_by = class_owner.user
        # student.save()
        # return redirect('home:home')
    return render(request,'join/joinhome.html',{

    })