-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2024 at 08:18 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydata`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee1`
--

CREATE TABLE `employee1` (
  `department` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `married_status` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `doj` varchar(45) DEFAULT NULL,
  `id_proof_type` varchar(45) DEFAULT NULL,
  `id_proof` varchar(45) NOT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `citizen` varchar(45) DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee1`
--

INSERT INTO `employee1` (`department`, `name`, `position`, `email`, `address`, `married_status`, `dob`, `doj`, `id_proof_type`, `id_proof`, `gender`, `phone`, `citizen`, `salary`) VALUES
('University', 'Evana Kapoor', 'Rektor', 'evanakar@gmail.com', 'New Delhi, India', 'Unmarried', '17/09/1999', '03/01/2024', 'NIP', '1209445035891351', 'Female', '83145789044', 'WNA', '50000000'),
('Faculty', 'Rifdah Testuro', 'Donatur tetap', 'rifdhtts@gmail.com', 'Japan', 'Married', '17/11/1994', '01/01/2016', 'NIK', '18080382741922', 'Male', '083113426826', 'WNA', '100000000000'),
('University', 'Divany', 'Admin', 'divany@gmail.com', 'Pringsewu, Lampung, Indonesia', 'Unmarried', '16/06/1998', '20/01/2020', 'NIK', '1810025606040003', 'Female', '0895366740169', 'WNI', '5000000'),
('Major', 'Amelia', 'Dosen', 'amel@gmail.com', 'Bandar Lampung, Lampung', 'Unmarried', '16/04/1999', '12/03/2018', 'NIP', '1920043510024', 'Female', '895705086106', 'WNI', '15000000'),
('Faculty', 'Safitri Khan', 'Dekan', 'Safitrikhann@gmail.com', 'Dubai', 'Unmarried', '27/02/1995', '08/11/2023', 'NIK', '91873986498653', 'Female', '82345081292', 'WNA', '35000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee1`
--
ALTER TABLE `employee1`
  ADD PRIMARY KEY (`id_proof`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
