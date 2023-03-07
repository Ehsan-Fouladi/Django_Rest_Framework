from  . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('questions/', views.QuestionListView.as_view(), name='List_view'),
    path('question/create/', views.QuestionCreateView.as_view(), name='Created_view'),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='Update_view'),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='Delete_view'),
]