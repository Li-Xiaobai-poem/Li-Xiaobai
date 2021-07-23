from django.core import serializers
import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import re
import random
import pandas as pd
import numpy as np
from django.views.decorators.http import require_http_methods
from keras.preprocessing import sequence
from keras.optimizers import SGD, RMSprop, Adagrad
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU
from keras.models import load_model
from keras import backend as K

from rest_framework import viewsets

from app1.models import History
from app1.serializer import HistorySerializer
from app1.models import User
from app1.models import Release
from app1.models import Collections
from app1.models import Comments
from rest_framework.response import Response
# 场景识别
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models





def searchform(request):
    return render(request, 'LXB.html')


'''
@author 邓钧恒
@date 2021/07/09
生成诗词的函数 ，输入: 两个汉字, 行数, 每行的字数 (默认为五言绝句)
'''


def gen_poetry(model, seed_text, rows=4, cols=5):
    '''
    @author  邓钧恒
    @date 2021/07/09
    打开训练文本，这里暂时写成绝对路径，需要修改
    '''
    with open('D:/djangoProject7/static/poe/poetry.txt', 'r', encoding='UTF-8') as f:
        raw_text = f.read()
    lines = raw_text.split("\n")[:-1]
    poem_text = [i.split(':')[1] for i in lines]
    char_list = [re.findall('[\x80-\xff]{3}|[\w\W]', s) for s in poem_text]

    all_words = []
    for i in char_list:
        all_words.extend(i)
    word_dataframe = pd.DataFrame(pd.Series(all_words).value_counts())
    word_dataframe['id'] = list(range(1, len(word_dataframe) + 1))

    word_index_dict = word_dataframe['id'].to_dict()
    index_dict = {}
    for k in word_index_dict:
        index_dict.update({word_index_dict[k]: k})

    len(all_words), len(word_dataframe), len(index_dict)
    '''
     @author 邓钧恒
     @date 2021/07/09
     设定长度为一个字
    '''
    seq_len = 1

    total_cols = cols + 1  # 加上标点符号
    chars = re.findall('[\x80-\xff]{3}|[\w\W]', seed_text)
    if len(chars) != seq_len:  # seq_len =1
        return ""
    arr = [word_index_dict[k] for k in chars]
    for i in range(seq_len, rows * total_cols):
        if (i + 1) % total_cols == 0:  # 逗号或句号
            if (i + 1) / total_cols == 2 or (i + 1) / total_cols == 4:  # 句号的情况
                '''
                @author 邓钧恒
                @date 2021/07/09
                句号在字典中的映射为 2
                '''
                arr.append(2)

            else:
                '''
                @author 邓钧恒
                @date 2021/07/09
                逗号在字典中的映射为 1
                '''
                arr.append(1)
        else:
            proba = model.predict(np.array(arr[-seq_len:]), verbose=0)
            '''
            @author 邓钧恒
            @date 2021/07/09
            一个字是0，两个字是1
            '''
            predicted = np.argsort(proba[0])[-5:]
            '''
            @author 邓钧恒
            @date 2021/07/09
             在前五个可能结果里随机取, 避免每次都是同样的结果
            '''
            index = random.randint(0, len(predicted) - 1)  #
            new_char = predicted[index]
            while new_char == 1 or new_char == 2:  # 如果是逗号或句号或_, 应该重新换一个
                index = random.randint(0, len(predicted) - 1)
                new_char = predicted[index]

            arr.append(new_char)
    poem = [index_dict[i] for i in arr]

    return "".join(poem)


'''
@author 邓钧恒
@date 2021/07/12
生成诗歌
'''


def search(request):
    K.clear_session()
    model1 = load_model('D:/djangoProject7/static/poe/lstm_poetry2.hdf5', compile=False)

    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        '''
        @author 邓钧恒
        @date 2021/07/09
        从前端得到字（用name访问）
        '''
        message = request.GET['q']
        checkmessage = request.GET['PoemType']
        '''
        @author 邓钧恒
        @date 2021/07/09
        进行诗词格式的数字转换
        '''
        if checkmessage == '5yjj':
            a = 4
            b = 5
        if checkmessage == '7yjj':
            a = 4
            b = 7
        if checkmessage == '5yls':
            a = 8
            b = 5
        if checkmessage == '7yls':
            a = 8
            b = 7

        c = gen_poetry(model1, message, rows=a, cols=b)
        return render(request,
                      "LXB.html",
                      {
                          'result': c
                      })


