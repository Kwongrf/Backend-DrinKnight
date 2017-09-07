from django.db import models

# Create your models here.


class User(models.Model):
    account = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=32)
    userName = models.CharField(max_length=32 , default= account)
    phoneNumber = models.CharField(max_length=11,null=True)
    emailAddress = models.CharField(max_length=32,null=True)
    height = models.FloatField(null=True)
    wight = models.FloatField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=5,null=True)
    registerTime = models.DateTimeField( auto_now_add =True,null=True)

    def __unicode__(self): #python2
    #def __str__(self):  #python3
        return self.account
    def toDict(self):
        return {u'account':self.account,u'password':self.password,u'userName':self.userName,
                u'phoneNumber':self.phoneNumber,u'emailAddress':self.emailAddress,u'height':self.height,
                u'weight':self.wight,u'age':self.age,u'gender':self.gender,
                u'registerTime':self.registerTime.strftime('%Y-%m-%d %H:%M:%S')}

class DrinkData(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=30,default='USER')
    time = models.DateTimeField(auto_now=True)
    dose = models.FloatField(default='0')
    def toDict(self):
        return {u'account':self.account,u'time':self.time.strftime('%Y-%m-%d %H:%M:%S'),u'dose':self.dose}

class DayDrinkData(models.Model):
    account = models.CharField(max_length=30,primary_key=True)
    date = models.DateField(auto_now_add=True)
    volume_dose = models.FloatField(default='0')
    def toDict(self):
        return {u'account':self.account,u'date':self.date.strftime('%Y-%m-%d'),u'dose':self.volume_dose}

class MonthDrinkData(models.Model):
    account = models.CharField(max_length=30,primary_key=True)
    month = models.DateField()
    volume_dose = models.FloatField(default='0')
    def toDict(self):
        return {u'account':self.account,u'month':self.month.strftime('%Y-%m'),u'volume_dose':self.volume_dose}

class YearDrinkData(models.Model):
    account = models.CharField(max_length=30,primary_key=True)
    year = models.DateField()
    volume_dose = models.FloatField(default='0')
    def toDict(self):
        return {u'account':self.account,u'year':self.year.strftime('%Y'),u'volume_dose':self.volume_dose}