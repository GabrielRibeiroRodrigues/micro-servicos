from rest_framework import serializers
from .models import Movimentacao

# Serializer para CRIAR uma movimentação (aceita apenas os IDs)
class MovimentacaoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['produto_id', 'setor_origem_id', 'setor_destino_id', 'quantidade']

# Serializer para LISTAR (apenas para estrutura, a view que monta os dados)
class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = '__all__'