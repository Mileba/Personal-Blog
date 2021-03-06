# Generated by Django 4.0.4 on 2022-06-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='caption',
        ),
        migrations.AddField(
            model_name='tag',
            name='caption',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
