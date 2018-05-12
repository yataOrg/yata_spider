/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50714
Source Host           : 127.0.0.1:3306
Source Database       : yata_data_01

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-05-11 01:09:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for elm_new
-- ----------------------------
DROP TABLE IF EXISTS `elm_new`;
CREATE TABLE `elm_new` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  `float_delivery_fee` float(5,2) DEFAULT NULL COMMENT '配送费',
  `float_minimum_order_amount` float(6,1) DEFAULT NULL COMMENT '最低起送',
  `cuisine` varchar(50) DEFAULT NULL COMMENT '菜系',
  `latitude` float(16,6) DEFAULT NULL COMMENT '纬度',
  `longitude` float(16,6) DEFAULT NULL COMMENT '经度',
  `name` varchar(255) DEFAULT NULL,
  `opening_hours1` varchar(50) DEFAULT NULL COMMENT '营业时间1',
  `opening_hours2` varchar(50) DEFAULT NULL COMMENT '营业时间2',
  `opening_hours3` varchar(50) DEFAULT NULL COMMENT '营业时间3',
  `phone1` varchar(20) DEFAULT NULL COMMENT '电话1',
  `phone2` varchar(20) DEFAULT NULL COMMENT '电话2',
  `rating` float(3,1) DEFAULT NULL COMMENT '综合评价',
  `order_lead_time` varchar(10) DEFAULT NULL COMMENT '平均送达速度',
  `recommend_reasons` varchar(255) DEFAULT NULL COMMENT '推荐理由',
  `distance` float(15,3) unsigned DEFAULT NULL COMMENT '距离',
  `ele_distance` float(15,3) unsigned DEFAULT NULL COMMENT '饿了么的距离',
  `ele_id` int(15) unsigned NOT NULL COMMENT '饿了么的店铺id',
  `ele_authentic_id` int(15) unsigned NOT NULL COMMENT '饿了么可信的id',
  `search_jwd` varchar(255) DEFAULT NULL COMMENT '搜索的经纬度',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `updated_at` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `latitude` (`latitude`),
  KEY `longitude` (`longitude`),
  KEY `ele_id` (`ele_id`),
  KEY `ele_authentic_id` (`ele_authentic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


