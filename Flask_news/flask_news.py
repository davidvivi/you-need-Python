# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# import pymysql
# pymysql.install_as_MySQLdb()

# __name__是用来确定flask运行的主文件
app = Flask(__name__)

# 开启debug模式方法一
app.debug = True
# +pymysql的目的是为了解决Flask中连接MySQL时出现ModuleNotFoundError: No module named 'MySQLdb'错误
# 或者在上面加入import pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask'
# 'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300), )
    author = db.Column(db.String(20), )
    view_count = db.Column(db.Integer)
    create_at = db.Column(db.Integer)
    is_valid = db.Column(db.Boolean)

    # __repr__方法告诉Python如何打印class对象，方便我们调试使用
    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """新闻首页"""
    news_list = News.query.all()
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """新闻类别"""
    news_list = News.query.filter(News.types == name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """新闻详情信息"""
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


if __name__ == '__main__':
    # 开启debug模式方法一
    app.run(debug=True)
