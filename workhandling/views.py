# from django.shortcuts import render , get_object_or_404 , redirect
# from django.http import HttpResponse
# from database.models import Work, Classes
# # Create your views here.
# def work(request, pk):
#     classes = get_object_or_404(Classes,id=pk)
    
#     if request.method == 'POST':
#         todo = request.POST.get('announcement')
#         tasks = Work()
#         tasks.todos = todo
#         tasks.work_class = classes
#         if request.user == classes.user:
#             tasks.created_by = request.user
#             tasks.save()
#         else:
#             return HttpResponse('You are not allowed to do any announcements')
        
#     tasks = Work.objects.filter(work_class=classes)
#     return render(request,'workhandling/class.html',{
#         'tasks':tasks,
#         'classes':classes,
#         'class_name':classes.class_name,
#     })



# def edit(request,pk):
#     if request.method == 'POST':
#         edited = request.POST.get('edit')
#         edit = get_object_or_404(Work,id=pk)
#         edit.todos = edited
#         edit.save()
#         return redirect('/home')
    
#     edit = get_object_or_404(Work,id=pk)
#     task = edit.todos
#     classes = edit.work_class
#     user = edit.created_by
#     print(edit.id)
#     return render(request,'workhandling/edit.html',{
#         'task':task,
#         'classes':classes,
#         'user':user
#     })




# def delete(request,pk):
#     delete_obj = get_object_or_404(Work,id=pk, created_by=request.user)
#     delete_obj.delete()
#     return redirect('home:home')