from django.db import models

# Create your models here.

# Question Model
class Question(models.Model):
    # 질문의 제목
    subject = models.CharField(max_length=200)
    # 질문의 내용
    content = models.TextField()
    # 작성일시
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# Answer Model
class Answer(models.Model):
    # 질문
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변의 내용
    content = models.TextField()
    # 답변을 작성한 일시
    create_date = models.DateTimeField()