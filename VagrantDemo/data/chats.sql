CREATE DATABASE `chats`;
USE `chats`;

DROP TABLE IF EXISTS `chat_logs`;
CREATE TABLE `chat_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text,
  `date_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

INSERT INTO `chat_logs` VALUES (1,'Ama','2017-01-07 06:07:12'),(2,'Derrick: Hello I am coming','2017-01-07 06:52:53');
