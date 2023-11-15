from django.db import models

# Create your models here.
class Coach(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    class Meta:
        db_table="coaches"
class Player(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    age=models.IntegerField()
    class Meta:
        db_table="players"
class Club(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    coach=models.ForeignKey(Coach,on_delete=models.DO_NOTHING)
    players=models.ManyToManyField(Player)
    def __str__(self):
        return self.name
    class Meta:
        db_table="clubs"