from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    #return render_template("index.html")
    return index()

@app.route('/movie')
def movie():
    conn = sqlite3.connect("movies.db")  # 打开或创建数据库
    cur = conn.cursor()  # 拿到数据库的游标
    sql = "select * from movies250;"
    datalist = []
    data = cur.execute(sql)  # 执行sql语句
    for item in data:
        datalist.append(item)

    cur.close()
    conn.close()
    return render_template("movie.html",datalist = datalist)

@app.route('/score')
def score():
    conn = sqlite3.connect("movies.db")  # 打开或创建数据库
    cur = conn.cursor()  # 拿到数据库的游标
    sql = "select score,count(score) from movies250 group by score;"
    scorelist = []
    countlist = []
    data = cur.execute(sql)  # 执行sql语句
    for item in data:
        scorelist.append(str(item[0]))
        countlist.append(item[1])

    cur.close()
    conn.close()
    return render_template("score.html",scorelist=scorelist,countlist=countlist)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
