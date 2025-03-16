from django.db import models
from django.core.validators import EmailValidator
from django.db.models import Q
from django.db.models.constraints import CheckConstraint
from django.core.exceptions import ValidationError
# Create your models here.

def positive_validator(value):
    if value <= 0:
        raise ValidationError('Value must be positive')

#會員檔
class member(models.Model):
    memberID=models.AutoField(primary_key=True)
    memberclass=models.CharField(max_length=4,null=False)
    memberLine=models.CharField(max_length=20)
    memberFB=models.CharField(max_length=20)
    memberName=models.CharField(max_length=20)
    memberTel=models.IntegerField(default="")
    memberEmail=models.CharField(max_length=100, validators=[EmailValidator])#符合email格式
    #Line or FB不能同時為空
    class Meta:
        constraints = [
            CheckConstraint(
            check=Q(memberLine__isnull=False) | Q(memberFB__isnull=False),
            name='memberLine_or_memberFB'
            )
        ]

#旅程檔
class travel(models.Model):
    travelID=models.AutoField(primary_key=True)
    memberID=models.ForeignKey(member, on_delete=models.CASCADE)
    travelDate=models.CharField(max_length=10)
    travelState=models.IntegerField(default="",validators=[positive_validator])
    travelPrice=models.IntegerField(default="15000元")

#圓之家菜單
class Bmenu(models.Model):
    BmenuID=models.AutoField(primary_key=True)
    BmenuName=models.CharField(max_length=20)
    Bmenuclass=models.IntegerField(default="",validators=[positive_validator])
    BmenuPrice=models.IntegerField(default="",validators=[positive_validator])
    BmenuState=models.IntegerField(default="1",validators=[positive_validator])
    #兩個欄位的組合不能重複
    class Meta:
        unique_together = ('BmenuID','BmenuName')

#孔之家菜單
class Dmenu(models.Model):
    DmenuID=models.AutoField(primary_key=True)
    DmenuName=models.CharField(max_length=20)
    Dmenuclass=models.IntegerField(default="",validators=[positive_validator])
    DmenuPrice=models.IntegerField(default="",validators=[positive_validator])
    DmenuState=models.IntegerField(default="1",validators=[positive_validator])
    #兩個欄位的組合不能重複
    class Meta:
        unique_together = ('DmenuID','DmenuName')

#早餐檔
class breakfast(models.Model):
    breakfastID=models.AutoField(primary_key=True)
    breakfasttravel=models.ForeignKey(travel, on_delete=models.CASCADE)
    breakfastOrder=models.ForeignKey(Bmenu, on_delete=models.CASCADE)
    breakfastNum=models.IntegerField(default="1",validators=[positive_validator])
    breakfastPrice=models.IntegerField(default="",validators=[positive_validator])

#晚餐檔
class Dinner(models.Model):
    DinnerID=models.AutoField(primary_key=True)
    Dinnertravel=models.ForeignKey(travel, on_delete=models.CASCADE)
    DinnerOrder=models.ForeignKey(Dmenu, on_delete=models.CASCADE)
    DinnerNum=models.IntegerField(default="1",validators=[positive_validator])
    DinnerPrice=models.IntegerField(default="",validators=[positive_validator])

#參加人員檔
class Join(models.Model):
    JoinID=models.AutoField(primary_key=True)
    JoinName=models.CharField(max_length=10)
    JoinCard=models.CharField(max_length=10,null=False)
    JoinInsurance=models.IntegerField(default="0",validators=[positive_validator])