'''
 @author 邓钧恒
 @date 2021/07/13
 获取前端关键字
'''
@require_http_methods(["GET"])
def getResult(request):
    response = {}  # 用于处理后向前端返回信息
    request.encoding = 'utf-8'


    try:
        # 诗歌类型： #关键字：

        checkmessage = request.GET.get('PoemType')
        message = request.GET.get('q')
        print(checkmessage)

        print(message)
        K.clear_session()
        model1 = load_model('D:/djangoProject7/static/poe/lstm_poetry2.hdf5', compile=False)

        '''
         @author 邓钧恒
         @date 2021/07/16
         根据诗歌类型进行判断 
        '''
        a = 0
        b = 0
        if checkmessage == '5yjj':
            a = 4
            b = 5
        if checkmessage == '7yjj':
            a = 4
            b = 7
        if checkmessage == '5yls':
            a = 8
            b = 5
        if checkmessage == '7yls':
            a = 8
            b = 7

        ######最新修改：
        '''
         @author 邓钧恒
         @date 2021/07/17
         根据类型进行分行
        '''
        result1 = gen_poetry(model1, message, rows=a, cols=b)
        print("here")
        result = ""
        if (checkmessage == '7yls'):
            i = 0
            while (i <= 63):
                if (i == 15 or i == 31 or i == 47 or i == 63):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1

        if (checkmessage == '5yls'):
            i = 0
            while (i <= 47):
                if (i == 11 or i == 35 or i == 47 or i == 23):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1
            #######
        if (checkmessage == '5yjj'):
            i = 0
            while (i <= 23):
                if (i == 11 or i == 23):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1
        if (checkmessage == '7yjj'):
            i = 0
            while (i <= 31):
                if (i == 15 or i == 31):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1

        result2 = ""
        for i in result:
            if (i == '_'):
                print("correct")
                result2 = result2 + "明"
            else:
                result2 = result2 + i;
        response['msg'] = 'success'
        response['error_num'] = 0  # 提示信息，实际不显示
        response['result'] = result2  # 返回给后端

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)  # 返回一个json给后端，想想ajax学习，其实知道后端产生json怎么产生了


'''
 @author 徐桑儒
 @date 2021/07/17
 论坛显示
'''
@require_http_methods(["GET"])
def showLuntan(request):
    response = {}

    try:

        # frontuser = request.GET.get('frontuser')
        # print("acv"+frontuser)
        rel = Release.objects.filter()

        response['msg'] = 'success'
        response['error_num'] = 0
        response['reallist'] = json.loads(serializers.serialize("json", rel))

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


'''
 @author 邓钧恒
 @date 2021/07/20
 收藏夹
'''
@require_http_methods(["GET"])
def addcollect1(request):
    response = {}

    try:

        username1 = request.GET.get('username')
        poemcontent1 = request.GET.get('poemcontent')
        keyword1 = request.GET.get('keyword')
        print("keyword1")

        collect_array = Collections.objects.all()
        '''
         @author 邓钧恒
         @date 2021/07/21
         当已经有这个信息时，将不会加入数据库
        '''
        flag = 1
        for item in collect_array:
            if item.username == username1 and item.keyword == keyword1 and item.poecontent == poemcontent1:
                flag = 2

        if flag == 1:
            c1 = Collections.objects.create(username=username1, poecontent=poemcontent1, keyword=keyword1)

            c1.save()
        response['msg'] = '收藏成功'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

'''
 @author 邓钧恒
 @date 2021/07/21
 评论显示
'''
@require_http_methods(["GET"])
def showComments(request):
    response = {}
    rel_id = request.GET.get('rel_id')
    print('烦烦烦' + rel_id)

    try:

        rel = Comments.objects.filter(release_id=rel_id)

        response['msg'] = 'success'
        response['error_num'] = 0
        response['comlist'] = json.loads(serializers.serialize("json", rel))
        print(response['comlist'])
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


'''
 @author 邓钧恒
 @date 2021/07/20
 添加评论
'''
@require_http_methods(["GET"])
def addComments(request):
    response = {}

    try:

        username1 = request.GET.get('username')
        comments1 = request.GET.get('saywords')
        release_id1 = request.GET.get('rel_id')

        c1 = Comments.objects.create(username=username1, comments=comments1, release_id=release_id1)

        c1.save()
        response['msg'] = '评论成功'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


