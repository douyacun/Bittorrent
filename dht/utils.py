import logging
import os, binascii
from struct import unpack
from socket import inet_ntoa
import configparser

# 每个节点长度
PER_NODE_LEN = 26
# 节点 id 长度
PER_NID_LEN = 20
# 节点 id 和 ip 长度
PER_NID_NIP_LEN = 24
# 构造邻居随机结点
NEIGHBOR_END = 14
# 日志等级
LOG_LEVEL = logging.INFO
# 配置文件读取
cg = configparser.ConfigParser()
cg.read('.env')
section = cg.sections()


def get_rand_id():
    """
    生成随机的节点 id，长度为 20 位
    """
    return os.urandom(PER_NID_LEN)


def get_neighbor(target):
    return target[:NEIGHBOR_END] + get_rand_id()[NEIGHBOR_END:]


def get_logger(logger_name):
    """
    获取日志实例
    :param logger_name:
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    fh = logging.StreamHandler()
    fh.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(fh)
    return logger


def get_nodes_info(nodes):
    """
    解析 find_node 回复中 nodes 节点的信息
    :param nodes: 节点薪资
    """
    length = len(nodes)
    # 每个节点单位长度为 26 为，node = node_id(20位) + node_ip(4位) + node_port(2位)
    if (length % PER_NODE_LEN) != 0:
        return []

    for i in range(0, length, PER_NODE_LEN):
        nid = nodes[i:i + PER_NID_LEN]
        # 利用 inet_ntoa 可以返回节点 ip
        ip = inet_ntoa(nodes[i + PER_NID_LEN:i + PER_NID_NIP_LEN])
        # 解包返回节点端口
        port = unpack("!H", nodes[i + PER_NID_NIP_LEN:i + PER_NODE_LEN])[0]
        yield (nid, ip, port)


def proper_infohash(infohash):
    """
    把 bytes 转换为 hex
    :param infohash:
    :return:
    """
    if isinstance(infohash, bytes):
        # 返回二进制数据的16进制的表现形式
        infohash = binascii.hexlify(infohash).decode('utf-8')
    return infohash.upper()


def config(args):
    """
    获取配置参数
    :param args: ['mysql', 'port'] or "mysql.port"
    :return: None or section
    """
    if isinstance(args, list) and len(args) != 2:
        return None
    elif isinstance(args, str):
        args = args.split('.')
        if len(args) != 2:
            return None

    return cg.get(args[0], args[1])
