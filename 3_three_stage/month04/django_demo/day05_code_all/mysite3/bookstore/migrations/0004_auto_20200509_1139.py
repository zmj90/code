# Generated by Django 2.2.12 on 2020-05-09 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20200509_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='姓名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='零售价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=50, verbose_name='出版社'),
        ),
    ]
