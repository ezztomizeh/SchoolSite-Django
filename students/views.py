from django.shortcuts import render , redirect
from user.models import Messages
from home.models import Teacher , Student , Subjects
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

# Create your views here.
def StudentLoginPage(request):
    if request.method == 'POST':
        username = request.POST['StudentID']
        password = request.POST['password']
        student = User.objects.filter(username=username).first()
        student = Student.objects.filter(StudentID=student.username).first()
        user = authenticate(username = username , password = password)
        if student is not None:
            if user is not None:
                login(request,user=user)
                return redirect('StudentPannel')
            else:
                messages.error(request,'Something went wrong')
                return redirect('LoginStudentPage')
        else:
            messages.error(request,'You are not a student')
            return redirect('LoginStudentPage')
    else:
        return render(request,'LoginStudentPage.html')

@login_required
def Pannel(request):
    user = User.objects.filter(username=request.user).first()
    student = Student.objects.filter(StudentID = user.username).first()
    teacher = Teacher.objects.filter(TeacherID=student.ResposveTeacher).first()
    subjects = Subjects.objects.filter(StudentID = student.StudentID).all()
    context = {
        'user' : user,
        'student' : student,
        'subjects' : subjects,
        'teacher' : teacher
    }
    return render(request,'index.html',context)

@login_required
def SendMessage(request):
    if request.method == "POST":
        user = User.objects.filter(username = request.user).first()
        student = Student.objects.filter(StudentID=user.username).first()
        title = request.POST['title']
        content = request.POST['msg']
        reciver = request.POST['Reciver']
        sender = student.StudentID
        msg = Messages.objects.create(Msg_title=title,Msg_content=content,
                                      Msg_reciver=reciver,Msg_sender=sender)
        msg.save()
        messages.success(request,'Message Sent Seccessfully')
        return redirect('SendMessage')
    else:
        user = User.objects.filter(username = request.user).first()
        student = Student.objects.filter(StudentID=user.username).first()
        teacher = Teacher.objects.filter(TeacherID=student.ResposveTeacher).first()
        context = {
            'student' : student,
            'teacher' : teacher
        }
        return render(request,'SendMessage.html',context)

@login_required
def MessageSent(request):
    user = User.objects.filter(username = request.user).first()
    student = Student.objects.filter(StudentID=user.username).first()
    msgs = Messages.objects.filter(Msg_sender=student.StudentID).all()
    context = {
        'msgs' : msgs
    }
    return render(request,'Messages.html',context)

@login_required
def Outbox1(request):
    user = User.objects.filter(username=request.user).first()
    student = Student.objects.filter(StudentID=user.username).first()
    teacher = Teacher.objects.filter(TeacherID=student.ResposveTeacher).first()
    msgs = Messages.objects.filter(Msg_reciver=student.StudentID).all()
    context = {
        'teacher' : teacher,
        'Msgs' : msgs
    }
    return render(request,'InboxStudent.html',context=context)

@login_required
def Reply(request,MsgID,TeacherID):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user).first()
        student = Student.objects.filter(StudentID=user.username).first()
        teacher = Teacher.objects.filter(TeacherID=TeacherID).first()
        title = request.POST['title']
        reciver = request.POST['Reciver']
        sender = student.StudentID
        content = request.POST['msg']
        msg = Messages.objects.create(Msg_title=title,Msg_content=content,
                                      Msg_sender=sender,Msg_reciver=reciver)
        msg.save()
        messages.success(request,'Reply sent successfully')
        return redirect('inbox')
    else:
        user = User.objects.filter(username=request.user).first()
        student = Student.objects.filter(StudentID=user.username).first()
        teacher = Teacher.objects.filter(TeacherID=TeacherID).first()
        if student.ResposveTeacher == teacher.TeacherID:
            msg = Messages.objects.filter(id = MsgID).first()
            context = {
                'teacher' : teacher,
                'msg' : msg
            }
            return render(request,'Reply.html',context)
        else:
            messages.error(request,'You can not reply on this message')
            return redirect('inbox')