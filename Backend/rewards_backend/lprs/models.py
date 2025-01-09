# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Users(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)
    username = models.CharField(db_column='Username', max_length=100)
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)
    passwordhash = models.CharField(db_column='PasswordHash', max_length=255)
    firstname = models.CharField(db_column='Firstname', max_length=100)
    lastname = models.CharField(db_column='Lastname', max_length=100)
    role = models.CharField(db_column='Role', max_length=50)
    points = models.IntegerField(db_column='Points', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class Products(models.Model):
    product_id = models.AutoField(db_column='Product_ID', primary_key=True)
    productname = models.CharField(db_column='ProductName', max_length=25)
    image = models.CharField(db_column='Image', max_length=500, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    sustainability_level = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'products'

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    date_submitted = models.DateField()
    product = models.ForeignKey('Products', on_delete=models.CASCADE, blank=True, null=True)
    service_rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    sustainability_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'

class Surveys(models.Model):
    survey_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveys'

class Surveyresponses(models.Model):
    response_id = models.AutoField(primary_key=True)
    survey = models.ForeignKey('Surveys', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    response_date = models.DateField()
    content = models.TextField(blank=True, null=True)
    initiative_engagement = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    points_earned = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveyresponses'

class Rewards(models.Model):
    reward_id = models.AutoField(db_column='Reward_ID', primary_key=True)
    points = models.IntegerField(db_column='Points')
    start = models.DateTimeField(db_column='Start', auto_now_add=True)
    end = models.DateTimeField(db_column='End', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='Image', max_length=500, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rewards'

class Percentdiscountreward(models.Model):
    reward = models.OneToOneField('Rewards', on_delete=models.CASCADE, db_column='Reward_ID', primary_key=True)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='Product_ID')
    percent = models.DecimalField(db_column='Percent', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'percentdiscountreward'

class Pricediscountreward(models.Model):
    reward = models.OneToOneField('Rewards', on_delete=models.CASCADE, db_column='Reward_ID', primary_key=True)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='Product_ID')
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pricediscountreward'

class Productupgradereward(models.Model):
    reward = models.OneToOneField('Rewards', on_delete=models.CASCADE, db_column='Reward_ID', primary_key=True)
    prevproduct = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='PrevProduct_ID')
    nextproduct = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='NextProduct_ID')

    class Meta:
        managed = False
        db_table = 'productupgradereward'

class Exclusiveproductreward(models.Model):
    reward = models.OneToOneField('Rewards', on_delete=models.CASCADE, db_column='Reward_ID', primary_key=True)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='Product_ID')

    class Meta:
        managed = False
        db_table = 'exclusiveproductreward'

class Rewardtransaction(models.Model):
    transaction_id = models.AutoField(db_column='Transaction_ID', primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='User_ID')
    reward = models.ForeignKey('Rewards', on_delete=models.CASCADE, db_column='Reward_ID')
    date = models.DateTimeField(db_column='Date', auto_now_add=True)
    active = models.IntegerField(db_column='Active', default=1)

    class Meta:
        managed = False
        db_table = 'rewardtransaction'

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    survey = models.ForeignKey('Surveys', on_delete=models.CASCADE)
    client_engagement_score = models.FloatField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    sustainability_engagement = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics'

class ClientEngagement(models.Model):
    engagement_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    participation_type = models.CharField(max_length=19, blank=True, null=True)
    participation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_engagement'

class SupportTickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    ticket_status = models.CharField(max_length=15, blank=True, null=True)
    ticket_start_date = models.DateField(blank=True, null=True)
    ticket_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_tickets'

class SupportPerformance(models.Model):
    ticket = models.OneToOneField('SupportTickets', on_delete=models.CASCADE, primary_key=True)
    response_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    resolution_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    resolution_effectiveness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    customer_satisfaction = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_performance'

class ProgramSuccess(models.Model):
    program_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    loyalty_effectiveness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    engagement_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    evaluation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_success'

class AdminAccess(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    access_time = models.DateTimeField(blank=True, null=True)
    report_type = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_access'

class CustomerStats(models.Model):
    user = models.OneToOneField('Users', on_delete=models.CASCADE, primary_key=True)
    loyalty_points = models.IntegerField(blank=True, null=True)
    reward_transactions = models.IntegerField(blank=True, null=True)
    product_purchases = models.IntegerField(blank=True, null=True)
    initiative_points = models.IntegerField(blank=True, null=True)
    campaign_points = models.IntegerField(blank=True, null=True)
    survey_points = models.IntegerField(blank=True, null=True)
    education_engagement = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_stats'
