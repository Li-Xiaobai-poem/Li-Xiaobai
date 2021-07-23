from django.urls import path, include  # 引入工具
# import app1.views                #引入views文件
from app1 import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('api', views.HistoryViewSet)   #由于第一季=级路径是app1，这里设的实际是访问自带工具的url的第二级，我设为api


urlpatterns = [

    # path('', include(router.urls)),

    path('search', views.search),
    path('searchform', views.searchform),
    path('getResult', views.getResult),
    path('getResult2', views.getResult2),
    path('login', views.login),
    path('regist', views.regist),
    path('showLuntan', views.showLuntan),
    path('addcollect1', views.addcollect1),
    path('showComments', views.showComments),
    path('addComments', views.addComments),

    path('userinfo/', views.get_user_info),
    path('releaseinfo/', views.get_release_info),
    path('releaseinfo2/', views.get_release_info2),
    path('reldelete/', views.delete_release_info),
    path('userchange/', views.change_user_info),
    path('colldelete', views.del_collections_info),
    path('collprint', views.prt_collections_info),
    path('commentinfo', views.get_comment_info),
    path('relpublish', views.release_publish)

]
