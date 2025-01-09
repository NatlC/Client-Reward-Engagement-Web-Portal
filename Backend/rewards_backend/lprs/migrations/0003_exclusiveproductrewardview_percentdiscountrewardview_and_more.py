# Generated by Django 4.2.16 on 2024-11-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lprs', '0002_rewardtransactionview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exclusiveproductrewardview',
            fields=[
                ('reward_id', models.AutoField(db_column='Reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points')),
                ('start', models.DateTimeField(db_column='Start')),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('productname', models.CharField(db_column='ProductName', max_length=25)),
                ('productimage', models.CharField(blank=True, db_column='ProductImage', max_length=500, null=True)),
                ('productdescription', models.TextField(blank=True, db_column='ProductDescription', null=True)),
                ('productprice', models.DecimalField(db_column='Price', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'Exclusiveproductrewardview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Percentdiscountrewardview',
            fields=[
                ('reward_id', models.AutoField(db_column='Reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points')),
                ('start', models.DateTimeField(db_column='Start')),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=500, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('percent', models.DecimalField(db_column='Percent', decimal_places=2, max_digits=10)),
                ('productname', models.CharField(db_column='ProductName', max_length=25)),
                ('productimage', models.CharField(blank=True, db_column='ProductImage', max_length=500, null=True)),
                ('productdescription', models.TextField(blank=True, db_column='ProductDescription', null=True)),
                ('productprice', models.DecimalField(db_column='Price', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'percentdiscountrewardview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pricediscountrewardview',
            fields=[
                ('reward_id', models.AutoField(db_column='Reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points')),
                ('start', models.DateTimeField(db_column='Start')),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=500, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('price', models.DecimalField(db_column='DiscountPrice', decimal_places=2, max_digits=10)),
                ('productname', models.CharField(db_column='ProductName', max_length=25)),
                ('productimage', models.CharField(blank=True, db_column='ProductImage', max_length=500, null=True)),
                ('productdescription', models.TextField(blank=True, db_column='ProductDescription', null=True)),
                ('productprice', models.DecimalField(db_column='Price', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'pricediscountrewardview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productupgraderewardview',
            fields=[
                ('reward_id', models.AutoField(db_column='Reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points')),
                ('start', models.DateTimeField(db_column='Start')),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('prevproductname', models.CharField(db_column='PrevProductName', max_length=25)),
                ('previmage', models.CharField(blank=True, db_column='PrevProductImage', max_length=500, null=True)),
                ('prevdescription', models.TextField(blank=True, db_column='PrevProductDescription', null=True)),
                ('prevprice', models.DecimalField(db_column='PrevPrice', decimal_places=2, max_digits=10)),
                ('nextproductname', models.CharField(db_column='NextProductName', max_length=25)),
                ('nextimage', models.CharField(blank=True, db_column='NextProductImage', max_length=500, null=True)),
                ('nextdescription', models.TextField(blank=True, db_column='NextProductDescription', null=True)),
                ('nextprice', models.DecimalField(db_column='NextPrice', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'Productupgraderewardview',
                'managed': False,
            },
        ),
    ]