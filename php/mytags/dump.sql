-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 05, 2012 at 07:38 PM
-- Server version: 5.5.20
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tagger`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `tags` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE IF NOT EXISTS `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `user` int(11) NOT NULL,
  `title` varchar(256) NOT NULL,
  `content` text NOT NULL,
  `tags` varchar(256) NOT NULL,
  `score` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`id`, `date`, `user`, `title`, `content`, `tags`, `score`) VALUES
(1, '2012-06-04 16:41:02', 1, 'My first tag', 'I can haz tagz?', 'my tag', 0),
(2, '2012-06-05 11:16:22', 1, 'anonymous function', '(function(i) { ... } )(i);', '|javascript|', 0),
(3, '2012-06-05 11:17:38', 1, 'infowindow in loop', 'for (var i ...) {\r\n  (function (i) {\r\n     infowindow...\r\n   })(i);\r\n}', '|javascript|google maps|', 0),
(4, '2012-06-05 11:17:57', 1, 'licensing', 'to get a key or not to get a key', '|google maps|', 0),
(5, '2012-06-05 11:30:48', 1, 'oss', 'is open source software', '|gnu|', 0),
(6, '2012-06-05 11:42:42', 1, 'map shapes', 'naturalearthdata.com\r\n\r\nhow to use?', '|maps|', 0),
(7, '2012-06-05 14:28:23', 1, 'public void ', 'interface MyPublicVoidInterfacer extends PrivateDoubleStringArray implements NoGoodVector v {\r\n\r\n}...', '|java|', 0),
(8, '2012-06-05 14:31:19', 1, 'rules', 'window.[''varname'']', '|javascript|', 0),
(9, '2012-06-05 14:57:40', 1, 'php PDO insert', '<?php\r\n$stmt = $dbh->prepare("INSERT INTO REGISTRY (name, value) VALUES (:name, :value)");\r\n$stmt->bindParam('':name'', $name);\r\n$stmt->bindParam('':value'', $value);\r\n\r\n// insert one row\r\n$name = ''one'';\r\n$value = 1;\r\n$stmt->execute();\r\n\r\n// insert another row with different values\r\n$name = ''two'';\r\n$value = 2;\r\n$stmt->execute();\r\n?>', '|php|pdo|insert|', 0),
(10, '2012-06-05 14:58:58', 1, 'explode docs', 'array explode ( string $delimiter , string $string [, int $limit ] )\r\n\r\n$pizza  = "piece1 piece2 piece3 piece4 piece5 piece6";\r\n$pieces = explode(" ", $pizza);\r\n\r\nReturns an array.', '|php|explode|array|', 0),
(11, '2012-06-05 15:15:12', 1, 'PDO nettuts', 'http://net.tutsplus.com/tutorials/php/why-you-should-be-using-phps-pdo-for-database-access/', '|nettuts|pdo|tutorial|', 0),
(12, '2012-06-05 15:15:37', 1, 'PDO nettuts', 'http://net.tutsplus.com/tutorials/php/why-you-should-be-using-phps-pdo-for-database-access/', '|nettuts|pdo|tutorial|', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

CREATE TABLE IF NOT EXISTS `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `tag`
--

INSERT INTO `tag` (`id`, `name`) VALUES
(1, 'java'),
(2, 'php'),
(3, 'ads'),
(4, ''),
(5, 'javascript'),
(6, 'language'),
(7, 'Forth'),
(8, 'c++'),
(9, 'pl/sql'),
(10, 'haskell'),
(11, 'google maps'),
(12, 'gnu'),
(13, 'maps'),
(14, 'pdo'),
(15, 'insert'),
(16, 'explode'),
(17, 'array'),
(18, 'nettuts'),
(19, 'tutorial');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`) VALUES
(1, 'heitor');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
