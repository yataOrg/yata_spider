/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50714
Source Host           : 127.0.0.1:3306
Source Database       : yata_data_01

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-05-13 21:20:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for elm_restaurant
-- ----------------------------
DROP TABLE IF EXISTS `elm_restaurant`;
CREATE TABLE `elm_restaurant` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL COMMENT '餐厅描述',
  `flavors` varchar(255) DEFAULT NULL COMMENT '风味',
  `float_delivery_fee` float(5,2) DEFAULT NULL COMMENT '配送费',
  `float_minimum_order_amount` float(6,1) DEFAULT NULL COMMENT '最低起送',
  `ele_id` int(15) unsigned NOT NULL COMMENT '饿了么的店铺id',
  `latitude` float(16,6) DEFAULT NULL COMMENT '纬度',
  `longitude` float(16,6) DEFAULT NULL COMMENT '经度',
  `name` varchar(255) DEFAULT NULL,
  `opening_hours1` varchar(50) DEFAULT NULL COMMENT '营业时间1',
  `opening_hours2` varchar(50) DEFAULT NULL COMMENT '营业时间2',
  `opening_hours3` varchar(50) DEFAULT NULL COMMENT '营业时间3',
  `order_lead_time` varchar(10) DEFAULT NULL COMMENT '平均送达速度',
  `phone1` varchar(20) DEFAULT NULL COMMENT '电话1',
  `phone2` varchar(20) DEFAULT NULL COMMENT '电话2',
  `promotion_info` varchar(512) DEFAULT NULL COMMENT '推荐信息',
  `rating` float(3,1) DEFAULT NULL COMMENT '综合评价',
  `rating_count` int(8) unsigned DEFAULT '0' COMMENT '星星后面的数字',
  `recent_order_num` int(10) unsigned DEFAULT '0' COMMENT '最近订单数?不清楚他的计算规则?todo',
  `recommend_reasons` varchar(255) DEFAULT NULL COMMENT '推荐理由',
  `supports` varchar(512) DEFAULT NULL COMMENT '商品支持',
  `city` int(8) unsigned DEFAULT '0',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `updated_at` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `latitude` (`latitude`),
  KEY `longitude` (`longitude`),
  KEY `ele_id` (`ele_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of elm_restaurant
-- ----------------------------
INSERT INTO `elm_restaurant` VALUES ('2', '闵行区江川路街道东川路889-1号', '2008年在北京开创了以台湾三角烧为主的甜品店。独创的丰厚馅料让三角烧。随后这美味便流向了全国各处。原材料要考究，做工要精细新鲜，对待每一位食客都要用心。', '甜品,简餐,', '0.00', '10.0', '58', '31.016766', '121.430901', '握的饭团', '08:40/21:00', '', '', '38', '18621927110', '', '本店所有证照齐全，干净卫生，请放心用餐。\n本店承诺：本店以服务客人为己任，实行不合口味不满意可退换，，如果您满意请给个好评，若不满意请电话告诉我们我们可以为你从新做或者换其他口味的。满足您合理的要求。\n如果需要饮品请注明冷热----默认为热', '4.7', '96', '178', '', '该商户食品安全已由中国太平洋保险承保，食品安全有保障|', '0', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('3', '上海市闵行区江川路街道东川路800号63幢底层118商铺', '烧烤，汉堡，鸡肉卷，酒水，饮料应有尽有，来者不拒吆。', '烧烤,', '0.00', '15.0', '60', '31.018049', '121.429543', '诚信烧烤', '15:00/23:40', '', '', '49', '13795394018', '', '各位同学好，本店于2月28正常营业，谢谢同学们的支持和光顾，祝新年快乐，诚信烧烤的新老顾客，本店搬迁到校外面，比起在校内送外卖有点远，所以外卖的速度会有一点点慢，希望各位同学能够谅解，谢谢', '4.7', '2603', '2323', '味道超赞|回头客多|', '', '1', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('4', '上海市闵行区江川路街道东川路811弄23-24号', '', '日韩料理,简餐,', '0.00', '16.0', '62', '31.017702', '121.434181', '大学路韩国料理', '08:10/22:30', '', '', '47', '18221792009', '34290736', '温馨提示:本店配送免费.上楼（包括电梯楼)收费3元', '4.7', '525', '1704', '回头客多|', '', '1', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('5', '上海市闵行区沧源路847号', '泡泡所有产品均为现做现卖！', '包子粥店,简餐,', '0.00', '10.0', '63', '31.016748', '121.428040', '泡泡香香鸡.粥.便当', '10:00/22:30', '', '', '0', '15001978727', '', 'PopU泡泡营业截止时间恢复至22:30！本店配送默认不提供上楼服务。', '5.0', '0', '2', '配送飞快|', '该商家支持开发票，开票订单金额100元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('6', '上海市闵行区江川街道东川路811弄38号一层B室，39号一层B室', '本店', '简餐,', '0.00', '10.0', '68', '31.017391', '121.434006', '老妈厨房', '09:30/21:00', '', '', '49', '15201927090', '15201927091', '【老妈厨房】成立于2009年，由一位毕业于［交大］，［复旦］三个孩子的妈妈主持。她用“三个原则”做菜，《一》孩子爱吃，《二》营养均衡，《三》干净卫生。【老妈】用“帮助在外大学生父母的心照顾他们的孩子。”', '4.7', '1253', '6343', '味道超赞|回头客多|', '该商户食品安全已由中国太平洋保险承保，食品安全有保障|该商家支持开发票，开票订单金额100元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('7', '闵行区东川路889号17-19号', '', '其他菜系,简餐,', '1.00', '10.0', '69', '31.017138', '121.429588', '新疆饭店', '09:50/15:00', '16:00/22:30', '', '57', '15821572036', '15821572507', '感谢同学们一如继往的支持，', '4.6', '225', '1517', '', '该商家支持开发票，开票订单金额60元起，请在下单时填写好发票抬头|', '0', '2018-05-13 20:18:56', '2018-05-13 20:18:56');
INSERT INTO `elm_restaurant` VALUES ('8', '上海市闵行区江川路街道东川路889-23号', '本店是交大十年老店，东北炒菜，盖浇饭，东北手工水饺，欢迎品尝。东川店。', '饺子馄饨,简餐,', '0.00', '10.0', '75', '31.016972', '121.428497', '东北饺子王', '09:30/22:00', '', '', '47', '13248289515', '', '', '4.7', '280', '1579', '回头客多|', '该商家支持开发票，开票订单金额50元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:57', '2018-05-13 20:18:57');
INSERT INTO `elm_restaurant` VALUES ('9', '上海市闵行区江川路街道东川路897号897-36室', '欢迎光临本店！', '汉堡,奶茶果汁,', '0.00', '10.0', '78', '31.016214', '121.428123', '可顿奶茶汉堡', '10:00/23:00', '', '', '39', '13816298149', '54717175', '本店套餐可乐或奶茶可以互换，可乐全部是加冰的，没有去冰或不加冰的，请知悉！小区不提供上楼服务，如有需要请点上楼费！为了方便您尽快拿到外卖，请保持手机畅通！谢谢！', '4.8', '987', '6022', '味道超赞|回头客多|', '该商户食品安全已由中国太平洋保险承保，食品安全有保障|该商家支持开发票，开票订单金额20元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:57', '2018-05-13 20:18:57');
INSERT INTO `elm_restaurant` VALUES ('10', '上海市闵行区东川路811弄35号－3', 'HL家，只因有你！^_^', '简餐,', '1.00', '9.0', '80', '31.018265', '121.434174', 'HL', '08:30/21:00', '', '', '38', '13137297480', '', '2008年L为H的一份照烧鸡排所感动，7年后L决定嫁给这个为人真诚笨笨但是用心的男孩，这是故事的开始。。。然而当年的小男孩如今已经长大，L想把学生时代的那份照烧鸡排，真诚还有懵懂传给更多的人，我们做的不仅仅是外卖，还是种对爱的传承。\r\n', '3.9', '90', '509', '', '该商户食品安全已由中国太平洋保险承保，食品安全有保障|该商家支持开发票，开票订单金额100元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:57', '2018-05-13 20:18:57');
INSERT INTO `elm_restaurant` VALUES ('11', '上海市闵行区东川路811弄35号2室', '十年老店，品质保证，好奇汉堡感谢各位新老同学对好奇的大力支持、好奇的宗旨是我们用心，让你放心。', '汉堡,简餐,', '0.00', '10.0', '56', '31.017994', '121.434631', '好奇汉堡', '09:15/23:55', '', '', '39', '13585535757', '13761839949', '本店卫生和产品质量经政府部门验收 合格，拥有政府颁发的《营业执照》和《食品经营许可证》，是 双证齐全店家，请大家放心食用。好奇汉堡，十年老店，欢迎您！本店考虑电瓶车安全，外卖只送到楼下，恕不上楼，敬请理解与配合。东海学院不让外卖进出，所有外卖只能送到大门口，不出来拿者，请勿点餐。', '4.7', '492', '3720', '味道超赞|回头客多|', '该商户食品安全已由中国太平洋保险承保，食品安全有保障|该商家支持开发票，开票订单金额200元起，请在下单时填写好发票抬头|', '1', '2018-05-13 20:18:59', '2018-05-13 20:18:59');
INSERT INTO `elm_restaurant` VALUES ('12', '宝山区新沪路689号', '正宗港式烧腊', '盖浇饭,简餐,', '5.00', '20.0', '115', '31.272537', '121.419312', '福荣祥烧腊(新沪路店)', '09:00/19:45', '', '', '36', '13564849649', '66397751', '', '4.9', '319', '458', '', '该商家支持开发票，开票订单金额100元起，请在下单时填写好发票抬头|', '0', '2018-05-13 20:18:59', '2018-05-13 20:18:59');
