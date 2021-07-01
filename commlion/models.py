from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Uni(models.Model):
    uni_num = models.IntegerField(primary_key=True)
    uni_name = models.CharField(max_length = 20)
    def __str__ (self): return self.uni_name

class Student(models.Model):
    student_id = models.CharField(primary_key=True,max_length = 20)
    student_password = models.CharField(max_length = 20)
    # 추후에 변경
    student_name = models.CharField(max_length = 20)
    student_generation = models.CharField(max_length = 3)

    uni_num = ForeignKey("Uni", on_delete=models.CASCADE, db_column="uni_num")
    # related_name은 외부에서의 관계를 정의함
    def __str__ (self): return self.student_name

class NoticePost(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    student_id = ForeignKey("Student", on_delete=models.CASCADE, db_column="student_id")
    # 소속 학교, 기수, 이름 불러올 때 사용

    def __str__ (self): return self.title

class SessionPost(models.Model):
    # 기본키(pk)는 장고 기본 id 사용
    session_year = models.IntegerField()
    session_num = models.IntegerField()
    session_title = models.CharField(max_length = 30)
    session_file = models.FileField(upload_to="pdf", null=True, blank=True)
    session_content = models.TextField()

    student_id = ForeignKey("Student", on_delete=models.CASCADE, db_column="student_id")
    def __str__ (self): return self.session_title


class QnaPost(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    hashtag1 = models.CharField(max_length = 15)
    hashtag2 =  models.CharField(max_length = 15)
    file = models.ImageField(upload_to="QnaImage/", null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    state = IntegerField(default=0)

    session_id = ForeignKey("SessionPost", on_delete=models.CASCADE, db_column="session_id")
    def __str__ (self): return self.title

class Comment(models.Model):
    answer = models.TextField()
    file = models.FileField(upload_to="QnaImage/", null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    like_num = IntegerField(default=0)

    qna_id = ForeignKey("QnaPost", on_delete=models.CASCADE, db_column="qna_id")
    student_id = ForeignKey("Student", on_delete=models.CASCADE, db_column="student_id")
    def __str__ (self): return self.answer[:20]

class ProjectPost(models.Model):
    file = models.ImageField(upload_to="ProjectImage/", null=True, blank=True)
    title = models.CharField(max_length = 30)
    introduction = models.TextField()
    developer = models.TextField()
    dev_period = models.CharField(max_length = 30)
    dev_stack = models.CharField(max_length = 50)
    ref = models.TextField()
    state = IntegerField(default=0)

    uni_num = ForeignKey("Uni", on_delete=models.CASCADE, db_column="uni_num")

    def __str__ (self): return (self.title + self.introduction[:20])