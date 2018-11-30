from django.http import HttpResponse
from django.shortcuts import render
import random

from django.utils import timezone

from lotto.models import Number

def read(request, num):
    n = Number.objects.get(id=num)

    return render(request,
                  'lotto/read.html',
                  {'n': n})

def index(request):
    # 저장된 로또번호 가져오기
    lottos = Number.objects.order_by('-id')

    return render(request,
                  'lotto/index.html',
                  {'lottos': lottos})

def make(request):
    # http://localhost:8000/lotto/make?title=제목명
    title = request.GET['title']

    lotto = [n for n in range(1, 46)]
    random.shuffle(lotto)
    lotto = lotto[:6]
    print(lotto)

    Number.objects.create(title=title, lottos=lotto, create_date=timezone.now())

    return HttpResponse(lotto)