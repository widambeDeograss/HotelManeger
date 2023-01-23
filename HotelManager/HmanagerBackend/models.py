from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate


class User(AbstractUser):
    USERNAME_FIELD = 'username'


def upload_path(instance, static):
    return 'images/{filename}'.format(filename=static)


class RoomType(models.Model):
    room_type_id = models.IntegerField(primary_key=True)
    room_type_name = models.CharField(max_length=25)
    room_type_desc = models.CharField(max_length=250)
    room_type_pic = models.ImageField(blank=True, null=True, upload_to=upload_path)
    room_type_size = models.CharField(max_length=20)
    room_type_maxoc = models.IntegerField()
    room_type_cost = models.IntegerField()


class Status(models.Model):
    statusid = models.IntegerField()
    status = models.CharField(max_length=20)


class Reservation(models.Model):
    client_name = models.CharField(max_length=300, default='name')
    client_email = models.EmailField()
    client_phone = models.IntegerField()
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    client_checkin = models.DateField()
    client_checkout = models.DateField()
    no_of_adults = models.IntegerField(default=1)
    no_of_children = models.IntegerField(default=0)
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)

    # objects = models.Manager()


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type_id = models.ForeignKey(RoomType, related_name='rooms',on_delete=models.CASCADE)
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=300, default='widambe')
    client_phone = models.IntegerField()
    client_email = models.EmailField()
    checkin = models.DateField()
    checkout = models.DateField()
    no_of_guests = models.IntegerField()
    no_of_children = models.IntegerField()
    room_payment = models.IntegerField(default=200000)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=200)
    blog_post = models.ImageField()
    blog_subtitle = models.CharField(max_length=200)
    blog_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField()
    blog_likes = models.IntegerField()


class BlogComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog,related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_owner = models.CharField(max_length=60)


class Suggestions(models.Model):
    suggestion_id = models.IntegerField()
    client_email = models.EmailField()
    suggestion = models.TextField()
