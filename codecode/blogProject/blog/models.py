from django.db import models

# Create your models here.
class Blog(models.Model): #blog라는 이름의 객체 틀을 만들겠다.
    title=models.CharField(max_length=200) #title 이름으로 최대 200글자의 데이터를 받겠다.
    pub_date = models.DateTimeField('date published') #pub_date라는 이름으로 시간 날짜 데이터를 받겠다.
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    #Blog 모델과 관계를 맺어준다. 1:N에서 N의 속성으로 들어간다
    # on_delete 는 관계를 맺고 있는 Blog 객체가 삭제되면 관련된 Comment도 삭제시킨다
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.body

