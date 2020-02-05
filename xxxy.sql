# Host: localhost  (Version: 5.0.96-community)
# Date: 2020-02-05 00:16:10
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "datas"
#

DROP TABLE IF EXISTS `datas`;
CREATE TABLE `datas` (
  `Id` int(11) NOT NULL auto_increment,
  `time` varchar(255) default NULL,
  `username` varchar(255) default NULL,
  `status_1` varchar(255) default NULL COMMENT '本人是否健康',
  `status_2` varchar(255) default NULL COMMENT '家人是否健康',
  `status_3` varchar(255) default NULL COMMENT '是否在校',
  `stu_name` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Data for table "datas"
#

/*!40000 ALTER TABLE `datas` DISABLE KEYS */;
INSERT INTO `datas` VALUES (1,'2020-02-04','admin','Yes','Yes','Yes','高镭'),(2,'2020-02-04','admin2','Yes','Yes','Yes','张三'),(3,'2020-02-05','20171305202','Yes','Yes','Yes','高镭'),(4,'2020-02-05','admin2','Yes','Yes','Yes','张三'),(5,'2020-02-05','admin','Yes','Yes','Yes','高镭');
/*!40000 ALTER TABLE `datas` ENABLE KEYS */;

#
# Structure for table "users"
#

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `Id` int(11) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `flag` varchar(255) default NULL,
  `stu_name` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

#
# Data for table "users"
#

/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','1','高镭'),(2,'admin2','admin2','1','张三'),(3,'20171305202','5202','2','高镭'),(4,'20171305301','5203','2','宗欣'),(5,'20171305203','5203','2','张子禹');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
