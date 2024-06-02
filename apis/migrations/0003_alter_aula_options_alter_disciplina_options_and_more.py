# Generated by Django 4.2.13 on 2024-05-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_aula_confirmada'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={'ordering': ['data', 'turno', 'disciplina'], 'verbose_name': 'Aula', 'verbose_name_plural': 'Aulas'},
        ),
        migrations.AlterModelOptions(
            name='disciplina',
            options={'ordering': ['nome'], 'verbose_name': 'Disciplina', 'verbose_name_plural': 'Disciplinas'},
        ),
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'ordering': ['nome'], 'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='laboratorio',
            options={'ordering': ['nome'], 'verbose_name': 'Laboratório', 'verbose_name_plural': 'Laboratórios'},
        ),
        migrations.AlterModelOptions(
            name='movimento',
            options={'ordering': ['produto', 'tipo'], 'verbose_name': 'Movimento', 'verbose_name_plural': 'Movimentos'},
        ),
        migrations.AlterModelOptions(
            name='notafiscal',
            options={'ordering': ['data_emissao'], 'verbose_name': 'Nota Fiscal', 'verbose_name_plural': 'Notas Fiscais'},
        ),
        migrations.AlterModelOptions(
            name='preco',
            options={'ordering': ['produto'], 'verbose_name': 'Preço', 'verbose_name_plural': 'Preços'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['nome'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['nome'], 'verbose_name': 'Professor', 'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterModelOptions(
            name='receita',
            options={'ordering': ['nome'], 'verbose_name': 'Receita', 'verbose_name_plural': 'Receitas'},
        ),
        migrations.AlterModelOptions(
            name='tipoculinaria',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo de Culinária', 'verbose_name_plural': 'Tipos de Culinária'},
        ),
        migrations.AlterModelOptions(
            name='unidademedida',
            options={'ordering': ['sigla'], 'verbose_name': 'Unidade de Medida', 'verbose_name_plural': 'Unidades de Medida'},
        ),
        migrations.AlterField(
            model_name='preco',
            name='valor',
            field=models.DecimalField(db_comment='Valor cotado por unidade de medida', decimal_places=2, default=0, max_digits=9),
        ),
        migrations.CreateModel(
            name='ItemNotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('preco_nitario', models.DecimalField(db_comment='preço unitário do produto', decimal_places=2, max_digits=9)),
                ('quantidade', models.DecimalField(db_comment='Quantidade comprada', decimal_places=5, max_digits=11)),
                ('notafiscal', models.ForeignKey(db_comment='ligacao com a tabela de nota fiscal', on_delete=django.db.models.deletion.RESTRICT, to='apis.notafiscal')),
                ('produto', models.ForeignKey(db_comment='ligacao com a tabela de produtos', on_delete=django.db.models.deletion.RESTRICT, to='apis.produto')),
            ],
            options={
                'verbose_name': 'Item da Nota Fiscal',
                'verbose_name_plural': 'Itens da Notas Fiscais',
                'db_table': 'itemnotafiscal',
                'ordering': ['notafiscal', 'produto'],
                'indexes': [models.Index(fields=['notafiscal'], name='itemnotafis_notafis_70ed22_idx'), models.Index(fields=['produto'], name='itemnotafis_produto_6d925d_idx')],
                'unique_together': {('notafiscal', 'produto')},
            },
        ),
    ]
