from studentorg.models import College, Student, Program # <-- update

# Serializer for Student (nested in Program)
class StudentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.prog_name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'lastname', 'firstname', 'middlename', 'program', 'program_name']
        read_only_fields = ['program_name']
        
# Serializer for Program with nested students
class ProgramSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True, source='student_set')

    class Meta:
        model = Program
        fields = ['id', 'prog_name', 'college', 'students']