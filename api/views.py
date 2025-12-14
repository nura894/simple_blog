from django.shortcuts import render,redirect
from shop.models import Category,Course
from django.http import JsonResponse
from .serializers import CategorySerializer, CourseSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# def api_course(request):
#     course= Course.objects.all()
#     course_list= list(course.values())
#     return JsonResponse(course_list,safe=False)

# @api_view(['GET'])
# def api_course(request):
#     if request.method=="GET":
#         course= Course.objects.all()
#         serializer= CourseSerializer(course, many=True)  #many=true bz of course are multiple
#         return Response(serializer.data)

def course_page(request):
    return render(request, "collection/js_api/js_course_list.html")

class CourseListAPI(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset= Course.objects.all()
    serializer_class=CourseSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# class CourseDetailAPI(RetrieveUpdateDestroyAPIView):
#     queryset= Course.objects.all()
#     serializer_class=CourseSerializer    


def course_detail(request, pk):
    return render(request, "collection/js_api/course_detail.html", {"pk": pk})

def register_page(request):
    return render(request, "collection/js_api/register1.html")

# class RegisterView(APIView):
#     def post(self,request):
#         username= request.data.get('username')
#         password= request.data.get('password')

#         if User.objects.filter(username=username).exists():
#             return Response({'error': 'User already exists'})
        
#         user= User.objects.create(
#             username= username,
#             password= make_password(password)
#         )
#         return Response({"message":"User created successfully"})
    

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered"}, status=201)

        return Response(serializer.errors, status=400)

    
class ProfileView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self,request):
        return Response({
            'message':'You are authenticated',
            'username': request.user.username
        })


class CategoryViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action in ['destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    
    queryset= Category.objects.all()
    serializer_class= CategorySerializer

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        category = self.get_object()
        courses = category.coursa.all()
        serializer= CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
# def register_view(request):
#     if request.method=='POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user=User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password= form.cleaned_data['password'],
#             )
#             login(request,user)
#             return redirect("course_page")
#     else:
#         form=RegisterForm()

#     return render(request, 'register.html', {'form':form})        


def login_view(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user= authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('course_page')
        
        return render(request,'login.html', {'error':'Invalid Credentials'})
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('course_page')