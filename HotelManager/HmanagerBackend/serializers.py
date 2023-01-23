from rest_framework import serializers
from .models import User, RoomType, Reservation, Room, Booking, Blog, BlogComment, Status, Suggestions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = self.validated_data['email']
        password = self.validated_data['password']
        username = self.validated_data['username']
        user = User.objects.create_user(username=username,email=email,password=password)
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number','room_type_id', 'statusid')


class RoomTypeSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = RoomType
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'


class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'
