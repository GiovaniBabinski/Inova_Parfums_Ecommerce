# Generated by Django 4.2.5 on 2023-10-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_lista_desejos'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='consumidor',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('U', 'Unissex')], default='M', max_length=2),
        ),
    ]
