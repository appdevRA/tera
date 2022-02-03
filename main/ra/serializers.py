from rest_framework import serializers

from .models import Bookmark, Bookmark_detail, Folder, Group, User

class FolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class BookmarkDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark_detail
        fields = "__all__"




class BookmarkModelSerializer(serializers.ModelSerializer):
    details = BookmarkDetailModelSerializer(source="bookmark", read_only=True)

    class Meta:
        model = Bookmark
        exclude = ("bookmark",)

class FolderRetrieveModelSerializer(FolderModelSerializer):
    bookmark_folders = BookmarkModelSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = "__all__"




class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "department",
        )


# request serializers
class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ChangePasswordRequestSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Passwords do not match.")

        return attrs


class AddToGroupRequestSerializer(serializers.Serializer):
    group_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)


# query serializers
class UserQueryMixinSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)


class BookmarkQuerySerializer(UserQueryMixinSerializer):
    favorite = serializers.BooleanField(required=False, allow_null=True, default=None)
    removed = serializers.BooleanField(required=False, allow_null=True, default=None)
    recently_added = serializers.BooleanField(required=False, default=False)
    recently_read = serializers.BooleanField(required=False, default=False)
    folder = serializers.IntegerField(required=False)
    group = serializers.IntegerField(required=False)
    groups_only = serializers.BooleanField(
        required=False, 
        allow_null=True, 
        default=None
        )

class GroupQuerySerializer(serializers.Serializer):
    for_user = serializers.IntegerField(required=False)
    available_for_bookmark_detail = serializers.IntegerField(required=False)


class FolderQuerySerializer(UserQueryMixinSerializer):
    pass