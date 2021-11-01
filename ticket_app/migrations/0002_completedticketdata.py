# Generated by Django 3.2.4 on 2021-11-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTicketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('tower', models.CharField(max_length=200)),
                ('dc', models.CharField(max_length=200)),
                ('action_item', models.CharField(max_length=1000)),
                ('severity', models.CharField(max_length=200)),
                ('action_history', models.CharField(max_length=1000)),
                ('owner', models.CharField(max_length=100)),
                ('eta', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Completed_ticket_data',
            },
        ),
    ]