'''
 @author 邓钧恒
 @date 2021/07/21
 场景生成
'''
@require_http_methods(["GET"])
def getResult2(request):
    response = {}  # 用于处理后向前端返回信息

    # book = Book(book_name=request.GET.get('book_name'))   获取用get加name这点不变
    # book.save()

    try:
        # 诗歌类型： #关键字：
        checkmessage = request.GET.get('PoemType')  # 到底对应的是前端的哪里，现在还没搞清楚
        message = request.GET.get('q')  # 处理后转化为关键字

        #######message处理
        try:
            cred = credential.Credential("AKID3vXsxnhT2NUN1RcZIm23oJYZLr8AwSjm", "qRmsiIchX8TZPzJOEpBH9l7D4g290bx4")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "nlp.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

            req = models.KeywordsExtractionRequest()
            params = {
                # 设置文本
                "Text": message,
                "Num": 1
            }
            req.from_json_string(json.dumps(params))

            resp = client.KeywordsExtraction(req)
            data1 = resp.to_json_string()
            user_dict = json.loads(data1)
            word = user_dict['Keywords'][0]['Word']
            message = word[0]

        except TencentCloudSDKException as err:
            print(err)
        '''
         @author 邓钧恒
         @date 2021/07/22
         清空模型数据
        '''#######
        K.clear_session()
        model1 = load_model('D:/djangoProject7/static/poe/lstm_poetry.hdf5', compile=False)
        a = 0
        b = 0
        if checkmessage == '5yjj':
            a = 4
            b = 5
        if checkmessage == '7yjj':
            a = 4
            b = 7
        if checkmessage == '5yls':
            a = 8
            b = 5
        if checkmessage == '7yls':
            a = 8
            b = 7
        ######最新修改：
        result1 = gen_poetry(model1, message, rows=a, cols=b)
        result = ""
        if (checkmessage == '7yls'):
            i = 0
            while (i <= 63):
                if (i == 15 or i == 31 or i == 47 or i == 63):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1

        if (checkmessage == '5yls'):
            i = 0
            while (i <= 47):
                if (i == 11 or i == 35 or i == 47 or i == 23):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1
            #######
        if (checkmessage == '5yjj'):
            i = 0
            while (i <= 23):
                if (i == 11 or i == 23):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1
        if (checkmessage == '7yjj'):
            i = 0
            while (i <= 31):
                if (i == 15 or i == 31):
                    result = result + '。' + '\n'
                else:
                    result = result + result1[i]
                i = i + 1

        response['msg'] = 'success'
        response['error_num'] = 0  # 提示信息，实际不显示
        response['result'] = result  # 返回给后端

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)  # 返回一个json给后端，想想ajax学习，其实知道后端产生json怎么产生了

'''
 @author 王博学
 @date 2021/07/14
 登录
'''
#######
@require_http_methods(["GET"])
def login(request):
    response = {}
    username = request.GET.get('username')
    password = request.GET.get('password')
    try:
        if username == '' or password == '':
            response['msg'] = '用户名/密码不能为空'
            response['error_num'] = 1
        else:
            flag = False
            if User.objects.filter(username__exact=username):
                username_array = User.objects.all()
                for item in username_array:
                    if item.username == username and item.password == password:
                        flag = True
                if flag:
                    response['msg'] = '成功登陆'
                    response['error_num'] = 0
                else:
                    response['msg'] = '用户名/密码错误'
                    response['error_num'] = 1
            else:
                response['msg'] = '用户名不存在'
                response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/14
 注册
'''
@require_http_methods(["GET"])
def regist(request):
    response = {}
    username = request.GET.get('username')
    password = request.GET.get('password')
    email = request.GET.get('email')
    sex = request.GET.get('sex')
    city = request.GET.get('city')

    try:
        print(sex == '0')
        if username == '' or password == '' or email == '' or sex == '' or city == '':
            response['msg'] = '请输入完整信息'
            response['error_num'] = 1
        else:
            if User.objects.filter(username__exact=username):
                response['msg'] = '用户名已存在'
                response['error_num'] = 1
            else:
                if User.objects.filter(email__exact=email):
                    response['msg'] = '邮箱已被使用'
                    response['error_num'] = 1
                else:
                    user = User.objects.create(username=username, password=password, email=email, sex=sex, city=city)
                    user.save()
                    response['msg'] = '注册成功'
                    response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/17
 接收用户名返回用户表的其他信息
'''
@require_http_methods(["GET"])
def get_user_info(request):  # 获得用户信息
    response = {}
    username = request.GET.get('username')
    try:
        user_array = User.objects.all()
        for item in user_array:
            if item.username == username:
                response['msg'] = {'email': item.email, 'sex': item.sex, 'city': item.city, 'password': item.password}
                print(response['msg'])
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

