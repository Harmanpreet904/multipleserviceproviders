-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2019 at 08:47 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `msp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `mobile` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`email`, `password`, `type`, `mobile`) VALUES
('harmanpreet904@gmail.com', 'imadmin', 'Admin', '7905115731'),
('tubidy@vu.co', '12344321', 'Sub Admin', '9116446513');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bookingid` int(11) NOT NULL,
  `memail` varchar(500) NOT NULL,
  `serviceid` int(11) NOT NULL,
  `usermobile` varchar(15) NOT NULL,
  `useremail` varchar(500) NOT NULL,
  `address` varchar(500) NOT NULL,
  `totalcharges` float NOT NULL,
  `status` varchar(500) NOT NULL,
  `bookingdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bookingid`, `memail`, `serviceid`, `usermobile`, `useremail`, `address`, `totalcharges`, `status`, `bookingdate`) VALUES
(109, 'harmanpreet904@gmail.com', 13, '9695330329', 'sandeepsand@gmail.com', 'Vill tah', 400, 'pending', '2019-11-19'),
(110, 'harmanpreet904@gmail.com', 13, '7006436851', 'erharsh237@gmail.com', 'Global', 400, 'pending', '2019-11-30'),
(111, 'harmanpreet904@gmail.com', 13, '7006436851', 'erharsh237@gmail.com', 'Global Institutes Batala Road Amritsar Jammu Highway,Punjab', 400, 'pending', '2019-11-21');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `categoryname` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `photo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`categoryname`, `description`, `photo`) VALUES
('AC & Refrigeration', 'Most of us use AC’s and Refrigerators throughout the year or most of the year. AC Servicing becomes mandatory during the start of heating and cooling seasons respectively. Timely servicing ensures fresh and filtered air. While AC’s provide us with deep pleasure of comfort they also require regular maintenance. All AC and Ref must be installed along with a good quality stabilizer', 'Ac-Repair_01.png'),
('Carpenter', 'Every household and office would have at least 1 broken door knob, hinges or handles. UnHung paintings vying for your attention. We consider carpentry to be the job for experts, as it requires specialized tools and skills. We take responsibility for service delivery from end to end. We help you customize or repair your furniture, doors and windows.\n', 'Carpenter.png'),
('Electrician', 'You want immediate services when your geyser or water motor breaks down for a sparkling switch or wiring fuse. We understand the urgency and provide express electrician services in with a TAT of 2 hours. We become your one call partner for all your electrician requirement, from a ceiling fan installation to doing commercial wiring or working on CAT 6 networking cable, our electricians can do it all.\n', 'electrician.jpg'),
('Fitter', 'With the assistance of our skilled professionals, we are offering Insulation Fitter Service. The Insulation Fitter Service is provided by our skilled professionals, as they have advance knowledge of the domain. Besides, these services are rendered accordingly as per clients requirements.', 'fitter.jpg'),
('Painter', 'With the continuous support and sincere efforts put by our experienced professionals, we have been able to provide our clients the best quality Modern Wall Painting Service. Offered service is performed under the strict supervision of our experts using optimum grade paints and latest techniques.', 'painter.jpg'),
('Plumber', 'Most of us surely find it frustrating to live with a broken tap, leaky pipe, undone toilet flush or low water pressure during our long showers. But somehow, we do live with it or we have to, as we have no idea how to get it fixed. It’s too time consuming and we choose to better utilize our time by living with issues. At Our Service we make sure that only an experienced serviceman knocks your door on the time promised.\n', 'plumbing.jpg'),
('Saloon', 'All Types OF Saloon Work', 'delicon.png'),
('Welder', 'Our team of technicians are second to none when it comes to welder repairs. Whether your welder is as old as the hills or a recent release our technicians have the training needed to make your welder work for you. Ongoing training programs, an extensive resource base, and the ability to source parts that would otherwise be unobtainable serve to back our already skilled technicians. If price is an issue, ask our friendly staff to quote on all repairs. Metro Welder Services are warranty repair age', 'welder.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `merchantservices`
--

CREATE TABLE `merchantservices` (
  `serviceid` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `services` varchar(30) NOT NULL,
  `price` float NOT NULL,
  `description` varchar(500) NOT NULL,
  `photo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `merchantservices`
--

