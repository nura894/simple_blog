from django.urls import path
from . import views   #from views import index

urlpatterns = [
   path('shop/', views.index, name='index'),
   path('shop/<int:id>/', views.single_course, name='single_course'),
   path('add-course/', views.add_course, name='add_course'),
   path('shop/delete/<int:id>/', views.delete_course, name='delete_course'),
   path('shop/update/<int:id>/', views.update_course, name='update_course'),
   path('shop/category/', views.add_category, name='add_category'),
]