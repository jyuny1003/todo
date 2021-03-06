from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from .models import scores

# Create your views here.

def index(request):
    
    print(request.GET)
    
    return render(request, 'first/index.html') 

    

def students(request):

    #디비에서 데이터 가져와서
    students = Students.objects.all()
    """
        SELECT *
            FROM students
    """

    #템플릿에 보내주기
    return render(request, 'first/students.html', {
        'text': '안녕하세요!',
        'students': students
    })


def score(request):
    score_2 = scores.objects.all()
    return render(request, 'first/scores.html')



# render(request, 템플릿경로 text, 보낼 데이터 dict)