from cookbook.util.info import etl


class CreateTable(object):
    def __init__(self, t_name):
        self.conn = etl
        self.cur = self.conn.cursor()
        self.t_name = t_name
        # if self._checkExists():
        #     print('This table is exist,Please check out!')
        #     exit(1)

    def create(self):
        """
        url = scrapy.Field()
        title = scrapy.Field()
        f_num = scrapy.Field()
        pic = scrapy.Field()
        category = scrapy.Field()
        nd = scrapy.Field()
        xgsc = scrapy.Field()
        xgzf = scrapy.Field()
        original = scrapy.Field()
        date = scrapy.Field()
        viewclicknum = scrapy.Field()
        zl = scrapy.Field()
        fl = scrapy.Field()
        """
        sql = """
		CREATE TABLE IF NOT EXISTS `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `f_num` varchar(100) DEFAULT '' COMMENT '收藏人数',
          `pic` varchar(300) DEFAULT '' COMMENT '菜谱图片链接',
          `category` longtext COMMENT '相关分类',
          `nd` varchar(100) DEFAULT '' COMMENT '难度',
          `xgsc` longtext COMMENT '相关食材',
          `xgzf` longtext COMMENT '相关做法',
          `original` varchar(500) DEFAULT '' COMMENT '查看原文',
          `date` varchar(100) DEFAULT '' COMMENT '菜谱上传时间',
          `viewclicknum` varchar(100) DEFAULT '' COMMENT '菜谱浏览量',
          `zl` longtext COMMENT '主料',
          `fl` longtext COMMENT '辅料',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_url` (`url`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='美食吧菜谱大全';
		""".format(self.t_name)
        self.cur.execute(sql)
        self.conn.commit()

    # def _checkExists(self):
    #     sql = """SELECT * FROM information_schema.tables WHERE table_name = '{0}'""".format(self.t_name)
    #     self.cur.execute(sql)
    #     if self.cur.fetchone():
    #         return True
    #     return False


if __name__ == '__main__':
    # print(etl.get_host_info())
    # print(etl.get_proto_info())
    ct = CreateTable('sbar')
    ct.create()
