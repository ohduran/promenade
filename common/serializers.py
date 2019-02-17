from rest_framework import serializers

from .models import Bot


class BotSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = Bot
        fields = ('username', 'password')


class SetRelationshipBoundsSerializer(serializers.Serializer):

    enabled = serializers.BooleanField(default=False)
    potency_ratio = serializers.DecimalField(max_digits=4, decimal_places=2,
                                             required=False)
    delimit_by_user = serializers.BooleanField(default=False)

    min_posts = serializers.IntegerField(required=False)
    max_posts = serializers.IntegerField(required=False)

    min_followers = serializers.IntegerField(required=False)
    max_followers = serializers.IntegerField(required=False)

    min_following = serializers.IntegerField(required=False)
    max_following = serializers.IntegerField(required=False)


class RelationshipBounded:

    relationship_bound = SetRelationshipBoundsSerializer()


class SessionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)