import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer


@api_view(['GET'])
def test_api(request):
    return Response('test api success')


@api_view(['GET'])
def random_quiz(request, id):
    total_quizzes = Quiz.objects.all()
    random_quizzes = random.sample(list(total_quizzes), id)
    serializer = QuizSerializer(random_quizzes, many=True)
    return Response(serializer.data)


