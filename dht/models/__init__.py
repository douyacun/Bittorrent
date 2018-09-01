import datetime, pytz
from sqlalchemy import Column, String, Integer, DateTime, Text
from ..db import mysqlBase


def get_date():
    # def get_datetime():
    tz = pytz.timezone('Asia/Shanghai')
    return datetime.datetime.now(tz)


class Videos(mysqlBase()):
    """
    视频库
    """
    __tablename__ = "scrapy_videos"
    __table_args__ = {'extend_existing': True}
    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 分类
    class_id = Column(Integer)
    # 标题
    title = Column(String(255), unique=True)
    # 原标题
    original_title = Column(String(500))
    # 导演
    director = Column(String(500))
    # 编剧
    screen_writer = Column(String(255))
    # 主演
    actor = Column(Text)
