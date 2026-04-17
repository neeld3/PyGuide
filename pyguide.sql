-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2025 at 09:14 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pyguide`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `signUp` (`user_full_name` VARCHAR(500), `user_email` VARCHAR(500), `user_name` VARCHAR(500), `user_password` VARCHAR(500), `user_age` INT)   BEGIN
    DECLARE last_id NUMERIC(8);

    SELECT COUNT(user_ID) INTO last_id FROM User;
    SET last_id = last_id + 1;

    INSERT INTO User 
    VALUES (
        last_id,
        user_full_name,
        user_email,
        user_name,
        user_password,
        user_age,
        NULL,
        NULL,
        "",
        '/static/avatars/python.png'
    );
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `Lesson`
--

CREATE TABLE `Lesson` (
  `lesson_ID` int(11) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `level` int(11) NOT NULL,
  `next_lesson` int(11) DEFAULT NULL,
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Lesson`
--

INSERT INTO `Lesson` (`lesson_ID`, `name`, `level`, `next_lesson`, `points`) VALUES
(1, 'Printing', 1, 0, 10),
(2, 'Variables', 1, 0, 15),
(3, 'Conditionals', 1, 0, 20),
(4, 'While_Loop', 1, 0, 25),
(5, 'For_Loop', 1, 11, 30),
(6, 'Printing', 2, 0, 40),
(7, 'Variables', 2, 0, 45),
(8, 'Conditionals', 2, 0, 50),
(9, 'While_Loop', 2, 0, 55),
(10, 'For_Loop', 2, 0, 60),
(11, 'String_Methods_Slicing', 2, 0, 70),
(12, 'Lists', 2, 0, 75),
(13, 'Dictionary', 2, 0, 85),
(14, 'Functions', 2, 24, 90),
(15, 'Printing', 3, 0, 100),
(16, 'Variables', 3, 0, 105),
(17, 'Conditionals', 3, 0, 110),
(18, 'While_Loop', 3, 0, 115),
(19, 'For_Loop', 3, 0, 120),
(20, 'String_Methods_Slicing', 3, 0, 130),
(21, 'Lists', 3, 0, 140),
(22, 'Dictionary', 3, 0, 150),
(23, 'Functions', 3, 0, 160),
(24, 'Files_Exceptions', 3, 0, 180),
(25, 'OOP', 3, 0, 200),
(26, 'Recursion', 3, 0, 250);

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `user_ID` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `age` int(11) NOT NULL,
  `recent_lesson` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `completed_lessons` varchar(255) DEFAULT '',
  `avatar` varchar(255) NOT NULL DEFAULT '/static/avatars/python.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`user_ID`, `name`, `email`, `username`, `password`, `age`, `recent_lesson`, `score`, `completed_lessons`, `avatar`) VALUES
(1, 'Mariam Rukhaia', 'mari@gmail.com', 'Mari', '$2b$12$P7IrmExxAHLX7WzgCqh59ev3tfetHVTIGPArO5SjEB7AJulOEtmRC', 10, 24, 6240, '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26', '/static/avatars/castle.png'),
(2, 'Nino Rukhaia', 'nino@gmail.com', 'nino', '$2b$12$ztccfKokD9qRqoTPBv8kceZGygBejUS4l03E7K8wgWHuccKCMv4yK', 14, 9, 225, '6,7,8,9', '/static/avatars/ninja.png'),
(3, 'oleg', 'olega@gmail.com', 'oleg', '$2b$12$hDEcVlk6hM0KOhl/lUlFfOwJXztsKwpvDHH9hvASja2y3FLr8qyxa', 16, 16, 205, '15,16', '/static/avatars/python.png'),
(4, 'elsa mitchell', 'elsa@kjhkjghkj', 'elsa', '$2b$12$J13D953SyckhSOSHEek2JOG/kCe4vG90Bl9cReWs77rjXIgqN.7ra', 14, 24, 750, '6,7,8,9,10,11,12,13,14,24', '/static/avatars/dragon.png'),
(5, 'neel dahake', 'bgdbf@nhgf', 'neel', '$2b$12$44RRwDBXupE8V.xPqEnOP..lfuyXJ1g20QEzmWCZGwEpau7lfTyLK', 6, 11, 130, '1,2,3,4,5', '/static/avatars/wizard.png'),
(6, 'Tinos Vafias', 'as@as', 'tinos', '$2b$12$e5zkURCPXBkbUNYlwkZ5k.xRIlpG76QpsorXekB9UjDQByIECRAfy', 13, NULL, NULL, '', '/static/avatars/cat.png'),
(7, 'jon a', 'a@a', 'jon', '$2b$12$SeFB7Y8V7NayS4C8JZYco.mdLFd2YZh80hZjTR.exG6Vugt26xCsW', 8, 2, 25, '1,2', '/static/avatars/dog.png'),
(8, 'Phillip Kentorovich', 'phillip@gmail.com', 'Phil', '$2b$12$1AFuNcjMb55uiiad2jdTYOxHqHHMGvwZAWlQJIXZDipQBTSSsoG8.', 16, NULL, NULL, '', '/static/avatars/python.png'),
(9, 'user level2', 'user_level2@gmail.com', 'user_level2', '$2b$12$Y3WKQrfwugB1nWLkcWRqSu5qURfFcc9OhbrjVn6ZmgOqP73DaenNi', 13, 6, 40, '6', '/static/avatars/ninja.png'),
(10, 'user level3', 'user_level3@gmail.com', 'user_level3', '$2b$12$SAL57gNMbZODB5VPzNvsD.tf05SnuweIrDKKEIaAER5E398PX47g.', 18, 15, 100, '15', '/static/avatars/python.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Lesson`
--
ALTER TABLE `Lesson`
  ADD PRIMARY KEY (`lesson_ID`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`user_ID`),
  ADD KEY `recent_lesson` (`recent_lesson`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `User`
--
ALTER TABLE `User`
  ADD CONSTRAINT `fk_recent_lesson` FOREIGN KEY (`recent_lesson`) REFERENCES `Lesson` (`lesson_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
