# Generated by Django 2.2.10 on 2021-11-21 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, verbose_name='Текст вопроса')),
                ('type', models.IntegerField(choices=[(1, 'Ответ текстом'), (2, 'Ответ с выбором одного варианта'), (3, 'Ответ с выбором нескольких вариантов')], default=1, verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Наименование опроса')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата начала опроса')),
                ('end_date', models.DateField(verbose_name='Дата окончания опроса')),
                ('description', models.TextField(max_length=255, verbose_name='Описание опроса')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField(verbose_name='Идентификатор персоны, которая дала ответ')),
                ('answer', models.TextField(max_length=255, verbose_name='Текст ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question', verbose_name='Вопрос на который был дан ответ')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Survey', verbose_name='Опрос к которому относится вопрос'),
        ),
    ]
