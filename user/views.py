from django.shortcuts import render , redirect
from .models import Messages
from django.views.generic import ListView
from home.models import Teacher , Student , Subjects
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def TeacherLoignPage(request):
    if request.method == 'POST':
        username = request.POST['TeacherID']
        password = request.POST['password']
        teacher = User.objects.filter(username=username).first()
        teacher = Teacher.objects.filter(TeacherID=teacher.username).first()
        user = authenticate(username = username , password = password)
        if teacher is not None:
            if user is not None:
                login(request,user = user)
                return redirect('PanelPage')
            else:
                messages.error(request,'Something went wrong')
                return redirect('LoginTeacherPage')
        else:
            messages.error(request,'You are not a teacher')
            return redirect('LoginTeacherPage')
    else:
        return render(request,'LoginTeaherPage.html')
    
@login_required
def Panel(request):
    user = User.objects.filter(username = request.user).first()
    teacher = Teacher.objects.filter(TeacherID=user.username).first()
    students = Student.objects.filter(ResposveTeacher=teacher.TeacherID).all()
    context = {
        'user' : user,
        'teacher' : teacher,
        'students' : students
    }
    return render(request,'TeacherPanel.html',context)

@login_required
def Logout(request):
    logout(request)
    return redirect('HomePage')

@login_required
def AddSubjects(request):
    if request.method == "POST":
        StudentID = request.POST['StudentID']
        Subject = request.POST['Subject']
        TopResalt = request.POST['Top']
        LowestResalt = request.POST['low']
        FirstExam = request.POST['1st']
        SecExam = request.POST['2sec']
        thExam = request.POST['3th']
        FinalExam = request.POST['Final']
        OtherMarks = request.POST['marks']
        reusalt = float(FirstExam) + float(SecExam) + float(thExam) + float(FinalExam) + float(OtherMarks)
        if Subject == 'math':
            SubjectID = '55'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'arabic':
            SubjectID = '100'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'english 1':
            SubjectID = '101'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'english 2':
            SubjectID = '101'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'scince':
            SubjectID = '56'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'art':
            SubjectID = '12'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        elif Subject == 'music':
            SubjectID = '15'
            Subject = Subjects.objects.create(StudentID=StudentID,SubjectID=SubjectID,
                                             SubjectName=Subject,SubjectTop=TopResalt,
                                             SubjectLow=LowestResalt, FirstExam=FirstExam,
                                             SecExam=SecExam,ThExam=thExam,
                                             FinalExam=FinalExam , OtherMarks=OtherMarks,
                                             SubjectRusalt=reusalt)
        else:
            messages.error(request,'This Subject is not exsit')
            return redirect('AddSubjects')
        messages.success(request,'Subject added successfully')
        return redirect('StudentPage' , StudentID = StudentID)

        
    else:
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user.username).first()
        students = Student.objects.filter(ResposveTeacher=teacher.TeacherID).all()
        context = {
            'students' : students
        }
        return render(request,'AddSubjects.html',context)

@login_required
def Search(request):
    if request.method == "POST":
        StudentID = request.POST['StudentID']
        Subject = request.POST['Subject']
        return redirect('Update',StudentID = StudentID , SubjectID = Subject)
    else:
        return render(request,'Search.html')

def UpdateSubject(request,StudentID,SubjectID):
    if request.method == 'POST':
        StudentID = request.POST['StudentID']
        SubjectName = request.POST['SubjectName']
        TopResalt = request.POST['Top']
        LowestResalt = request.POST['low']
        FirstExam = request.POST['1st']
        SecExam = request.POST['2sec']
        thExam = request.POST['3th']
        FinalExam = request.POST['Final']
        OtherMarks = request.POST['marks']
        subject = Subjects.objects.filter(SubjectName=SubjectName,StudentID=StudentID).first()
        subject.SubjectTop = TopResalt
        subject.SubjectLow = LowestResalt
        subject.FirstExam = FirstExam
        subject.SecExam = SecExam
        subject.ThExam = thExam
        subject.FinalExam = FinalExam
        subject.OtherMarks = OtherMarks
        subject.SubjectRusalt = float(FirstExam) + float(SecExam) + float(thExam) + float(FinalExam) + float(OtherMarks)
        subject.save()
        messages.success(request,'Subject updated successfully')
        return redirect('StudentPage',StudentID=StudentID)
    else:
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user.username).first()
        student = Student.objects.filter(StudentID=StudentID).first()
        if teacher.TeacherID == student.ResposveTeacher:
            subjects = Subjects.objects.filter(SubjectID=SubjectID,StudentID=StudentID).first()
            context = {
                'subject' : subjects
            }
            return render(request,'UpdateSubject.html',context)
        else:
            return redirect('Search')

