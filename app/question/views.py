from datetime import datetime
from django.shortcuts import get_object_or_404
import rest_framework.response as rest_response
from rest_framework import authentication
from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from question.forms import (
    SurveyForm,
    QuestionForm,
    ResponseForm
)
from question.models import (
    Survey,
    Question,
    Response
)


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    """
    A view that allows users to login providing their username and password.
    """
    permission_classes = ()
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return rest_response.Response({'token': token.key})


class SurveyAddView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = SurveyForm(request.data)
            if form.is_valid():
                form.save()
                return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class SurveyEditView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            survey = get_object_or_404(Survey, id=data['id'])
            form = SurveyForm(data, instance=survey)
            if form.is_valid():
                form.save()
                return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class SurveyDeleteView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            survey = get_object_or_404(Survey, id=data['id'])
            survey.delete()
            return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class SurveyListView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            surveys = Survey.objects.filter(
                start_date__lte=datetime.now(),
                end_date__gte=datetime.now()
            ).values()
            return rest_response.Response({"result": surveys}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class QuestionAddView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = QuestionForm(request.data)
            if form.is_valid():
                form.save()
                return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class QuestionEditView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            question = get_object_or_404(Question, id=data['id'])
            form = QuestionForm(request.data, instance=question)
            if form.is_valid():
                form.save()
                return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            question = get_object_or_404(Question, id=data['id'])
            question.delete()
            return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class QuestionListBySurveyView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            questions = Question.objects.filter(
                survey=data['survey']
            ).values()
            return rest_response.Response({"result": questions}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class ResponseView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ResponseForm(request.data)
            if form.is_valid():
                form.save()
                return rest_response.Response({"state": "Successful."}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class ResponseListByUserView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            responses = Response.objects\
                .select_related('question__survey') \
                .filter(person_id=data['person_id']) \
                .values('question__survey__name', 'question__text', 'answer')
            return rest_response.Response({"result": responses}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)
