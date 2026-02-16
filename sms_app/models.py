from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    register_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('pending', 'pending')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)