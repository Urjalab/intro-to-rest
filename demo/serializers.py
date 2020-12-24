from rest_framework import serializers
from .models import Post

class PostSerialzer(serializers.ModelSerializer):


    class Meta:

        model = Post
        fields = (
            'name',
            'is_student',
            'description',
            'created',
            'modified',
        )

        read_only_fields = (
            'created',
            'modified',
        )
