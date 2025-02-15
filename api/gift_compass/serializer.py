from rest_framework import serializers
from .models import Test, Page, Content, Choice, Answer, SelectedChoice

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class SelectedChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedChoice
        fields = ['order', 'value']

class AnswerSerializer(serializers.ModelSerializer):
    selected_choice = SelectedChoiceSerializer(many=True)

    class Meta:
        model = Answer
        fields = ['owner', 'respondent_name', 'selected_choice']

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

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        content = Content.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(content=content, **choice_data)
        return content

class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['uuid', 'title', 'template_id', 'contents']

    def create(self, validated_data):
        contents_data = validated_data.pop('contents')
        page = Page.objects.create(**validated_data)
        for content_data in contents_data:
            Content.objects.create(page=page, **content_data)
        return page