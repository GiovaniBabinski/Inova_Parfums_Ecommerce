# Generated by Django 4.2.5 on 2023-09-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_categoria_produto_delete_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria_produto',
            field=models.CharField(choices=[('PF', 'Perfumes'), ('DE', 'Desodorantes'), ('LO', 'Locoes'), ('SH', 'Shampoos'), ('CO', 'Condicionadores'), ('CR', 'Cremes'), ('SA', 'Sabonetes'), ('ES', 'Esmaltes'), ('MA', 'Maquiagens')], max_length=2),
        ),
    ]