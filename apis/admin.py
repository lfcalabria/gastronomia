from django.contrib import admin
from .models import *


@admin.register(ReceitaIngrediente)
class ReceitaIngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'receita',
        'produto',
        'quantidade',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(TipoCulinaria)
class TipoCulinariaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'tipo',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sigla',
        'descricao',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'quantidade',
        'unidade',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'data_cotacao',
        'valor',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = (
        'data_emissao',
        'valor',
        'fornecedor',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'localizacao',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(AulaReceita)
class AulaReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'aula',
        'receita',
        'qtd_receita',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'turno',
        'disciplina',
        'professor',
        'laboratorio',
        'qtd_aluno',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )

@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'tipo',
        'quantidade',
        'data_criacao',
        'data_ateracao',
        'ativo',
    )
