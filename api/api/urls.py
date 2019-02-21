
from django.contrib import admin
from django.urls import path
from courses import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<int:course_id>/', views.CourseById.as_view(), name='courses-id'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
