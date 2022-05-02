from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:name>', views.say_name, name='name'),
    path('details/<int:question_id>', views.details, name='details')
]