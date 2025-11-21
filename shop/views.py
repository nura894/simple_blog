from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category,Course
# Create your views here.

def index(request):
    courses= Course.objects.all()
    context={
        'courses': courses
    }
    return render(request, 'course.html', context)


def single_course(request,id):
    course= get_object_or_404(Course,pk=id)
    return render(request, 'course_details.html',{'course':course})



def add_course(request):
    if request.method == "POST":
        Course.objects.create(
            title=request.POST["title"],
            price=request.POST["price"],
            student_qty=request.POST["student_qty"],
            reviews_qty=request.POST["reviews_qty"],
            category_id=request.POST["category"],
        )
        return redirect("index")   # redirect to first page

    category = Category.objects.all()
    return render(request,'add_course.html',{'category':category})

def delete_course(request,id):
    course_del= get_object_or_404(Course,pk=id)
    course_del.delete()
    return redirect('index')

def update_course(request, id):
    course = get_object_or_404(Course, pk=id)
    category = Category.objects.all()

    if request.method == "POST":
        course.title = request.POST["title"]
        course.price = request.POST["price"]
        course.student_qty = request.POST["student_qty"]
        course.reviews_qty = request.POST["reviews_qty"]
        course.category_id = request.POST["category"]
        course.save()
        return redirect("index")

    context = {
        'course': course,
        'category': category,
    }

    return render(request, 'update.html', context)

def add_category(request):
    if request.method=='POST':
        Category.objects.create(
            title=request.POST['title']
        )
        next_page= request.GET.get('next',None)
        course_id= request.GET.get('id',None)

        if next_page=='add_course':
            return redirect('add_course')
        elif next_page=='update_course' and course_id:
            return redirect('update_course',id=course_id)

    return render(request,'add_category.html')