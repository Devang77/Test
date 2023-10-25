from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
class Member(models.Model):
    name = models.CharField(max_length=100)
    outstanding_debt = models.FloatField(default=0)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
   
