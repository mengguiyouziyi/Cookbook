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
            pic = scrapy.Field()
            title = scrapy.Field()
            rate = scrapy.Field()
            review = scrapy.Field()
            submitter = scrapy.Field()
            submitterLogo = scrapy.Field()
            submitterTitle = scrapy.Field()
            submitterRole = scrapy.Field()
            nutrition_profile = scrapy.Field()
            ingredients = scrapy.Field()
            active = scrapy.Field()
            totalTime = scrapy.Field()
            step = scrapy.Field()
        """
        sql = """
		CREATE TABLE IF NOT EXISTS `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `pic` varchar(500) DEFAULT '' COMMENT '菜谱图片',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `rate` varchar(500) DEFAULT '' COMMENT '评分',
          `review` varchar(500) DEFAULT '' COMMENT '评论数',
          `submitter` varchar(500) DEFAULT '' COMMENT '贡献者',
          `submitterLogo` varchar(500) DEFAULT '' COMMENT '贡献者照片',
          `submitterTitle` varchar(500) DEFAULT '' COMMENT '贡献者名字',
          `submitterRole` varchar(500) DEFAULT '' COMMENT '贡献者角色',
          `nutrition_profile` varchar(500) DEFAULT '' COMMENT '营养特点',
          `ingredients` longtext COMMENT '配料',
          `active` varchar(500) DEFAULT '' COMMENT '烹饪时间',
          `totalTime` varchar(500) DEFAULT '' COMMENT '总时间',
          `step` longtext COMMENT '步骤',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_url` (`url`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='allrecipes菜谱大全';
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
    ct = CreateTable('eatingwell')
    ct.create()
