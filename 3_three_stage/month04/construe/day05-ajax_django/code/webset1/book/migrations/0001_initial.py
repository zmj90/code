# Generated by Django 2.2.12 on 2020-05-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='书名')),
                ('describe', models.CharField(max_length=300, verbose_name='描述')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='单价')),
                ('picture', models.ImageField(default=None, upload_to='', verbose_name='图片')),
                ('publisher_date', models.DateField(verbose_name='出版时间')),
            ],
        ),
    ]
