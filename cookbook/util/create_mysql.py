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
        CREATE TABLE IF NOT EXISTS `meishij` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `f_num` varchar(100) DEFAULT '' COMMENT '收藏人数',
          `pic` varchar(300) DEFAULT '' COMMENT '菜谱图片链接',
          `news_id` varchar(30) DEFAULT '' COMMENT '菜谱id',
          `category` longtext COMMENT '菜谱分类',
          `pinglun` varchar(30) DEFAULT '' COMMENT '评论数',
          `step` varchar(30) DEFAULT '' COMMENT '步骤数目',
          `gx` varchar(500) DEFAULT '' COMMENT '功效',
          `gy` varchar(100) DEFAULT '' COMMENT '工艺',
          `nd` varchar(100) DEFAULT '' COMMENT '难度',
          `rsh` varchar(100) DEFAULT '' COMMENT '人数',
          `kw` varchar(100) DEFAULT '' COMMENT '口味',
          `zbsj` varchar(100) DEFAULT '' COMMENT '准备时间',
          `prsj` varchar(100) DEFAULT '' COMMENT '烹饪时间',
          `author` varchar(100) DEFAULT '' COMMENT '作者',
          `author_url` varchar(500) DEFAULT '' COMMENT '作者主页url',
          `v_small` varchar(10) DEFAULT '' COMMENT '是否大V',
          `cp_num` varchar(100) DEFAULT '' COMMENT '作者菜谱数',
          `gz_num` varchar(100) DEFAULT '' COMMENT '作者被关注数',
          `fs_num` varchar(100) DEFAULT '' COMMENT '作者粉丝数',
          `date` varchar(100) DEFAULT '' COMMENT '菜谱上传时间',
          `viewclicknum` varchar(100) DEFAULT '' COMMENT '菜谱浏览量',
          `jy` longtext COMMENT '作者寄语',
          `zl` longtext COMMENT '主料',
          `fl` longtext COMMENT '辅料',
          `prjq` longtext COMMENT '烹饪技巧',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_news_id` (`news_id`),
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='美食杰菜谱大全';

        :return:
        """
        sql = """
		CREATE TABLE IF NOT EXISTS `{}` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
          `url` varchar(500) DEFAULT '' COMMENT '网页url',
          `title` varchar(500) DEFAULT '' COMMENT '菜谱名称',
          `f_num` varchar(100) DEFAULT '' COMMENT '收藏人数',
          `pic` varchar(300) DEFAULT '' COMMENT '菜谱图片链接',
          `news_id` varchar(30) DEFAULT '' COMMENT '菜谱id',
          `category` longtext COMMENT '菜谱分类',
          `pinglun` varchar(30) DEFAULT '' COMMENT '评论数',
          `step` varchar(30) DEFAULT '' COMMENT '步骤数目',
          `gx` varchar(500) DEFAULT '' COMMENT '功效',
          `gy` varchar(100) DEFAULT '' COMMENT '工艺',
          `nd` varchar(100) DEFAULT '' COMMENT '难度',
          `rsh` varchar(100) DEFAULT '' COMMENT '人数',
          `kw` varchar(100) DEFAULT '' COMMENT '口味',
          `zbsj` varchar(100) DEFAULT '' COMMENT '准备时间',
          `prsj` varchar(100) DEFAULT '' COMMENT '烹饪时间',
          `author` varchar(100) DEFAULT '' COMMENT '作者',
          `author_url` varchar(500) DEFAULT '' COMMENT '作者主页url',
          `v_small` varchar(10) DEFAULT '' COMMENT '是否大V',
          `cp_num` varchar(100) DEFAULT '' COMMENT '作者菜谱数',
          `gz_num` varchar(100) DEFAULT '' COMMENT '作者被关注数',
          `fs_num` varchar(100) DEFAULT '' COMMENT '作者粉丝数',
          `date` varchar(100) DEFAULT '' COMMENT '菜谱上传时间',
          `viewclicknum` varchar(100) DEFAULT '' COMMENT '菜谱浏览量',
          `jy` longtext COMMENT '作者寄语',
          `zl` longtext COMMENT '主料',
          `fl` longtext COMMENT '辅料',
          `prjq` longtext COMMENT '烹饪技巧',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
          PRIMARY KEY (`id`),
          KEY `index_title` (`title`),
          KEY `index_news_id` (`news_id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='美食杰菜谱大全';
		""".format(self.t_name)
        self.cur.execute(sql)
        self.conn.commit()

    def add_column(self):
        sql = """alter table {} add citycode varchar(6) DEFAULT '' COMMENT '是否大V';"""

    # def _checkExists(self):
    #     sql = """SELECT * FROM information_schema.tables WHERE table_name = '{0}'""".format(self.t_name)
    #     self.cur.execute(sql)
    #     if self.cur.fetchone():
    #         return True
    #     return False


if __name__ == '__main__':
    # print(etl.get_host_info())
    # print(etl.get_proto_info())
    ct = CreateTable('meishij')
    ct.create()
