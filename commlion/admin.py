from django.contrib import admin
from .models import Uni, Student, NoticePost, SessionPost, QnaPost, Comment, ProjectPost

# Register your models here.


class UniAdmin(admin.ModelAdmin):
    pass


admin.site.register(Uni, UniAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class NoticePostAdmin(admin.ModelAdmin):
    pass


admin.site.register(NoticePost, NoticePostAdmin)


class SessionPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(SessionPost, SessionPostAdmin)


class QnaPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(QnaPost, QnaPostAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)


class ProjectPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectPost, ProjectPostAdmin)
