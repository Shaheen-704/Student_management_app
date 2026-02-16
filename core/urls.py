from django.urls import path
from sms_app import views  # Explicitly import from your app folder

urlpatterns = [
    # Student CRUD
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    
    # Achievement CRUD
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:student_pk>/add_achievement/', views.add_achievement, name='add_achievement'),
    path('achievement/delete/<int:pk>/', views.delete_achievement, name='delete_achievement'),
]