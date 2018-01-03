import redis, hashlib


class Send(object):
    def __init__(self):
        # self.conn = conn
        # self.cursor = self.conn.cursor()
        # self.r = redis.StrictRedis(host='10.142.97.92')
        # self.key = redis_key
        self.sha = hashlib.sha1()

    def send(self, url):
        self.sha.update(url.encode('utf-8'))

        print(self.sha.hexdigest())

        # sql = """select url from meishij"""
        # self.cursor.execute(sql)
        # results = self.cursor.fetchall()
        # for i, result in enumerate(results):
        #     if (i + 1) % 5000 == 0:
        #         print(i)
        #     url = result.get('url', '')
        #     if not url:
        #         continue
        #     self.sha.update(url.encode('utf-8'))
        #     self.r.sadd(self.key, url)


if __name__ == '__main__':
    send = Send()
    send.send('http://www.meishij.net/chufang/diy/shipincaipu/xiangcai/170296.html')
    send.send('http://www.meishij.net/yaoshanshiliao/jibingtiaoli/gaoxueya/176827.html')
