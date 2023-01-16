from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index', methods=["GET", "POST"])
def index():
    summ = 'Данные не введены'
    if request.method == 'POST':
        some_nums_form = request.form.get('some_nums_form')
        nums = list(some_nums_form)
        summ = 0
        for num in nums:
            summ += int(num)
        summ = str(summ)
    return render_template('index.html', result=summ)


if __name__ == '__main__':
    app.run()
