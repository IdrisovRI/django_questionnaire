"""questionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import path, re_path, include
from django.contrib.auth.views import LogoutView
# from question.views import LoginView
from question.views import (
    LoginView,
    SurveyAddView,
    SurveyEditView,
    SurveyDeleteView,
    SurveyListView,
    QuestionAddView,
    QuestionEditView,
    QuestionDeleteView,
    QuestionListBySurveyView,
    ResponseView,
    ResponseListByUserView
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
# from

# router = DefaultRouter()
# router.register(r'surveys/actives', views.TransactionViewSet, base_name='transaction')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('surveys/', include([
        path('', SurveyListView.as_view(), name='survey_list'),
        path('add/', SurveyAddView.as_view(), name='add_survey'),
        path('edit/', SurveyEditView.as_view(), name='edit_survey'),
        path('delete/', SurveyDeleteView.as_view(), name='delete_survey'),
    ])),
    path('questions/', include([
        path('', QuestionListBySurveyView.as_view(), name='questions_list_by_survey'),
        path('add/', QuestionAddView.as_view(), name='add_question'),
        path('edit/', QuestionEditView.as_view(), name='edit_question'),
        path('delete/', QuestionDeleteView.as_view(), name='delete_question'),
    ])),
    path('responses/', include([
        path('', ResponseListByUserView.as_view(), name='response_list'),
        path('add/', ResponseView.as_view(), name='add_response'),
    ]))
]
