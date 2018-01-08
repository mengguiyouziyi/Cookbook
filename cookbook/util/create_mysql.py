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
            item['pic'] = pic
            item['likes'] = likes
            item['camera'] = camera
            item['desc'] = desc
            item['author_url'] = author_url
            item['author'] = author
            item['Ingredients'] = json.dumps(Ingredients, ensure_ascii=False)
            item['servings'] = servings
            item['cook_time'] = cook_time
            item['instructions'] = json.dumps(instructions, ensure_ascii=False)
        """
        sql = """
		CREATE TABLE IF NOT EXISTS `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `pic` varchar(500) DEFAULT '' COMMENT '菜谱图片',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `likes` varchar(500) DEFAULT '' COMMENT '喜欢数',
          `camera` varchar(500) DEFAULT '' COMMENT '照片数',
          `desc` varchar(500) DEFAULT '' COMMENT '菜谱介绍',
          `author_url` varchar(500) DEFAULT '' COMMENT '作者url',
          `author` varchar(500) DEFAULT '' COMMENT '作者',
          
          `ingredients` longtext COMMENT '配料',
          
          `servings` varchar(500) DEFAULT '' COMMENT '服务人数',
          `cook_time` varchar(500) DEFAULT '' COMMENT '总时间',
          `instructions` longtext COMMENT '步骤',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_url` (`url`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='cookpad菜谱大全';
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
    ct = CreateTable('cookpad')
    ct.create()
