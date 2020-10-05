# Generated by Django 3.1.1 on 2020-10-05 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201005_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=240)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.postmodel')),
            ],
        ),
    ]