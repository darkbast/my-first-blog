
from django.conf.urls import url
from . import views

# post_list라는 이름의 view가 ^$에 활당
# http://127.0.0.1:8000/ 이라면 views.post_list를 불러옴.
# name='post_list'는 뷰의 이름을 
urlpatterns = [
	url(r'^$',views.post_list,name='post_list'),
]