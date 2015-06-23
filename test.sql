-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 23, 2015 at 07:17 AM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `Administrator`
--

CREATE TABLE IF NOT EXISTS `Administrator` (
  `UserId` char(5) NOT NULL DEFAULT '',
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Administrator`
--

INSERT INTO `Administrator` (`UserId`, `password`) VALUES
('a', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `Bill`
--

CREATE TABLE IF NOT EXISTS `Bill` (
  `ResId` char(5) NOT NULL,
  `total` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ChessRoom`
--

CREATE TABLE IF NOT EXISTS `ChessRoom` (
  `FacilityId` char(5) NOT NULL,
  `size` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Company`
--

CREATE TABLE IF NOT EXISTS `Company` (
  `cName` varchar(20) NOT NULL,
  `cAdress` varchar(20) DEFAULT NULL,
  `GId` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Company`
--

INSERT INTO `Company` (`cName`, `cAdress`, `GId`) VALUES
('fe', 'e', '0');

-- --------------------------------------------------------

--
-- Table structure for table `Contact`
--

CREATE TABLE IF NOT EXISTS `Contact` (
  `GId` char(5) NOT NULL DEFAULT '',
  `telNo` varchar(20) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Contact`
--

INSERT INTO `Contact` (`GId`, `telNo`) VALUES
('0', '3'),
('1', '0');

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE IF NOT EXISTS `Employee` (
  `UserId` char(5) NOT NULL DEFAULT '',
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`UserId`, `password`) VALUES
('1', '2'),
('2', '33');

-- --------------------------------------------------------

--
-- Table structure for table `Facility`
--

CREATE TABLE IF NOT EXISTS `Facility` (
  `FacilityId` char(5) NOT NULL,
  `ServiceId` char(5) NOT NULL,
  `duration` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Food`
--

CREATE TABLE IF NOT EXISTS `Food` (
  `FoodId` char(5) NOT NULL,
  `ServiceId` char(5) NOT NULL,
  `deliveredTime` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Global`
--

CREATE TABLE IF NOT EXISTS `Global` (
  `UserId` int(11) DEFAULT NULL,
  `RoomId` int(11) DEFAULT NULL,
  `GId` int(11) DEFAULT NULL,
  `ResId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Global`
--

INSERT INTO `Global` (`UserId`, `RoomId`, `GId`, `ResId`) VALUES
(3, 18, 2, 9);

-- --------------------------------------------------------

--
-- Table structure for table `Guest`
--

CREATE TABLE IF NOT EXISTS `Guest` (
  `GId` char(5) NOT NULL,
  `guestType` varchar(20) DEFAULT NULL,
  `VId` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Guest`
--

INSERT INTO `Guest` (`GId`, `guestType`, `VId`) VALUES
('0', 'VIP', '33'),
('1', 'Ordinary', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Gym`
--

CREATE TABLE IF NOT EXISTS `Gym` (
  `FacilityId` char(5) NOT NULL,
  `type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Person`
--

CREATE TABLE IF NOT EXISTS `Person` (
  `SSN` char(5) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `firstName` varchar(20) DEFAULT NULL,
  `lastName` varchar(20) DEFAULT NULL,
  `GId` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Person`
--

INSERT INTO `Person` (`SSN`, `age`, `gender`, `firstName`, `lastName`, `GId`) VALUES
('123', 32, 'F', 's', 's', NULL),
('32', 1, 'F', '3', 'd', '1');

-- --------------------------------------------------------

--
-- Table structure for table `Reserve`
--

CREATE TABLE IF NOT EXISTS `Reserve` (
  `EmpId` char(5) DEFAULT NULL,
  `GId` char(5) DEFAULT NULL,
  `RoomId` char(5) DEFAULT NULL,
  `ResId` char(5) NOT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Reserve`
--

INSERT INTO `Reserve` (`EmpId`, `GId`, `RoomId`, `ResId`, `startDate`, `endDate`) VALUES
('1', '1', '1', '1', '2015-06-23', '2015-07-23'),
('1', '1', '2', '2', '2015-06-23', '2015-08-23'),
('1', '1', '15', '3', '2015-06-23', '2016-06-23'),
('2', '0', '3', '4', '2015-06-24', '2015-06-30'),
('1', '1', '4', '7', '2015-06-23', '2017-06-24'),
('1', '1', '0', '8', '2015-06-23', '2020-06-23');

-- --------------------------------------------------------

--
-- Table structure for table `Room`
--

CREATE TABLE IF NOT EXISTS `Room` (
  `RoomId` char(5) NOT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `BigFlag` tinyint(1) DEFAULT NULL,
  `DoubleFlag` tinyint(1) DEFAULT NULL,
  `SingleFlag` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Room`
--

INSERT INTO `Room` (`RoomId`, `available`, `price`, `BigFlag`, `DoubleFlag`, `SingleFlag`) VALUES
('0', 0, 200, 1, 0, 0),
('1', 0, 200, 1, 0, 0),
('10', 1, 100, 0, 0, 1),
('11', 1, 100, 0, 0, 1),
('12', 1, 100, 0, 0, 1),
('13', 1, 100, 0, 0, 1),
('14', 1, 100, 0, 0, 1),
('15', 0, 30000, 1, 0, 0),
('16', 1, 3321, 0, 0, 1),
('2', 0, 5000, 1, 0, 0),
('3', 0, 200, 1, 0, 0),
('4', 0, 200, 1, 0, 0),
('5', 1, 300, 0, 1, 0),
('6', 1, 300, 0, 1, 0),
('7', 1, 300, 0, 1, 0),
('8', 1, 300, 0, 1, 0),
('9', 1, 300, 0, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `Service`
--

CREATE TABLE IF NOT EXISTS `Service` (
  `ServiceId` char(5) NOT NULL,
  `cost` int(11) DEFAULT NULL,
  `RoomId` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VIP`
--

CREATE TABLE IF NOT EXISTS `VIP` (
  `VId` char(5) NOT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Administrator`
--
ALTER TABLE `Administrator`
 ADD PRIMARY KEY (`UserId`);

--
-- Indexes for table `Bill`
--
ALTER TABLE `Bill`
 ADD PRIMARY KEY (`ResId`);

--
-- Indexes for table `ChessRoom`
--
ALTER TABLE `ChessRoom`
 ADD PRIMARY KEY (`FacilityId`);

--
-- Indexes for table `Company`
--
ALTER TABLE `Company`
 ADD PRIMARY KEY (`cName`), ADD KEY `GId` (`GId`);

--
-- Indexes for table `Contact`
--
ALTER TABLE `Contact`
 ADD PRIMARY KEY (`GId`,`telNo`);

--
-- Indexes for table `Employee`
--
ALTER TABLE `Employee`
 ADD PRIMARY KEY (`UserId`);

--
-- Indexes for table `Facility`
--
ALTER TABLE `Facility`
 ADD PRIMARY KEY (`FacilityId`,`ServiceId`), ADD KEY `ServiceId` (`ServiceId`);

--
-- Indexes for table `Food`
--
ALTER TABLE `Food`
 ADD PRIMARY KEY (`FoodId`,`ServiceId`), ADD KEY `ServiceId` (`ServiceId`);

--
-- Indexes for table `Guest`
--
ALTER TABLE `Guest`
 ADD PRIMARY KEY (`GId`);

--
-- Indexes for table `Gym`
--
ALTER TABLE `Gym`
 ADD PRIMARY KEY (`FacilityId`);

--
-- Indexes for table `Person`
--
ALTER TABLE `Person`
 ADD PRIMARY KEY (`SSN`), ADD KEY `GId` (`GId`);

--
-- Indexes for table `Reserve`
--
ALTER TABLE `Reserve`
 ADD PRIMARY KEY (`ResId`), ADD KEY `EmpId` (`EmpId`), ADD KEY `GId` (`GId`), ADD KEY `RoomId` (`RoomId`);

--
-- Indexes for table `Room`
--
ALTER TABLE `Room`
 ADD PRIMARY KEY (`RoomId`);

--
-- Indexes for table `Service`
--
ALTER TABLE `Service`
 ADD PRIMARY KEY (`ServiceId`), ADD KEY `RoomId` (`RoomId`);

--
-- Indexes for table `VIP`
--
ALTER TABLE `VIP`
 ADD PRIMARY KEY (`VId`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Bill`
--
ALTER TABLE `Bill`
ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`ResId`) REFERENCES `Reserve` (`ResId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ChessRoom`
--
ALTER TABLE `ChessRoom`
ADD CONSTRAINT `chessroom_ibfk_1` FOREIGN KEY (`FacilityId`) REFERENCES `Facility` (`FacilityId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Company`
--
ALTER TABLE `Company`
ADD CONSTRAINT `company_ibfk_1` FOREIGN KEY (`GId`) REFERENCES `Guest` (`GId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Contact`
--
ALTER TABLE `Contact`
ADD CONSTRAINT `contact_ibfk_1` FOREIGN KEY (`GId`) REFERENCES `Guest` (`GId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Facility`
--
ALTER TABLE `Facility`
ADD CONSTRAINT `facility_ibfk_1` FOREIGN KEY (`ServiceId`) REFERENCES `Service` (`ServiceId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Food`
--
ALTER TABLE `Food`
ADD CONSTRAINT `food_ibfk_1` FOREIGN KEY (`ServiceId`) REFERENCES `Service` (`ServiceId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Gym`
--
ALTER TABLE `Gym`
ADD CONSTRAINT `gym_ibfk_1` FOREIGN KEY (`FacilityId`) REFERENCES `Facility` (`FacilityId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Person`
--
ALTER TABLE `Person`
ADD CONSTRAINT `person_ibfk_1` FOREIGN KEY (`GId`) REFERENCES `Guest` (`GId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Reserve`
--
ALTER TABLE `Reserve`
ADD CONSTRAINT `reserve_ibfk_1` FOREIGN KEY (`EmpId`) REFERENCES `Employee` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `reserve_ibfk_2` FOREIGN KEY (`GId`) REFERENCES `Guest` (`GId`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `reserve_ibfk_3` FOREIGN KEY (`RoomId`) REFERENCES `Room` (`RoomId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Service`
--
ALTER TABLE `Service`
ADD CONSTRAINT `service_ibfk_1` FOREIGN KEY (`RoomId`) REFERENCES `Room` (`RoomId`) ON DELETE SET NULL ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
