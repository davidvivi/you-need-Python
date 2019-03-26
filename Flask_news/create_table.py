# -*- coding: utf-8 -*-

from Flask_news.flask_news import db
from Flask_news.flask_news import News

# 创建名为news的数据表
db.create_all()

# 插入
# db.session.add(News(title='标题1', content='内容1', types='类型1'))
# db.session.add(News(title='标题2', content='内容2', types='类型2'))
# db.session.commit()

# 查询
News.query.all()  # 查询全部
News.query.filter_by(title='标题1').first()
