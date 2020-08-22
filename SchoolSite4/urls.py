"""SchoolSite4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from user import views as user_view
from students import views as student_view
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('StaffLogin/',user_view.TeacherLoignPage,name="LoginTeacherPage"),
    path('StudentLogin/',student_view.StudentLoginPage,name="LoginStudentPage"),
    path('Panel/',user_view.Panel,name="PanelPage"),
    path('Logout/',user_view.Logout,name = "Logout"),
    path('Pannel/AddSubject',user_view.AddSubjects,name = "AddSubjects"),
    path('Pannel/Search',user_view.Search,name = "Search"),
    path('Pannel/UpdateSubject/<str:StudentID>/<str:SubjectID>',user_view.UpdateSubject,name = "Update"),
    path('Pannel/SearchStudent',user_view.SearchStudent,name = "Search1"),
    path('Pannel/Student/<str:StudentID>',user_view.StudentPage,name = "StudentPage"),
    path('Pannel/Student/<str:StudentID>/Update',user_view.UpdateStudentINFO,name = "UpdateStudent"),
    path('Pannel/Inbox/',user_view.Inbox,name = "inboxTeacher"),
    path('Pannel/SendMessage/',user_view.SendMessage,name = "SendMsg"),
    path('Pannel/Outbox/',user_view.Outbox,name = "TeacherOutbox"),
    path('Pannel/SendMessage/All',user_view.ForEverone,name = "SendMsgAll"),
    path('StudentPannel/',student_view.Pannel,name = "StudentPannel"),
    path('StudentPannel/SendMessage',student_view.SendMessage,name = "SendMessage"),
    path('StudentPannel/Outbox',student_view.MessageSent,name = "outbox"),
    path('StudentPannel/Inbox',student_view.Outbox1,name = "inbox"),
    path('StudentPannel/Reply/<int:MsgID>/<str:TeacherID>',student_view.Reply,name = "reply"),
]
