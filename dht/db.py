import redis
import mysql.connector
from .utils import config

# magnet 磁力链key
MAGNET_KEY = "info_hash"


class RedisClient:
    def __init__(self):
        conn_pool = redis.ConnectionPool(
            host=config('redis.host'),
            port=config('redis.port'),
            password=config('redis.password'),
            db=config('redis.db'),
            max_connections=config('redis.max_connections')
        )
        self.redis = redis.Redis(connection_pool=conn_pool)

    def add_magnet(self, magnet):
        """
        新增磁力链
        :param magnet:
        :return:
        """
        self.redis.zincrby(MAGNET_KEY, magnet, 1)

    def get_magnet(self, count=128):
        """
        返回指定数量的磁力链
        :param count:
        :return:
        """
        return self.redis.srandmember(MAGNET_KEY, count)

    def get_zlencount(self, min=None, max=None):
        return self.redis.zlexcount(MAGNET_KEY, min, max)


class MysqlClient:
    def __init__(self):
        self.conn = mysql.connector.connect(user=config('mysql.user'), password=config('mysql.password'),
                                            database=config('mysql.database'), host=config('mysql.host'),
                                            port=config('mysql.port'), use_unicode=True)
        self.db = self.conn.cursor()

    def execute(self, sql, args):
        self.db.execute(sql, args)
        self.conn.commit()

    def select(self, sql, args):
        self.db.execute(sql, args)
        return self.db.fetchall()

    def add_magnet(self, magnet):
        """
        新增磁力链
        :param magnet:
        :return:
        """
        sql = "insert into dht_magnet (info_hash) values (%s)"
        args = [magnet]
        self.execute(sql, args)
