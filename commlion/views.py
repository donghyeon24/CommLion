from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timezone
from datetime import time
from .models import NoticePost, QnaPost, SessionPost, Student, ProjectPost, Uni

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def noticeMain(request):
    notices = NoticePost.objects.all()
    return render(request, 'notice-main.html', {'notices': notices})


def sessionMain(request, session_num):
    exist_session = SessionPost.objects.filter(session_num=session_num)
    if exist_session.exists():
        session = SessionPost.objects.get(session_num=session_num)
        return render(request, 'session-main.html', {'session': session})
    else:
        return redirect('sessionWrite', session_num)


def qnaMain(request, session_num):
    exist_session = SessionPost.objects.filter(session_num=session_num)
    if exist_session.exists():
        session = SessionPost.objects.get(session_num=session_num)
        qnas = QnaPost.objects.filter(session_id=session)
        return render(request, 'qna-main.html', {'qnas': qnas, 'session':session})
    else:
        return redirect('qnaWrite', session_num)


def qnaDetail(request, qna_id):
    exist_qna = QnaPost.objects.filter(id=qna_id)
    if exist_qna.exists():
        qna = QnaPost.objects.get(id=qna_id)
        return render(request, 'qna-detail.html',{'qna':qna})
    else:
        return redirect('qnaMain', 10)
    

def qnaWrite(request, session_num):
    if request.method == 'POST':
        qnaPost = QnaPost()
        qnaPost.title = request.POST['title']
        qnaPost.content = request.POST['content']
        qnaPost.hashtag1 = request.POST['hashtag1']
        qnaPost.hashtag2 = request.POST['hashtag2']
        qnaPost.file = request.FILES['img']
        qnaPost.pub_date = timezone.datetime.now()
        qnaPost.state = 0
        qnaPost.session_id = SessionPost.objects.get(session_num=session_num)
        qnaPost.save()

        return redirect('qnaMain',session_num)
    else:
        return render(request, 'qna-write.html')


def projectMain(request):
    return render(request, 'project-main.html')


def projectDetail(request):
    return render(request, 'project-detail.html')


def sessionWrite(request, session_num):
    if request.method == 'POST':
        sessionPost = SessionPost()
        sessionPost.session_num = session_num
        sessionPost.session_year = 2021
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

        return redirect('noticeMain')
    else:
        return render(request, 'notice-write.html')


def projectWrite(request):
    if request.method == 'POST':
        projectPost = ProjectPost()
        if request.FILES.get('img') is not None:
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
