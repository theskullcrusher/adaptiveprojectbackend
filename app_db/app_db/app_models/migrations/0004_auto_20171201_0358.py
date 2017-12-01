# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0003_cards_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='app_models.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='GroupsCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='app_models.CardGroups')),
                ('user', models.ForeignKey(to='app_models.AppUser')),
            ],
        ),
        migrations.AddField(
            model_name='cards',
            name='in_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groupscard',
            name='card',
            field=models.ForeignKey(to='app_models.Cards'),
        ),
        migrations.AddField(
            model_name='groupscard',
            name='group',
            field=models.ForeignKey(to='app_models.CardGroups'),
        ),
    ]
