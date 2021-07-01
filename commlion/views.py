from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timezone
from datetime import time
from .models import NoticePost, SessionPost, Student, ProjectPost, Uni

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def noticeMain(request):
    notices = NoticePost.objects.all()
    return render(request, 'notice-main.html', {'notices': notices})


def sessionMain(request):
    session = SessionPost.objects.get(id=1)
    return render(request, 'session-main.html', {'session': session})


def qnaMain(request):
    return render(request, 'qna-main.html')


def qnaDetail(request):
    return render(request, 'qna-detail.html')


def qnaWrite(request):
    if request.method == 'POST':
        qnaPost = QnaPost()
        qnaPost.session_title = request.POST['title']
        qnaPost.session_content = request.POST['content']
        qnaPost.session_hashtag1 = request.POST['hashtag1']
        qnaPost.session_hashtag2 = request.POST['hashtag2']
        qnaPost.session_file = request.FILES['img']
        qnaPost.pub_date = timezone.datetime.now()
        qnaPost.state = 0
        qnaPost.session_id = SessionPost.objects.get(id=0)
        qnaPost.save()

        return redirect('sessionMain')
    else:
        return render(request, 'qna-write.html')


def projectMain(request):
    return render(request, 'project-main.html')


def projectDetail(request):
    return render(request, 'project-detail.html')


def sessionWrite(request):
    if request.method == 'POST':
        sessionPost = SessionPost()
        sessionPost.session_num = 0
        sessionPost.session_year = 0
        sessionPost.session_content = request.POST['content']
        sessionPost.session_title = request.POST['title']
        sessionPost.session_file = request.FILES['img']
        sessionPost.student_id = Student.objects.get(student_id=0)
        sessionPost.save()

        return redirect('sessionMain')
    else:
        return render(request, 'session-write.html')


def noticeWrite(request):
    if request.method == 'POST':
        noticePost = NoticePost()
        noticePost.content = request.POST['content']
        noticePost.title = request.POST['title']
        noticePost.pub_date = timezone.datetime.now()
        noticePost.student_id = Student.objects.get(student_id=0)
        # 아이디값 변경
        noticePost.save()

        return redirect('noticeMain')
    else:
        return render(request, 'notice-write.html')


def projectWrite(request):
    if request.method == 'POST':
        projectPost = ProjectPost()
        projectPost.file = request.POST['img']
        projectPost.title = request.POST['title']
        projectPost.introduction = request.POST['introduction']
        projectPost.developer = request.POST['developer']
        projectPost.dev_period = request.POST['dev_period']
        projectPost.dev_stack = request.POST['dev_stack']
        projectPost.ref = request.POST['ref']
        projectPost.state = request.POST['state']
        projectPost.uni_num = Uni.objects.get(uni_num=0)
        # 아이디값 변경
        projectPost.save()

        return redirect('projectMain')
    else:
        return render(request, 'Project-write.html')
