# Generated by Django 5.0.1 on 2024-02-14 10:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=10000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('is_premium', models.BooleanField(default=False, verbose_name='Is this a premim article?')),
                ('user', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
