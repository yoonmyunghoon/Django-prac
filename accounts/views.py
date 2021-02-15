from django.shortcuts import render
import random
from datetime import datetime
from decouple import config
import requests

def index(request):
    return render(request, 'accounts/index.html')

def image(request):
    return render(request, 'accounts/image.html')

def dinner(request):
    menu = ['족발', '치킨', '햄버거', '초밥']
    pick = random.choice(menu)
    context = {'pick' : pick}
    return render(request, 'accounts/dinner.html', context)

def hello(request, name, age):
    menu = ['족발', '치킨', '햄버거', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick': pick,
    }
    return render(request, 'accounts/hello.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'accounts/template_language.html', context)

def static_example(request):
    return render(request, 'accounts/static_example.html')


# 네이버 마마고 번역
def mamago(request):
    return render(request, 'accounts/mamago.html')

def translated(request):
    #1. 사용자가 입력한 번역하고자 하는 한국어 텍스트
    word = request.GET.get('word')

    #2. 네이버에 번역 요청을 위해 필요한 준비
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    #3. 요청을 보낼 url
    mamago_url = 'https://openapi.naver.com/v1/papago/n2mt'

    #4. 헤더 정보 구성
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
    }

    #5. 요청 데이터 준비
    data = {
        'source': 'ko',
        'target': 'en',
        'text': word
    }

    #6. 네이버로 요청을 보내자!
    mamago_response = requests.post(mamago_url, headers=headers, data=data).json()
    # print(mamago_response)

    #7. 번역된 텍스트 뽑기
    english = mamago_response.get('message').get('result').get('translatedText')

    context = {
        'korean': word,
        'english': english,
    }

    return render(request, 'accounts/translated.html', context)