'''
 @author 林绰禧
 @date 2021/07/18
 从前端接收发布内容和用户名，将内容存入用户名对应的Release表
'''
@require_http_methods(["GET"])
def release_publish(request):  # 发布诗
    response = {}
    username = request.GET.get('username')
    keyword = request.GET.get('keyword')
    poecontent = request.GET.get('poecontent')
    mywords = request.GET.get('mywords')
    try:
        flag = True
        rel_array = Release.objects.all()
        for item in rel_array:
            if item.poecontent == poecontent:
                flag = False
        if flag:
            Release.objects.create(username=username, keyword=keyword, poecontent=poecontent, mywords=mywords)
            for item in Release.objects.all():
                if item.poecontent == poecontent:
                    rel_id = item.release_id
            Comments.objects.create(comments=mywords, username=username, release_id=rel_id)
            response['msg'] = '发布成功'
        else:
            response['msg'] = '此正文内容已存在'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

'''
 @author 吴维凡
 @date 2021/07/19
 通过用户名获得自己发布诗的信息
'''
@require_http_methods(["GET"])
def get_release_info(request):  # 获得自己发布的诗的信息
    response = {}
    username = request.GET.get('username')
    rel_array = Release.objects.filter(username=username)
    response['list'] = json.loads(serializers.serialize("json", rel_array))
    return JsonResponse(response)

'''
 @author 吴维凡
 @date 2021/07/19
 通过发布id获得发布诗的信息
'''
@require_http_methods(["GET"])
def get_release_info2(request):  # 发布的诗的信息
    response = {}
    release_id = request.GET.get('release_id')
    rel_array = Release.objects.filter(release_id=release_id)
    response['list'] = json.loads(serializers.serialize("json", rel_array))
    print(response['list'])
    return JsonResponse(response)

'''
 @author 吴维凡
 @date 2021/07/20
 通过发布id删除自己发布的诗
'''
@require_http_methods(["GET"])
def delete_release_info(request):  # 删除发布的诗
    response = {}
    release_id = request.GET.get('release_id')
    try:
        rel = Release.objects.get(release_id=release_id)
        rel.delete()
        response['msg'] = '删除成功'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/20
 通过发布id获得这首诗的评论表
'''
@require_http_methods(["GET"])
def get_comment_info(request):
    response = {}
    release_id = request.GET.get('release_id')
    com_array = Comments.objects.filter(release_id=release_id)
    response['list'] = json.loads(serializers.serialize("json", com_array))
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/17
 修改用户信息
'''
@require_http_methods(["GET"])
def change_user_info(request):  # 修改用户信息
    response = {}
    username = request.GET.get('username')
    password = request.GET.get('password')
    sex = request.GET.get('sex')
    email = request.GET.get('email')
    city = request.GET.get('city')
    try:
        user_array = User.objects.all()
        print(User.objects.get(username=username).email)
        for item in user_array:
            if User.objects.get(username=username).email != email and item.email == email:
                response['msg'] = '该邮箱已被注册'
                response['error_num'] = 1
            else:
                User.objects.filter(username=username).update(password=password, email=email, sex=sex, city=city)
                response['msg'] = '修改成功'
                response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/21
 通过收藏表的默认pk删除对应的诗
'''
@require_http_methods(["GET"])
def del_collections_info(request):  # 删除收藏的诗
    response = {}
    pk = request.GET.get('pk')
    try:
        coll = Collections.objects.get(pk=pk)
        coll.delete()
        response['msg'] = '删除成功'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

'''
 @author 王博学
 @date 2021/07/21
 根据用户名返回该用户名对应的收藏表
'''
@require_http_methods(["GET"])
def prt_collections_info(request):  # 打印收藏的诗
    response = {}
    username = request.GET.get('username')
    coll_array = Collections.objects.filter(username=username)
    response['list'] = json.loads(serializers.serialize("json", coll_array))
    return JsonResponse(response)
