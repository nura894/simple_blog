from rest_framework import serializers
from shop.models import Course, Category
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'price', 'student_qty', 'reviews_qty', 'category', 'category_name']



class CategorySerializer(serializers.ModelSerializer):
    coursa= CourseSerializer(many=True, read_only=True)   #nested 
    class Meta:
        model = Category
        fields= '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
        message="This email is already registered."    )]
    )

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(),
        message="This username is already taken."     )]
    )

    class Meta:
        model = User
        fields = ["username","email", "password"]

    def validate_password(self,value):
        if len(value)<4:
            raise serializers.ValidationError("Password must be at least 4 characters.")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)        