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
        item['url'] = response.url
        item['title'] = title
        item['sub_title'] = sub_title
        item['time'] = time
        item['servings'] = servings
        item['nutrition'] = nutrition
        item['description'] = description
        item['like'] = like if like else ''
        item['save'] = save if save else ''
        item['ingredients'] = ingredients
        item['tools'] = tools
        """
        sql = """
		CREATE TABLE IF NOT EXISTS `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `sub_title` varchar(500) DEFAULT '' COMMENT '副标题',
          `time` varchar(100) DEFAULT '' COMMENT '烹饪时长',
          `servings` varchar(300) DEFAULT '' COMMENT '用餐人数',
          `nutrition` varchar(100) DEFAULT '' COMMENT '卡里路量',
          `description` longtext COMMENT '描述',
          `like` varchar(100) DEFAULT '' COMMENT 'facebook点赞数',
          `save` varchar(100) DEFAULT '' COMMENT 'pinterest收藏数',
          `ingredients` longtext COMMENT '配料',
          `tools` longtext COMMENT '工具',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_url` (`url`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='blueapron菜谱大全';
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
    ct = CreateTable('blueapron')
    ct.create()
