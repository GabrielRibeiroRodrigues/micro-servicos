import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movimentacao
from .serializers import MovimentacaoSerializer, MovimentacaoCreateSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()

    def get_serializer_class(self):
        # Usar um serializer para criar (que aceita IDs)
        if self.action == 'create':
            return MovimentacaoCreateSerializer
        # E outro para listar/detalhar (que mostra os dados completos)
        return MovimentacaoSerializer

    def list(self, request, *args, **kwargs):
        # Pega todas as movimentações do nosso banco de dados
        movimentacoes = self.get_queryset()

        # Lista para guardar os dados enriquecidos
        dados_enriquecidos = []

        for mov in movimentacoes:
            try:
                # Chama a API do serviço de produtos para pegar o nome
                url_produto = f"http://servico-produtos:8000/api/produtos/{mov.produto_id}/"
                produto_data = requests.get(url_produto).json()

                # Chama a API do serviço de setores para pegar os nomes
                url_setor_origem = f"http://servico-setores:8000/api/setores/{mov.setor_origem_id}/"
                setor_origem_data = requests.get(url_setor_origem).json()

                url_setor_destino = f"http://servico-setores:8000/api/setores/{mov.setor_destino_id}/"
                setor_destino_data = requests.get(url_setor_destino).json()

                dados_enriquecidos.append({
                    'id': mov.id,
                    'produto': produto_data,
                    'setor_origem': setor_origem_data,
                    'setor_destino': setor_destino_data,
                    'quantidade': mov.quantidade,
                    'data': mov.data
                })
            except requests.exceptions.RequestException as e:
                # Lidar com erros, caso um serviço esteja fora do ar
                print(f"Erro ao buscar dados para movimentação {mov.id}: {e}")
                # Pode-se adicionar um objeto de erro na resposta
                dados_enriquecidos.append({'id': mov.id, 'erro': 'Não foi possível buscar todos os dados.'})

        return Response(dados_enriquecidos)