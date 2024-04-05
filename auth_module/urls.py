from django.urls import path 
from . import views 
from .views import UserLoginAPIView,my_question,save_contact_message

urlpatterns = [
    path('user/' , views.CreateUserView.as_view(), name = 'create_user'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('question/', my_question, name='question'),
    path('contact_us/', save_contact_message, name='contact'),
   
 ]