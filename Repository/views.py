from django.shortcuts import render
from Repository.models import Questions
from Repository.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self, request):
        qs = Questions.objects.all()                                        # Collection of Questions
        serializer_instance = QuestionSerializer(qs, many=True)             # many=True indicates serializer input 
                                                                            # contains multiple objects
        return Response(serializer_instance.data)                           # Return serialized data as a response
   
    def post(self, request):
        form_data = request.data                                            # form_data dictionary--->Python native type
        serializer_instance = QuestionSerializer(data=form_data)            # create serializer instance with form data
        if serializer_instance.is_valid():                                  # Check if the data is valid through serializer validation rules
            actual_data = serializer_instance.validated_data                # Get validated data from the serializer
            Questions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):                                             # pk is the primary key of the question to retrieve
        qs = Questions.objects.get(id=pk)                                   # get the question from the given primary key
        serializer_instance = QuestionSerializer(qs)                        # serialize the question object
        return Response(data=serializer_instance.data)                      # Return the serialize data as a response

    def put(self, request, pk):                                             # pk is the primary key of the question to update
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)            # Create serializer instance with form data
        if serializer_instance.is_valid():                                  # Check if the data is valid according to the serializer's val
            actual_data = serializer_instance.validated_data
            # Modelname.object.filter(id).update()
            Questions.objects.filter(id=pk).update(**actual_data)           # Update the question object with the given primary key
            return Response(data=serializer_instance.data)                  # Return the serialized data as a response
        else:
            return Response(data=serializer_instance.errors)                # Return the validation errors as a response