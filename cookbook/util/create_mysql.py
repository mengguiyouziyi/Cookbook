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
		CREATE TABLE `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `star_num` varchar(100) DEFAULT '' COMMENT '打星',
          `made_it` varchar(100) DEFAULT '' COMMENT '制作数',
          `review_count` varchar(100) DEFAULT '' COMMENT '浏览数',
          `picture_count` varchar(100) DEFAULT '' COMMENT '照片数',
          `author` varchar(100) DEFAULT '' COMMENT '作者',
          `descriptions` longtext COMMENT '描述',
          `pics` longtext COMMENT '照片列表',
          `time` varchar(100) DEFAULT '' COMMENT '烹饪时长',
          `servings` varchar(300) DEFAULT '' COMMENT '用餐人数',
          `nutrition` varchar(100) DEFAULT '' COMMENT '卡里路量',
          `ingredients` longtext COMMENT '配料',
          `pretime` varchar(100) DEFAULT '' COMMENT '准备时长',
          `cooktime` varchar(100) DEFAULT '' COMMENT '烹饪时长',
          `totaltime` varchar(100) DEFAULT '' COMMENT '总时长',
          `directions` longtext COMMENT '指南',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`(255)),
          KEY `index_url` (`url`(255))
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
    ct = CreateTable('allrecipes')
    ct.create()
