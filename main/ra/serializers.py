from rest_framework import serializers

from .models import Folder, User_bookmark


class FolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class UserBookmarkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_bookmark
        fields = "__all__"


class FolderRetrieveModelSerializer(FolderModelSerializer):
    bookmark_folders = UserBookmarkModelSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = "__all__"


# query serializers
class UserBookmarkQuerySerializer(serializers.Serializer):
    favorite = serializers.BooleanField(required=False, allow_null=True, default=None)
    removed = serializers.BooleanField(required=False, allow_null=True, default=None)
    recently_added = serializers.BooleanField(required=False, default=False)
    recently_read = serializers.BooleanField(required=False, default=False)
    folder = serializers.IntegerField(required=False)
