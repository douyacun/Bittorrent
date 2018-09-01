from dht.dyc import DYC
from dht.utils import get_logger
# from dht.db import MysqlClient

logger = get_logger('dht')
# rd = MysqlClient()


class Crawler(DYC):
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
    crawler = Crawler()
    crawler.run(port=6881)

