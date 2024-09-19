from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets, generics
from rest_framework.views import APIView    
from rest_framework.decorators import api_view
from rest_framework.response import Response


class StudentSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', '') 

        if search_query:
            students = Student.objects.filter(name_icontains=search_query)
        else:
            students = Student.objects.all()

        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class ClientListView(APIView):
    def get(self, request):
        clients = Student.objects.all()
        serializer = StudentSerializers(clients, many=True)
        return Response(serializer.data)
    

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


@api_view(["GET", "POST"])
def create_or_get_students(request):
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'GET':
        # clients = Student.objects.all()
        # serializer = StudentSerializers(clients, many=True)
        # return Response(serializer.data)
        search_query = request.GET.get('search', '') 

        if search_query:
            students = Student.objects.filter(name__icontains=search_query)
        else:
            students = Student.objects.all()

        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)