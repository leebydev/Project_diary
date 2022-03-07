from django.db import models
from django.conf import settings

# class명이 Board이면 만들어지는 실제 table이름은 bbs_board이 되요!
# class는 반드시 장고가 제공하는 class를 상속받아서 만들어야 해요!
# Database Table이 가지고 있는 각각의 column을
# class의 class variable을 이용해서 define.

# 클래스를 이용해서 Table을 생성하면 자동으로 id column이 하나
# 생성되요. id column은 Integer, PK, AUTO_INCREMENT


class Board(models.Model):
    b_title = models.CharField(max_length=50)  # 글 제목
    b_author = models.CharField(max_length=20)  # 글 작성자
    b_content = models.CharField(max_length=200)  # 글 내용
    b_date = models.DateTimeField(auto_now=True)  # 글 작성시간
    # auto_now=True => 현재시간이 자동으로 삽입
    b_comment_count = models.IntegerField(default=0)  # 댓글 개수
    b_like_count = models.IntegerField(default=0)  # 좋아요 개수
    b_img = models.ImageField(upload_to=settings.MEDIA_ROOT,
                                blank=True,
                                null=True)
    b_map = models.CharField(max_length=50)

    def __str__(self):
        return self.b_title


class Comment(models.Model):
    c_author = models.CharField(max_length=20)  # 댓글 작성자
    c_content = models.CharField(max_length=100)  # 댓글 내용
    # board라는 class variable은 실제 table이 생성되면
    # board_id라는 이름의 column으로 생성되고 ForeignKey로 설정되요!
    board = models.ForeignKey(Board,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.c_content

