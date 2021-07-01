from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime, timezone
from datetime import time
from .models import NoticePost,SessionPost, Student

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def notice(request):
    notices=NoticePost.objects.all()
    return render(request, 'notice.html',{'notices':notices})


def session(request):
    session=SessionPost.objects.get(id=1)
    return render(request, 'session.html',{'session':session})


def qnaMain(request):
    return render(request, 'qna-main.html')


def qnaDetail(request):
    return render(request, 'qna-detail.html')


def qnaWrite(request):
    return render(request, 'qna-write.html')


def projectMain(request):
    return render(request, 'project-main.html')


def projectDetail(request):
    return render(request, 'project-detail.html')


def projectWrite(request):
    return render(request, 'project-write.html')


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

    return redirect('session')
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

    return redirect('notice')
  else:
    return render(request, 'notice-write.html')


