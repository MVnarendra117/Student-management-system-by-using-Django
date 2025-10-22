from django.urls import path, include
from student import views
from rest_framework .routers import DefaultRouter


router = DefaultRouter()
router.register(r'students', views.StudentView, basename='student')
router.register(r'teachers', views.TeacherView, basename='teacher')
router.register(r'courses', views.CoursesView, basename='course') 


urlpatterns = [
    path('student_list/', views.student_list_view, name='student_list'),
    path('student_add/', views.student_creation_view, name='student_create'),
    path('edit_student/<int:id>/', views.student_edit_view, name='edit_student'),
    path('delete_student/<int:id>/', views.student_delete_view, name='delete_student'),
    path('', include(router.urls)),
]