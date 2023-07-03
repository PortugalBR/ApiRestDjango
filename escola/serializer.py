from rest_framework import serializers
from escola.models import Aluno, Curso,Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude =[]

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    PERIODO = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'PERIODO']
    def get_PERIODO(self, obj):
        return obj.get_PERIODO_display()
    
class ListaAlunosMatriculadosCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields =['aluno_nome']
