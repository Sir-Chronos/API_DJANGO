from rest_framework import serializers
from gerenciador.models.tarefaModel import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'