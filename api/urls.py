from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('category',views.CategoryViewSet, basename='category' )
router.register('api/course', views.CourseListAPI, basename='course')

urlpatterns=[
    path("course/", views.course_page, name='course_page'),
    path("course/<int:pk>/", views.course_detail, name="course_detail"),
    #path('api/course/', views.CourseListAPI.as_view(), name='api_course'),
    #path('api/course/<int:pk>/', views.CourseDetailAPI.as_view(), name='api_course_details'), #pk is required (not id) because generics expect pk.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register-page/',views.register_page, name='register_page'),
    path("register/", views.RegisterView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('', include(router.urls)),
    #path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]