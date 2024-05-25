import pandas as pd
from django_pandas.io import read_frame
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class ReceitaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = ReceitaIngrediente.objects.all()
    serializer_class = ReceitaIngredienteSerializer


class TipoCulinariaViewSet(viewsets.ModelViewSet):
    queryset = TipoCulinaria.objects.all()
    serializer_class = TipoCulinariaSerializer

    @action(detail=True, methods=('get',))
    def receitas(self, request, pk=None):
        id_tipo = self.get_object()
        serializer = ReceitaSerializer(id_tipo.tipoculinara.all(), many=True)
        return Response(serializer.data)


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PrecoViewSet(viewsets.ModelViewSet):
    queryset = Preco.objects.all()
    serializer_class = PrecoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer


class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class AulaReceitaViewSet(viewsets.ModelViewSet):
    queryset = AulaReceita.objects.all()
    serializer_class = AulaReceitaSerializer


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer


class MovimentoViewSet(viewsets.ModelViewSet):
    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer

    def create(self, request, *args, **kwargs):

        produto_queryset = Produto.objects.filter(id=request.data['id_produto'])
        quantidade_entrada = float(request.data['quantidade'])
        quantidade_produto = produto_queryset[0].quantidade
        if request.data['tipo'] == 'E' or request.data['tipo'] == 'A':
            quantidade_produto = float(quantidade_produto) + float(quantidade_entrada)
        else:
            quantidade_produto = float(quantidade_produto) - float(quantidade_entrada)
        produto_serializer = ProdutoSerializer(produto_queryset, many=True)
        produto_data = produto_serializer.data
        produto_data[0]['quantidade'] = quantidade_produto
        produto = Produto.objects.get(id=request.data['id_produto'])
        produto.quantidade = produto_data[0]['quantidade']
        produto.save()

        movimento_serializer = self.get_serializer(data=request.data)
        movimento_serializer.is_valid(raise_exception=True)
        self.perform_create(movimento_serializer)
        headers = self.get_success_headers(movimento_serializer.data)
        return Response(movimento_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustoDiarioApiView(APIView):
    """
    Custo por dia de aula prática
    """

    def __ultimas_cinco(self, group):
        """

        :param group: coluna de agrupamento
        :return: as 5 maiores de caga agrupamento
        """
        return group.head(5)

    def get(self, request):
        aulas = Aula.objects.all()
        df_aula = read_frame(aulas)
        aulas_receita = AulaReceita.objects.all()
        df_aulas_receita = read_frame(aulas_receita)
        df_aulas_receita['receita'] = df_aulas_receita['receita'].str.slice(0, 7)
        df_aulas_receita['receita'] = df_aulas_receita['receita'].astype(int)
        df_aulas_receita['aula'] = df_aulas_receita['aula'].str.slice(0, 7)
        df_aulas_receita['aula'] = df_aulas_receita['aula'].astype(int)
        df_custo = pd.merge(df_aula, df_aulas_receita, left_on=['id'],
                            right_on=['aula'], how='left')
        colunas = ['data', 'qtd_receita', 'receita']
        df_custo = df_custo[colunas]
        del aulas
        del aulas_receita
        del df_aula
        del df_aulas_receita
        receitas_ingrediente = ReceitaIngrediente.objects.all()
        df_receitas_ingrediente = read_frame(receitas_ingrediente)
        df_receitas_ingrediente['receita'] = df_receitas_ingrediente['receita'].str.slice(0, 7)
        df_receitas_ingrediente['receita'] = df_receitas_ingrediente['receita'].astype(int)
        df_receitas_ingrediente['produto'] = df_receitas_ingrediente['produto'].str.slice(0, 7)
        df_receitas_ingrediente['produto'] = df_receitas_ingrediente['produto'].astype(int)
        df_custo = pd.merge(df_custo, df_receitas_ingrediente, left_on=['receita'],
                            right_on=['receita'], how='left')
        df_custo['qtd'] = df_custo['qtd_receita'] * df_custo['quantidade']
        colunas = ['data', 'qtd', 'produto']
        df_custo = df_custo[colunas]
        df_custo = df_custo.groupby(['data', 'produto'])['qtd'].aggregate(['sum'])
        df_custo = df_custo.reset_index()
        del receitas_ingrediente
        del df_receitas_ingrediente
        precos = Preco.objects.all()
        df_precos = read_frame(precos)
        df_precos['produto'] = df_precos['produto'].str.slice(0, 7)
        df_precos['produto'] = df_precos['produto'].astype(int)
        df_precos = df_precos.sort_values(by='data_cotacao', ascending=False)
        df_precos = df_precos.groupby('produto').apply(self.__ultimas_cinco)
        print(df_precos.columns)
        df_precos.columns = ['id', 'data_criacao', 'data_ateracao', 'ativo', 'id_prod','data_cotacao', 'valor']
        df_precos = df_precos.groupby(['id_prod'])['valor'].aggregate(['mean'])
        df_precos = df_precos.reset_index()
        df_custo = pd.merge(df_custo, df_precos, left_on=['produto'],
                            right_on=['id_prod'], how='left')
        df_custo['sum'] = df_custo['sum'].astype(float)
        df_custo['mean'] = df_custo['mean'].astype(float)
        df_custo['custo'] = df_custo['sum'] * df_custo['mean']
        df_custo = df_custo.groupby(['data'])['custo'].aggregate(['sum'])
        df_custo = df_custo.reset_index()
        df_custo['sum'] = round(df_custo['sum'], 2)
        df_custo.columns = ['data', 'valor']
        print(df_custo)
        serializer = CustoDiarioSerializer(df_custo.to_dict(orient='records'), many=True)
        return Response(serializer.data)
