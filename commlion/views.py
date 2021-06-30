from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def notice(request):
    return render(request, 'notice.html')


def session(request):
    return render(request, 'session.html')


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
    return render(request, 'session-write.html')

# def sessionWrite(request):
#   if request.method == 'POST':
#     SessionPost = SessionPost()
#     PublicPost.name = request.POST['name']
#     PublicPost.title = request.POST['title']
#     PublicPost.img = request.FILES['img']


#     PublicPost.save()
#     return render(request,"session.html")
#   else:
#     return render(request, 'session-write.html')
