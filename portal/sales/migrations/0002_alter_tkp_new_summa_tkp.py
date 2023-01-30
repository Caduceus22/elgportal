# Generated by Django 4.1.5 on 2023-01-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tkp_new',
            name='summa_tkp',
            field=models.DecimalField(decimal_places=2, default=0, help_text='указывать сумму в рублях с НДС', max_digits=19, verbose_name='Сумма ТКП'),
        ),
    ]
