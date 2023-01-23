from django.contrib import admin
from .models import User,RoomType,Status,Reservation,Room,Blog,BlogComment,Booking,Suggestions

# Register your models here.
admin.site.register(User)
admin.site.register(Status)
admin.site.register(RoomType)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Suggestions)