@login_required
def SearchStudent(request):
    if request.method == "POST":
        StudentID = request.POST['StudentID']
        return redirect('StudentPage',StudentID = StudentID)
    else:
        return render(request,'Search1.html')

@login_required
def StudentPage(request,StudentID):
    user = User.objects.filter(username = request.user).first()
    teacher = Teacher.objects.filter(TeacherID=user.username).first()
    student = Student.objects.filter(StudentID=StudentID).first()
    if teacher.TeacherID == student.ResposveTeacher:
        subjects = Subjects.objects.filter(StudentID=StudentID).all()  
        context = {
            'student' : student,
            'subjects' : subjects
        }
        return render(request,'StudentPage.html',context)
    else:
        messages.success(request,'Student not yours')
        return redirect('Search')

@login_required
def UpdateStudentINFO(request,StudentID):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user.username).first()
        student = Student.objects.filter(ResposveTeacher=teacher.TeacherID).first()
        if teacher.TeacherID == student.ResposveTeacher:
            resalt = request.POST['resalt']
            total = request.POST['Total']
            student.StudentTotal = total
            student.StudentRusalt = resalt
            student.save()
            messages.success(request,'Info updated successfully')
            return redirect('StudentPage',StudentID = StudentID)
        else:
            messages.error(request,'This is not your student')
            return redirect('PannelPage')
    else:
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user.username).first()
        student = Student.objects.filter(ResposveTeacher=teacher.TeacherID).first()
        if teacher.TeacherID == student.ResposveTeacher:
            context = {
                'teacher' : teacher,
                'student' : student
            }
            return render(request,'UpdateStudent.html',context)
        else:
            messages.error(request,'This is not your student')
            return redirect('PanelPage')

@login_required
def SendMessage(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user).first()
        title = request.POST['title']
        reciver = request.POST['Reciver']
        content = request.POST['msg']
        sender = teacher.TeacherID
        student = Student.objects.filter(StudentID=reciver).first()
        if teacher.TeacherID == student.ResposveTeacher:
            msg = Messages.objects.create(Msg_title = title , Msg_content = content,
                                         Msg_sender = sender , Msg_reciver=reciver)
            msg.save()
            messages.success(request,'Message sent successfully')
            return redirect('SendMsg')
    else:
        user = User.objects.filter(username=request.user).first()
        teacher = Teacher.objects.filter(TeacherID=user).first()
        students = Student.objects.filter(ResposveTeacher=teacher.TeacherID).all()
        context = {
            'students' : students
        }
        return render(request,'SendMessageTeacher.html',context)

@login_required
def Inbox(request):
    user = User.objects.filter(username=request.user).first()
    teacher = Teacher.objects.filter(TeacherID = user.username).first()
    msgs = Messages.objects.filter(Msg_reciver=teacher.TeacherID).all()
    context = {
        'msgs' : msgs
    }
    return render(request,'InboxTeacher.html',context)

@login_required
def Outbox(request):
    uesr = User.objects.filter(username = request.user).first()
    teacher = Teacher.objects.filter(TeacherID=uesr.username).first()
    msgs = Messages.objects.filter(Msg_sender = teacher.TeacherID).all()
    context = {
        'msgs' : msgs
    }
    return render(request,'Outbox.html',context)

def ForEverone(request):
    if request.method == 'POST':
        uesr = User.objects.filter(username = request.user).first()
        teacher = Teacher.objects.filter(TeacherID=uesr.username).first()
        students = Student.objects.filter(ResposveTeacher=teacher.TeacherID).all()
        title = request.POST['title']
        content = request.POST['msg']
        for student in students:
            msg = Messages.objects.create(Msg_title = title , Msg_content = content,
                                          Msg_sender= teacher.TeacherID , Msg_reciver = student.StudentID)
            msg.save()
        messages.success(request,'Messages send to all successfully')
        return redirect('SendMsgAll')
    else:
        return render(request,'SendMsgForAll.html')