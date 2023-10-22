# from django.shortcuts import render , redirect , HttpResponse , get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login , logout
# from django.contrib import messages
# from database.models import Classes
# import random
# import string  




# def homepage(request):
#     username = 'Anonymous'
#     classes = ''
#     if request.user.is_authenticated:
#         username = request.user
#         classes = Classes.objects.filter(user = username)

#     return render(request,'home/home.html',{
#         'username':username,
#         'classes':classes
#     })

    

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

       
#         if User.objects.filter(username__iexact=username).exists():
#             return HttpResponse('Username already in use')
        
#         if User.objects.filter(email=email).exists():
#             return HttpResponse('email already in use')

#         if password1 != password2:
#             return HttpResponse('Check your password please')

#         my_user = User.objects.create_user(username,email,password1)
#         my_user.save()
#         return redirect('/login')
    
#     return render(request,'home/signup.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pass')
#         user = authenticate(request,username=username,password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('home:home')
#         else:
#             return HttpResponse("Email doesn't exist in our database")

#     return render(request,'home/login.html')


# def logouts(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("home:login")


# def createclass(request):
#     if request.method == 'POST':
#         user_class = Classes()
#         class_name = request.POST.get('subject')
#         about = request.POST.get('About')
#         user_class.user = request.user
#         user_class.class_name = class_name
#         user_class.About = about
#         user_class.class_code = unique_class_code(8)
#         user_class.save()
#         return redirect('home:home')
    
#     return render(request,'home/createclass.html')





# def unique_class_code(length):
#     characters = string.ascii_uppercase + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))

