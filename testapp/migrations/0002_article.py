# Generated by Django 3.0.14 on 2024-12-10 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testapp.Rubric')),
            ],
        ),
    ]
