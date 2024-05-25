from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('receitasingrediente', ReceitaIngredienteViewSet)
router.register('tiposculinaria', TipoCulinariaViewSet)
router.register('receitas', ReceitaViewSet)
router.register('unidadesmedida', UnidadeMedidaViewSet)
router.register('produtos', ProdutoViewSet)
router.register('precos', PrecoViewSet)
router.register('professores', ProfessorViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('laboratorios', LaboratorioViewSet)
router.register('receitasaula', AulaReceitaViewSet)
router.register('aulas', AulaViewSet)
router.register('movimentos', MovimentoViewSet)
router.register('notasfiscais', NotaFiscalViewSet)

urlpatterns = [
    path('', CustoDiarioApiView.as_view(), name='custosdiario'),
]