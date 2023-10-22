from django.db import models
from django.contrib.auth.models import User

class Classes(models.Model):
    user = models.ForeignKey(User,related_name='classes',on_delete=models.CASCADE)
    class_code = models.CharField(max_length=8)
    class_name = models.CharField(max_length=200)
    # student = models.ManyToManyField(User, related_name='student')
    About = models.TextField(blank=False)
    def __str__(self):
        return self.class_code

class Work(models.Model):
    work_class = models.ForeignKey(Classes,related_name='work',on_delete=models.CASCADE)
    todos = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , on_delete=models.CASCADE)



class Student(models.Model):
    class_joined = models.CharField(max_length=8)
    student_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    models.CharField(max_length=150)



# class Conversation(models.Model):
#     item = models.ForeignKey(Classes,related_name = 'conversations',on_delete=models.CASCADE)
#     members = models.ManyToManyField(User,related_name='conversations')
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('-modified_at',)


# class ConversationMessage(models.Model):
#     conversation = models.ForeignKey(Conversation, related_name = 'messages',on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User,related_name='created_messages',on_delete=models.CASCADE)
