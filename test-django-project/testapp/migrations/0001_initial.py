# Generated by Django 2.1.7 on 2019-03-09 21:34

from django.db import migrations, models
import django.db.models.deletion
import django_models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_models', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTestModel',
            fields=[
                ('id', django_models.fields.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(default='example@example.com', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestDigitsOnlyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digits_only_field', django_models.fields.CharFieldDigitsOnly(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TestHistoryFail',
            fields=[
                ('historymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_models.HistoryModel')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_models.historymodel',),
        ),
        migrations.CreateModel(
            name='TestHistoryModel',
            fields=[
                ('historymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_models.HistoryModel')),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(default='example@example.com', max_length=32)),
                ('description', models.CharField(blank=True, default='Lorem Ipsum', max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_models.historymodel', models.Model),
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('id', django_models.fields.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestSignalsModel',
            fields=[
                ('id', django_models.fields.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='historytestmodel',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='testapp.TestHistoryModel'),
        ),
    ]
