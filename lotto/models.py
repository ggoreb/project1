from django.db import models

class Number(models.Model):
    # 게시물 제목
    title = models.CharField(max_length=30)
    # 생성된 로또번호
    lottos = models.CharField(max_length=200)
    # 로또번호 생성일자
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title
