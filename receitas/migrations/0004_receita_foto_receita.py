# Generated by Django 3.2.3 on 2021-06-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='foto/%Y/%m/%d'),
        ),
    ]
