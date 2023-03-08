from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly

class Home(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PersonSerializer
    
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     name = request.data['name']
    #     return Response({'object': name})


class QuestionListView(APIView):
    serializer_class = QuestionSerializer
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    """
    Create New Question 
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self, request):
        sez_data = QuestionSerializer(data=request.POST)
        if sez_data.is_valid():
            sez_data.save()
            return Response(sez_data.data, status=status.HTTP_201_CREATED)
        return Response(sez_data.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'questions deleted'}, status=status.HTTP_200_OK)