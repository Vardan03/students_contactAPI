from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'lastname', 'contacts', 'createdAt', 'updatedAt']
        read_only_fields = ['id', 'createdAt', 'updatedAt']