from info import etl


class CreateTable(object):
    def __init__(self, t_name):
        self.conn = etl
        self.cur = self.conn.cursor()
        self.t_name = t_name
        # if self._checkExists():
        #     print('This table is exist,Please check out!')
        #     exit(1)

    def create(self):
        sql = """
		CREATE TABLE IF NOT EXISTS `{}`(
           `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增id',
           `url` VARCHAR(500) DEFAULT '' COMMENT '网页url',
           `title` VARCHAR(500) DEFAULT '' COMMENT '菜谱名称',
           `f_num` VARCHAR(100) DEFAULT '' COMMENT '收藏人数',
           `gx` VARCHAR(500) DEFAULT '' COMMENT '功效',
           `gy` VARCHAR(100) DEFAULT '' COMMENT '工艺',
           `nd` VARCHAR(100) DEFAULT '' COMMENT '难度',
           `rsh` VARCHAR(100) DEFAULT '' COMMENT '人数',
           `kw` VARCHAR(100) DEFAULT '' COMMENT '口味',
           `zbsj` VARCHAR(100) DEFAULT '' COMMENT '准备时间',
           `prsj` VARCHAR(100) DEFAULT '' COMMENT '烹饪时间',
           `author` VARCHAR(100) DEFAULT '' COMMENT '作者',
           `author_url` VARCHAR(500) DEFAULT '' COMMENT '作者主页url',
           `v_small` VARCHAR(10) DEFAULT '' COMMENT '是否大V',
           `cp_num` VARCHAR(100) DEFAULT '' COMMENT '作者菜谱数',
           `gz_num` VARCHAR(100) DEFAULT '' COMMENT '作者被关注数',
           `fs_num` VARCHAR(100) DEFAULT '' COMMENT '作者粉丝数',
           `date` VARCHAR(100) DEFAULT '' COMMENT '菜谱上传时间',
           `viewclicknum` VARCHAR(100) DEFAULT '' COMMENT '菜谱浏览量',
           `jy` longtext COMMENT '作者寄语',
           `zl` VARCHAR(500) DEFAULT '' COMMENT '主料',
           `fl` LONGTEXT COMMENT '辅料',
           `prjq` longtext COMMENT '烹饪技巧',
          `load_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '落地时间',
           PRIMARY KEY ( `id` ),
           KEY `index_title` (`title`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '美食杰菜谱大全';
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
    ct = CreateTable('meishij')
    ct.create()
