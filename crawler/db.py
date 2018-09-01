import redis

REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"
REDIS_PASSWROD = "123456"
REDIS_MAX_CONNECTION = 20
# magnet 磁力链key
MAGNET_KEY = "magnet"


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWROD):
        conn_pool = redis.ConnectionPool(
            host=host,
            port=port,
            max_connections=REDIS_MAX_CONNECTION,
            password=password
        )
        self.redis = redis.Redis(conn_pool)

    def add_magnet(self, magnet):
        """
        新增磁力链
        :param magnet:
        :return:
        """
        self.redis.sadd(MAGNET_KEY, magnet)

    def get_magnet(self, count=128):
        """
        返回指定数量的磁力链
        :param count:
        :return:
        """
        return self.redis.srandmember(MAGNET_KEY, count)