INSERT INTO `merchantservices` (`serviceid`, `email`, `services`, `price`, `description`, `photo`) VALUES
(13, 'harmanpreet904@gmail.com', 'Indoor Lights & Lighting Acces', 100, 'All types of Indoor Lights & Lighting Accessories', 'electrician1.jpg'),
(14, 'amarjeetsingh00595@gmail.com', 'Furniture Installation And Ass', 200, 'We provide Furniture Installation And Assembly', 'carpenter1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `id` int(11) NOT NULL,
  `rating` float NOT NULL,
  `serviceid` int(11) NOT NULL,
  `review` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`id`, `rating`, `serviceid`, `review`) VALUES
(1, 4, 13, ''),
(2, 5, 13, '');

-- --------------------------------------------------------

--
-- Table structure for table `serviceproviders`
--

CREATE TABLE `serviceproviders` (
  `mobile` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `business` varchar(50) NOT NULL,
  `category` varchar(500) NOT NULL,
  `address` varchar(500) NOT NULL,
  `timing` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `servicearea` varchar(500) NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `serviceproviders`
--

INSERT INTO `serviceproviders` (`mobile`, `email`, `password`, `business`, `category`, `address`, `timing`, `price`, `servicearea`, `state`, `city`, `status`) VALUES
('9876671860', 'amarjeetsingh00595@gmail.com', '123456', 'Carpentary', 'Carpenter', 'Jammu Katra', '10:00 am to 5:00pm', 200, 'All areas nearby katra jamu', 'Jammu & Kashmir', ' Jammu ', 'pending'),
('7905115732', 'harmanpreet904@gmail.com', '123456', 'Electrician', 'Electrician', 'Global Institute Amritsar,Punjab', '10:am to 5:00pm', 300, 'All Areas nearby Global Institutes', 'Punjab', ' Amritsar ', 'done'),
('9621827023', 'pharman984@gmail.com', '123456', 'Electrician', 'Electrician', 'All Types Of Electrician Work', '10:am to 5:00pm', 250, 'Amritsar CIty', 'Punjab', ' Amritsar ', 'done');

-- --------------------------------------------------------

--
-- Table structure for table `userenquiry`
--

CREATE TABLE `userenquiry` (
  `enquiryid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `message` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `mobile` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `photo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`mobile`, `email`, `password`, `address`, `city`, `photo`) VALUES
('7006436851', 'erharsh237@gmail.com', '605868', 'Global Institutes Batala Road Amritsar Jammu Highw', 'Amritsar', '1.jpg'),
('7905115732', 'harman123@yahoo.com', '611280', 'street14 Montarial,Canada', 'Montarial', 'Harman9.jpg'),
('7986271350', 'dilrajsandhu38@gmail.com', '651553', 'Adjacent Hotel Veenus 3,Queen,s Road Amritsar-Punj', 'Amritsar', '4.png'),
('9695330329', 'sandeepsand@gmail.com', '085690', 'Banda Shahjahanpur', 'Shahjahanpur', '2.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookingid`),
  ADD KEY `memail` (`memail`),
  ADD KEY `serviceid` (`serviceid`),
  ADD KEY `usermobile` (`usermobile`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`categoryname`);

--
-- Indexes for table `merchantservices`
--
ALTER TABLE `merchantservices`
  ADD PRIMARY KEY (`serviceid`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`id`),
  ADD KEY `serviceid` (`serviceid`);

--
-- Indexes for table `serviceproviders`
--
ALTER TABLE `serviceproviders`
  ADD PRIMARY KEY (`email`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `userenquiry`
--
ALTER TABLE `userenquiry`
  ADD PRIMARY KEY (`enquiryid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`mobile`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bookingid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT for table `merchantservices`
--
ALTER TABLE `merchantservices`
  MODIFY `serviceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userenquiry`
--
ALTER TABLE `userenquiry`
  MODIFY `enquiryid` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`memail`) REFERENCES `serviceproviders` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`serviceid`) REFERENCES `merchantservices` (`serviceid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`usermobile`) REFERENCES `users` (`mobile`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `merchantservices`
--
ALTER TABLE `merchantservices`
  ADD CONSTRAINT `merchantservices_ibfk_1` FOREIGN KEY (`email`) REFERENCES `serviceproviders` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rating`
--
ALTER TABLE `rating`
  ADD CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`serviceid`) REFERENCES `merchantservices` (`serviceid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `serviceproviders`
--
ALTER TABLE `serviceproviders`
  ADD CONSTRAINT `serviceproviders_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`categoryname`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
