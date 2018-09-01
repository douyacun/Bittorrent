from dht.maga import Maga
from dht.utils import get_logger, config
# from dht.db import MysqlClient

logger = get_logger('dht')
# rd = MysqlClient()


class Crawler(Maga):
    async def handle_get_peers(self, infohash, addr):
        logger.info(
            "Receive get peers message from DHT {}. Infohash: {}.".format(
                addr, infohash
            )
        )
        # rd.add_magnet(infohash.lower())

    async def handle_announce_peer(self, infohash, addr, peer_addr):
        logger.info(
            "Receive announce peer message from DHT {}. Infohash: {}. Peer address:{}".format(
                addr, infohash, peer_addr
            )
        )
        # rd.add_magnet(infohash.lower())


if __name__ == '__main__':
    # crawler = Crawler()
    # Set port to 0 will use a random available port
    # crawler.run(port=6881)
    # rd.add_magnet("B7611BAACDEA11816D0959F62617A6A88383993A".lower())
    print(config('mysql.port'))

