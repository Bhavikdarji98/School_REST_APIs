from rest_framework import serializers
from students.models import Student, Teacher, Lecture

class StudentSerializer(serializers.ModelSerializer):
    """
    The serialzers to serializer and Deserialzer
    Student object
    """
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    """
    The serializer to serialze and deseralize 
    Teacher object
    """
    class Meta:
        model = Teacher
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    """
    The serializer to serialze and deseralize 
    Lecture object
    """
    student = StudentSerializer(many= True, read_only= True)
    students_ids = serializers.PrimaryKeyRelatedField(
        many= True, write_only= True, queryset = Student.objects.all()
    )
    class Meta:
        model = Lecture
        fields = ['id',
            'name',
            'description',
            'time',
            'teacher',
            'student',
            'students_ids',]

    def create(self, validated_data):
        students = validated_data.pop("students_ids", None)
        lecture = Lecture.objects.create(**validated_data)
        if students:
            lecture.student.set(students)
        return lecture
    
    def update(self, instance, validated_data):
        students = validated_data.pop('students_ids', None)
        instance = super(LectureSerializer, self).update(instance, validated_data)

        for s in students:
            print(s.id)
            obj = Student.objects.filter(id = s.id)

            if obj.exists():
                student = obj.first()
            else:
                pass
            instance.student.add(student.id)
        return instance