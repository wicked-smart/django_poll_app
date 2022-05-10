from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:name>', views.say_name, name='name'),
    path('details/<int:question_id>', views.details, name='details'),
    path('vote/<int:question_id>', views.vote, name="vote"),
    path('result/<int:question_id>', views.result, name="result"),
    path('add_poll/', views.add_poll, name="add_poll")
]