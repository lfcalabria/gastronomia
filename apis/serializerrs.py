from rest_framework import serializers
from .models import *


class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaIngrediente
        fields = (
            'id_receita',
            'id_produto',
            'quantidade',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class TipoCulinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCulinaria
        fields = (
            'nome',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = (
            'nome',
            'id_tipo',
            'data_criacao',
            'data_ateracao',
            'ativo',
            'ingredientes',
    )


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = (
            'sigla',
            'descricao',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'nome',
            'quantidade',
            'id_unidade',
            'data_criacao',
            'data_ateracao',
            'ativo',
            'receitas',
    )


class PrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preco
        fields = (
            'id_produto',
            'data_cotacao',
            'valor',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = (
            'nome',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = (
            'nome',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = (
            'nome',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = (
            'data_emissao',
            'valor',
            'id_fornecedor',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = (
            'nome',
            'localizacao',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class AulaReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaReceita
        fields = (
            'id_aula',
            'id_receita',
            'qtd_receita',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = (
            'data',
            'turno',
            'id_disciplina',
            'id_professor',
            'id_laboratorio',
            'qtd_aluno',
            'data_criacao',
            'data_ateracao',
            'ativo',
            'receitas',
    )


class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimento
        fields = (
            'id_produto',
            'tipo',
            'quantidade',
            'data_criacao',
            'data_ateracao',
            'ativo',
    )
    