from django.core.exceptions import ValidationError
from django.test import TestCase
from shop.models import Category, Course



class CourseModelTest(TestCase):
    def setUp(self):
        self.course=Course(title="Test Course", price=100.0, student_qty=50, reviews_qty=10, category=Category(title="Test Category"), created_by=None)

    def test_course_price_morethan_zero(self):
        self.assertTrue(self.course.price_morethan_zero)
       
        self.course.price = -10.0
        self.assertFalse(self.course.price_morethan_zero)    

    def test_negative_review_validation(self):
        self.course.reviews_qty=-5
        self.assertRaises(ValidationError, self.course.full_clean)    #This calls full_clean(), which checks: field validators, model clean(), constraints

       

