# Generated by Django 4.2.7 on 2023-11-10 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_sample_data', '0002_alter_tb_pessoa_fisica_nr_cpf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tb_pessoa_fisica',
        ),
    ]
