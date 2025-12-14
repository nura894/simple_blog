from django import forms
from django.contrib.auth.models import User
from shop.models import Course

class RegisterForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email','password']


from django import forms
from django.core.exceptions import ValidationError


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'price', 'student_qty', 'reviews_qty', 'category']

    def clean(self):
        cleaned_data = super().clean()  #First run Django’s built-in validation

        price = cleaned_data.get("price")
        student_qty = cleaned_data.get("student_qty")
        reviews_qty = cleaned_data.get("reviews_qty")

        if price is not None and price <= 0:
            self.add_error("price", "Price cannot be negative.")

        if student_qty is not None and student_qty <= 0:
            self.add_error("student_qty", "Student quantity cannot be negative.")

        if reviews_qty is not None and reviews_qty <= 0:
            self.add_error("reviews_qty", "Reviews quantity cannot be negative.")

        return cleaned_data

