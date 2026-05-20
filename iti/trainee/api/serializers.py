from rest_framework import serializers
from course.models import Course
from trainee.models import Trainee


class StudentSerializer(serializers.Serializer):
    ID = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_null=False)
    email = serializers.EmailField(required=False, allow_null=True)
    age = serializers.IntegerField(allow_null=False)
    degree = serializers.DecimalField(decimal_places=2, max_digits=4, allow_null=False)
    image = serializers.ImageField(required=False, allow_null=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Trainee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
