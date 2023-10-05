from rest_framework import serializers
from gerenciador.models.alunoModel import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

