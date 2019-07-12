from flask import Flask, render_template, request
from datetime import datetime
import random
app = Flask(__name__)


@app.route('/')
def hello():
    # return 'Hello World!'
    # render_template 씀
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY'


@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days}일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """


@app.route('/greeting/<name>')
# @app.route('/greeting/<string:name>') 위랑 아래랑 같음 
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    # 연산을 모두 끝내고 변수만 cube.html 로 넘긴다.
    # return f'{number} 세제곱은 {number**3}입니다.'
    result = number**3
    return render_template('cube.html', result = result, html_number=number)

@app.route('/dinner/<int:number>')
def dinner(number):
    dinner_menu = ['호박고구마','감자','깻잎','김치']
    return f'오늘의 점심은 {random.sample(dinner_menu,number)}'


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면','탕수육','볶음밥','팔보채','짬뽕','유산슬']
    order = random.sample(menu, people)
    return str(order)


    # render template


@app.route('/movie')
def movie():
    movies = ['토이스토리4', '알라딘', '스파이더맨', '기생충', '엔드게임']
    return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    print(request.args)
    name = request.args.get('data') #안녕하세요가 들어가져있을거임
    return render_template('pong.html', name=name)


    # https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
    return render_template('naver.html')


#  https://www.google.com/search?source=hp&ei=   
@app.route('/google')
def google():
    return render_template('google.html')


    # https://www.google.com/search?source=hp&ei=-b4mXbfRCoGl8QX8oaa4CQ&q=


    # 이름 받을 페이지 
    # 결과가 나올 페이지
    # 함수도 2개 (본본 신이나를만들때 처럼 만들려면)


@app.route('/fakevonvon')
def fakevonvon():
    return render_template('fakevonvvon.html')


@app.route('/realvonvon/')
def realvonvon():
    name = request.args.get(name)
    first_list = ['잘생김', '못생김', '어중어중']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
        first = random.choice(first_list)
        second = random.choice(second_list)
        third = random.choice(third_list)

        return render_template('realvonvon.html', name=name, first=first, second=second,third=third)