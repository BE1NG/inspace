from django.db import models

# 사용자 DB       email 기본키로 수정해주세여
class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
<<<<<<< HEAD
    phone = models.CharField(max_length=15)
=======

# 게시글 DB
class Posting(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    picture = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
>>>>>>> 35bbd1a18bbecc1e44d0bbcfccde22673076ff52
