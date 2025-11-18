from rest_framework import serializers
from studentorg.models import College, Student, Program 

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
      model = College
      fields = '__all__'
      
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


from rest_framework import serializers
from studentorg.models import College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


from rest_framework import serializers
from wildlife.models import ConservationSite, EndangeredSpecies

class ConservationSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationSite
        fields = '__all__'

class EndangeredSpeciesSerializer(serializers.ModelSerializer):

    conservation_site = ConservationSiteSerializer(read_only=TRUE)
    class Meta:
        model = EndangeredSite
        fields = '__all__'






from rest_framework import serializers
from wildlife.models import ConservationSite, EndangeredSite

class ConservationSiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConservationSite
        fields = '__all__'

class EndangeredSiteSerializer(serializers.ModelSerializer):

    conservation_site = ConservationSiteSerializers(read_only=TRUE)
    class Meta:
        model = EndangeredSite
        fields = '__all__'