from rest_framework import serializers
from .models import Test, Page, Content, Choice

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['uuid', 'title', 'published']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['number', 'text']

class ContentSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ['number', 'question', 'choices']

class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['uuid', 'title', 'template_id', 'contents']

