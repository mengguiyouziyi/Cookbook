import redis
from info import etl


class Send(object):
    def __init__(self, conn=etl, redis_key='meishij:dupefilter'):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.r = redis.StrictRedis(host='10.142.97.92')
        self.key = redis_key

    def send(self):
        sql = """select url from meishij"""
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for i, result in enumerate(results):
            while (i+1) % 1000 == 0:
                print(i)
            url = result.get('url', '')
            if not url:
                continue
            self.r.sadd(self.key, url)


if __name__ == '__main__':
    send = Send()
    send.send()
