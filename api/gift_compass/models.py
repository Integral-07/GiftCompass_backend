from django.db import models
from django.contrib.auth.models import User
import uuid

class Test(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "test"
        verbose_name = "テスト"


class Page(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    template_id = models.IntegerField()
    title = models.CharField(max_length=100, default="Untitled page", verbose_name="ページタイトル")
    published = models.DateTimeField(auto_now_add=True)


class Content(models.Model):

    owner = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='contents')
    number = models.IntegerField()
    question = models.TextField()


class Choice(models.Model):

    owner = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='choices')
    number = models.IntegerField()
    text = models.CharField(max_length=200)


class Answer(models.Model):

    owner = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='answer')
    respondent_name = models.CharField(max_length=100, default="anony")


class SelectedChoice(models.Model):

    owner = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="selected_choice")
    order = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
