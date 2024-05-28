from flask import Flask, render_template, request
import datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/secynd')
def secynd():
    return render_template('secynd.html')


@app.route('/taimer')
def taimer():
    return render_template('taimer.html')


@app.route('/change_timer', methods=['POST'])
def change_timer():
   new_time = int(request.form['new_time'])
   # Обработка нового времени таймера
   return ''


@app.route('/finish_timer', methods=['POST'])
def finish_timer():
   # Обработка завершения таймера
   return ''


if __name__ == '__main__':
    app.run(debug=True)