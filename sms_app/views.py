from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Achievement, Category

# 1. Public List Page
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# 2. Secured Detail Page (Bonus Feature)
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    achievements = Achievement.objects.filter(student=student)
    categories = Category.objects.all() # Needed for the "Add Achievement" dropdown
    return render(request, 'student_detail.html', {
        'student': student, 
        'achievements': achievements,
        'categories': categories
    })

# 3. Student CRUD: Add
def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        reg_no = request.POST.get('register_number')
        course = request.POST.get('course')
        # Creates record using synchronized schema
        Student.objects.create(
            name=name, 
            register_number=reg_no, 
            course=course, 
            status='Active'
        )
    return redirect('student_list')

# 4. Student CRUD: Delete
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

# 5. Achievement CRUD: Add
def add_achievement(request, student_pk):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=student_pk)
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)
        
        Achievement.objects.create(
            student=student,
            category=category,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            status='pending'
        )
    return redirect('student_detail', pk=student_pk)

# 6. Achievement CRUD: Delete
def delete_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    student_pk = achievement.student.pk
    achievement.delete()
    return redirect('student_detail', pk=student_pk)