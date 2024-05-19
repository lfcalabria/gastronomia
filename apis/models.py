from django.db import models

class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')
    data_ateracao = models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')
    ativo = models.BooleanField(default=True, db_comment='Indicador se o dado ainda está ativo')

    class Meta:
        abstract = True


class ReceitaIngrediente(Base):
    id_receita = models.ForeignKey('Receita', on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de receita')
    id_produto = models.ForeignKey('Produto', on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de produto')
    quantidade = models.DecimalField(max_digits=9, decimal_places=2,
                                     db_comment='quantidade usada na receita por unidade de medida',
                                     )

    class Meta:
        verbose_name = 'Ingrediente da Receita'
        verbose_name_plural = 'Ingredientes da Receita'
        unique_together = ('id_receita', 'id_produto')
        indexes = (
            models.Index(fields=('id_receita',)),
            models.Index(fields=('id_produto',)),
        )
        db_table = 'receitaingrediente'


class TipoCulinaria(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do tipo de culinária')
    class Meta:
        verbose_name = 'Tipo de Culinária'
        verbose_name_plural = 'Turmas'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tipoculinaria'


class Receita(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do tipo de receita')
    id_tipo = models.ForeignKey(TipoCulinaria, on_delete=models.RESTRICT,
                                db_comment='ligacao com a tabela de tipo de culinaria')
    ingredientes = models.ManyToManyField('Produto', through='ReceitaIngrediente')
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        unique_together = ('nome', 'id_tipo')
        indexes = (
            models.Index(fields=('nome',)),
            models.Index(fields=('id_tipo',)),
        )
        db_table = 'receita'


class UnidadeMedida(Base):
    sigla = models.CharField(max_length=5, blank=False, unique=True, null=False,
                             db_comment='Sigla da unidade de medida')
    descricao = models.CharField(max_length=100, blank=False, null=False,
                                 db_comment='Descrição da unidade de medida')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'
        indexes = (
            models.Index(fields=('sigla',)),
        )
        db_table = 'unidademedida'

class Produto(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do produto')
    quantidade = models.IntegerField(default=0, db_comment='Quantidade disponível')
    id_unidade = models.ForeignKey(UnidadeMedida, on_delete=models.RESTRICT,
                                db_comment='ligação com tabela de unidade de medida')
    receitas = models.ManyToManyField('Receita', through='ReceitaIngrediente')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        indexes = (
            models.Index(fields=('nome',)),
            models.Index(fields=('id_unidade',)),
        )
        db_table = 'produto'


class Preco(Base):
    id_produto = models.ForeignKey(Produto, on_delete=models.RESTRICT,
                                   db_comment='ligação com tabela de produto')
    data_cotacao = models.DateField(blank=False, unique=True, null=False,
                            db_comment='Data Cotação')
    valor = models.DecimalField(max_digits=9, decimal_places=2,
                                db_comment='Valor cotado por unidade de medida',
                                )

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'
        indexes = (
            models.Index(fields=('id_produto',)),
        )
        db_table = 'preco'


class Professor(Base):
    nome = models.CharField(max_length=100, blank=False, null=False,
                            db_comment='Nome do professor')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = '`Professores`'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'professor'


class Disciplina(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome da disciplina')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = '`Disciplinas`'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'disciplina'


class Fornecedor(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do fornecedor')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = '`Fornecedores`'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'fornecedor'


class NotaFiscal(Base):
    data_emissao = models.DateField(blank=False, null=False,
                                    db_comment='Data de emissão da nota fiscal')
    valor = models.DecimalField(max_digits=9, decimal_places=2,
                                db_comment='Valor total da nota fiscal',
                                blank=False, null=False
                                )
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de fornecedor')

    class Meta:
        verbose_name = 'Nota Fiscal'
        verbose_name_plural = 'Notas Fiscais'
        indexes = (
            models.Index(fields=('id_fornecedor',)),
        )
        db_table = 'notafiscal'


class Laboratorio(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do laboratório')
    localizacao = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Localização do laboratório')

    class Meta:
        verbose_name = 'Laboratório'
        verbose_name_plural = 'Laboratórios'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'laboratorio'


class AulaReceita(Base):
    id_aula = models.ForeignKey('Aula', on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de aula')
    id_receita = models.ForeignKey('Receita', on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de receita')

    qtd_receita = models.IntegerField(blank=False, null=False, db_comment='Quantidade de receitas previstas para a aula')

    class Meta:
        verbose_name = 'Receita da Aula'
        verbose_name_plural = 'Receitas das Aulas'
        unique_together = ('id_aula', 'id_receita')
        indexes = (
            models.Index(fields=('id_aula',)),
            models.Index(fields=('id_receita',)),
        )
        db_table = 'aulareceita'


class Aula(Base):
    TURNO_CHOICE = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('V', 'Vespertino'),
        ('N', 'Noite'),
        ('I', 'Integral'),
    )
    data = models.DateField(blank=False, null=False, db_comment='Data da aula')
    turno = models.CharField(max_length=1, blank=False, null=False,
                             db_comment='Turno da aula', choices=TURNO_CHOICE)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de disciplina')
    id_professor = models.ForeignKey(Professor, on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de professor')
    id_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de laboratorio')
    qtd_aluno = models.IntegerField(blank=False, null=False,
                                    db_comment='Número de alunos previsto')
    receitas = models.ManyToManyField('Receita', through='AulaReceita')

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        unique_together = ('data', 'turno', 'id_professor')
        indexes = (
            models.Index(fields=('id_disciplina',)),
            models.Index(fields=('id_professor',)),
            models.Index(fields=('id_laboratorio',)),
        )
        db_table = 'aula'


class Movimento(Base):
    TIPO_CHOICE = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
        ('A', 'Ajuste de auditoria'),
    )
    id_produto = models.ForeignKey(Produto, on_delete=models.RESTRICT,
                                      db_comment='Ligação com a tabela de produto')
    tipo = models.CharField(max_length=1, blank=False, null=False,
                             db_comment='Tipo do movimento', choices=TIPO_CHOICE)
    quantidade = models.IntegerField(blank=False, null=False,
                                    db_comment='Quantidade movimentada')

    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentos'
        indexes = (
            models.Index(fields=('id_produto',)),
        )
        db_table = 'movimento'
