from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
# def index(request):
#     row = GuessNumbers(name=request.POST['name'], text=request.POST['text'])
#     row.lottos = ""
#     origin = list(range(1,46))
#
#     for _ in range(0, row.num_lotto):
#         random.shuffle(origin)
#         guess = origin[:6]
#         guess.sort()
#         row.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가
#
#     row.update_date = timezone.now()
#     row.save() # commit
#
#     return HttpResponse('<h1>Hello, world!</h1>')


def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 원한다면 SQL문으로도 들고올 수 있음
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음

    # {'lottos':lottos} <- context
    return render(request, 'lotto/default.html', {'lottos':lottos})



def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")



def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)  # 채워진 양식
        if form.is_valid():
            lotto = form.save(commit=False)  # DB에 행이 올라가긴 하지만, 파일에 반영은 안한 상태
            # 추가 조치
            # lotto.name = lotto.name.strip()
            lotto.generate()   # name열과 text열만 받았으니, lottos, num_lotto, update_date 채워줘야함
            # generate와 save는 같아서 default값이 commit=True로 DB에 저장이 된다
            return redirect('index')
            # 다 불러와서 return render(request, 'lotto/form.html', {'form':form}) 대신에 redirect 하나

        ### 1번째 방법 (Form Tag 안쓰고 손수 꺼내 쓸 때)
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_text)
        # row.generate()  # self.save()

        # print('\n\n\n===========================\n\n\n')
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print('\n\n\n===========================\n\n\n')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto": lotto})
