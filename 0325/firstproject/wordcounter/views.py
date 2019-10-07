import random
#만들어진 view저장
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    #count에서 받아온 내용..?
    full_text = request.GET['fulltext']
    #다시 보내주기.?
    word_list = full_text.split() #전체 텍스트를 스페이스 단위로 나눠서 담음
    word_dic = {} #사전형 변수

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return render(request,'count.html',{'fulltext': full_text,
                                        'total': len(word_list), #데이터 개수
                                        'dictionary': word_dic.items()})
    #return render(request,'count.html',{'fulltext':  request.GET[full_text]})
    #그니까 home.html에서 글을 쓰고 submit하면 views.py를 통해서 full_text변수를 받고
    #retrun 통해서 count.html로 출력

    #(3) html쪽으로 보내야 할 정보들, => 딕셔너리 자료형으로 보내야 한다.

def select(request): #select 함수에 요청이 들어오면 home.html로 보내줄거야
    #로또 번호 추출 코드 
    list = []
    ran_num = random.randint(1,45)

    for i in range(6):
        while ran_num in list:
            ran_num = random.randint(1, 45)
        list.append(ran_num)

    list.sort()

    return render(request,'home.html', {'list':list}) #(3)list의 값을 'list'의 이름으로 보낸다. 