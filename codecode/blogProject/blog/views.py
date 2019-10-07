from django.shortcuts import render,get_object_or_404,redirect #get_object_or_404, redirect 추가해줘야해
from django.utils import timezone
from .models import Blog,Comment
# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-id') #Blog 객체를 다 가져오겠다.
    #-id (역순)
    return render(request, 'blog/home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'blog/new.html'); #요청이 들어오면 render라는 함수를 통해 new.html 파일을 띄워주자

def create(request):
    blog = Blog() #붕어빵 틀
    blog.title = request.GET['title'] #new.html에서 name을 tilte로 지어줬자나 ! 그거 가져온다.
    blog.body = request.GET['body'] #new.html에서 name을 body로 지어준 거 가져온다.
    blog.pub_date = timezone.datetime.now() #python에서 현재 시간을 불러온다.
    #저장해준다.
    blog.save() 

    #return render(request,'') #create 되는 공간을 보여줄 필요가 없어
    #그래서 이렇게 한다.!
    return redirect('/blog/'+str(blog.id))

#U-edit 수정하는 페이지를 띄으는 동작
def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/edit.html',{'blog':blog}); #요청이 들어오면 render라는 함수를 통해 edit.html 파일을 띄워주자

#U-updates 실제 글이 수정되는 동작
def update(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id) #붕어빵 틀
    blog.title = request.GET['title'] #new.html에서 name을 tilte로 지어줬자나 ! 그거 가져온다.
    blog.body = request.GET['body'] #new.html에서 name을 body로 지어준 거 가져온다.
    blog.pub_date = timezone.datetime.now() #python에서 현재 시간을 불러온다.
    #저장해준다.
    blog.save() 

    #return render(request,'') #create 되는 공간을 보여줄 필요가 없어
    #그래서 이렇게 한다.!
    return redirect('/blog/'+str(blog.id))

#D-delete
def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()

    return redirect('home')
    # 삭제하면 그 페이지가 사라질거니까 home으로 갈게

def comment_create(request,blog_id):
    comment = Comement()#댓글을 저장하기 위해 빈 Comment 객체를 하나 생성
    comment.body = request.GET['content'] #댓글의 내용을 받아옴
    comment.blog = get_object_or_404(Blog,pk=blog_id)#해당 댓글을 어떤 blog 객체와 연결시켜줄지
    comment.save() #만들어진 comment db에 저장

    return redirect('/blog/'+str(blog_id)) #보고 있었던 글로 돌아갈 수 있도록 url 설정