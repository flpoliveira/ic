-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 25/03/2020 às 08:04
-- Versão do servidor: 5.7.29-0ubuntu0.18.04.1
-- Versão do PHP: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `database`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `flowStats`
--

CREATE TABLE `flowStats` (
  `id` int(11) NOT NULL,
  `dpid` int(11) NOT NULL,
  `in-port` int(11) NOT NULL,
  `eth-dst` varchar(17) NOT NULL,
  `out-port` int(11) NOT NULL,
  `packets` int(11) NOT NULL,
  `bytes` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `flowStats`
--

INSERT INTO `flowStats` (`id`, `dpid`, `in-port`, `eth-dst`, `out-port`, `packets`, `bytes`, `insertedTime`, `updatedTime`) VALUES
(1, 1, 1, '00:00:00:00:00:02', 2, 5, 434, '2020-03-25 10:53:12', '2020-03-25 10:53:12'),
(2, 1, 2, '00:00:00:00:00:01', 1, 6, 532, '2020-03-25 10:53:12', '2020-03-25 10:53:12'),
(3, 1, 1, '00:00:00:00:00:02', 2, 6, 532, '2020-03-25 10:53:22', '2020-03-25 10:53:22'),
(4, 1, 2, '00:00:00:00:00:01', 1, 7, 630, '2020-03-25 10:53:22', '2020-03-25 10:53:22');

-- --------------------------------------------------------

--
-- Estrutura para tabela `portStats`
--

CREATE TABLE `portStats` (
  `id` int(11) NOT NULL,
  `dpid` int(11) NOT NULL,
  `port_no` varchar(255) NOT NULL,
  `rx-packets` int(11) NOT NULL,
  `rx-bytes` int(11) NOT NULL,
  `rx-error` int(11) NOT NULL,
  `tx-packets` int(11) NOT NULL,
  `tx-bytes` int(11) NOT NULL,
  `tx-error` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `portStats`
--

INSERT INTO `portStats` (`id`, `dpid`, `port_no`, `rx-packets`, `rx-bytes`, `rx-error`, `tx-packets`, `tx-bytes`, `tx-error`, `insertedTime`, `updatedTime`) VALUES
(1, 1, '1', 37, 3222, 0, 72, 5964, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(2, 1, '2', 37, 3222, 0, 74, 6120, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(3, 1, '3', 29, 2318, 0, 31, 2414, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(4, 2, '1', 31, 2414, 0, 29, 2318, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(5, 2, '2', 12, 996, 0, 50, 3936, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(6, 2, '3', 11, 926, 0, 51, 4006, 0, '2020-03-25 10:42:53', '2020-03-25 10:42:53'),
(7, 1, '1', 37, 3222, 0, 74, 6104, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(8, 1, '2', 37, 3222, 0, 75, 6190, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(9, 1, '3', 30, 2388, 0, 31, 2414, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(10, 2, '1', 31, 2414, 0, 30, 2388, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(11, 2, '2', 12, 996, 0, 51, 4006, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(12, 2, '3', 12, 996, 0, 52, 4076, 0, '2020-03-25 10:43:03', '2020-03-25 10:43:03'),
(13, 1, '1', 37, 3222, 0, 75, 6146, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(14, 1, '2', 42, 3600, 0, 80, 6568, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(15, 1, '3', 35, 2766, 0, 36, 2792, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(16, 2, '1', 36, 2792, 0, 35, 2766, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(17, 2, '2', 17, 1374, 0, 56, 4384, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(18, 2, '3', 12, 996, 0, 53, 4118, 0, '2020-03-25 10:44:13', '2020-03-25 10:44:13'),
(19, 1, '1', 38, 3292, 0, 75, 6146, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(20, 1, '2', 42, 3600, 0, 81, 6638, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(21, 1, '3', 35, 2766, 0, 37, 2862, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(22, 2, '1', 37, 2862, 0, 35, 2766, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(23, 2, '2', 17, 1374, 0, 57, 4454, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(24, 2, '3', 12, 996, 0, 54, 4188, 0, '2020-03-25 10:44:23', '2020-03-25 10:44:23'),
(25, 1, '1', 38, 3292, 0, 77, 6286, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(26, 1, '2', 43, 3670, 0, 82, 6708, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(27, 1, '3', 36, 2836, 0, 38, 2932, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(28, 2, '1', 38, 2932, 0, 36, 2836, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(29, 2, '2', 18, 1444, 0, 59, 4594, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(30, 2, '3', 12, 996, 0, 56, 4328, 0, '2020-03-25 10:44:33', '2020-03-25 10:44:33'),
(31, 1, '1', 17, 1458, 0, 25, 1978, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(32, 1, '2', 17, 1458, 0, 25, 1978, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(33, 1, '3', 12, 936, 0, 13, 978, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(34, 2, '1', 13, 978, 0, 12, 936, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(35, 2, '2', 9, 786, 0, 17, 1278, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(36, 2, '3', 9, 786, 0, 17, 1278, 0, '2020-03-25 10:53:13', '2020-03-25 10:53:13'),
(37, 1, '1', 18, 1528, 0, 30, 2328, 0, '2020-03-25 10:53:32', '2020-03-25 10:53:32'),
(38, 1, '2', 18, 1528, 0, 30, 2328, 0, '2020-03-25 10:53:32', '2020-03-25 10:53:32'),
(39, 1, '3', 15, 1146, 0, 16, 1188, 0, '2020-03-25 10:53:33', '2020-03-25 10:53:33'),
(40, 2, '1', 16, 1188, 0, 15, 1146, 0, '2020-03-25 10:53:33', '2020-03-25 10:53:33'),
(41, 2, '2', 10, 856, 0, 22, 1628, 0, '2020-03-25 10:53:33', '2020-03-25 10:53:33'),
(42, 2, '3', 10, 856, 0, 22, 1628, 0, '2020-03-25 10:53:33', '2020-03-25 10:53:33'),
(43, 2, '1', 19, 1398, 0, 18, 1356, 0, '2020-03-25 10:54:02', '2020-03-25 10:54:02'),
(44, 2, '2', 11, 926, 0, 27, 1978, 0, '2020-03-25 10:54:02', '2020-03-25 10:54:02'),
(45, 2, '3', 11, 926, 0, 26, 1908, 0, '2020-03-25 10:54:03', '2020-03-25 10:54:03'),
(46, 1, '1', 19, 1598, 0, 35, 2678, 0, '2020-03-25 10:54:03', '2020-03-25 10:54:03'),
(47, 1, '2', 19, 1598, 0, 35, 2678, 0, '2020-03-25 10:54:03', '2020-03-25 10:54:03'),
(48, 1, '3', 18, 1356, 0, 19, 1398, 0, '2020-03-25 10:54:03', '2020-03-25 10:54:03'),
(49, 2, '3', 11, 926, 0, 27, 1978, 0, '2020-03-25 10:54:12', '2020-03-25 10:54:12');

-- --------------------------------------------------------

--
-- Estrutura para tabela `switch`
--

CREATE TABLE `switch` (
  `dpid` int(11) NOT NULL,
  `n_buffers` int(11) NOT NULL,
  `n_tables` int(11) NOT NULL,
  `auxiliary_id` int(11) NOT NULL,
  `capabilities` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `switch`
--

INSERT INTO `switch` (`dpid`, `n_buffers`, `n_tables`, `auxiliary_id`, `capabilities`, `insertedTime`, `updatedTime`) VALUES
(1, 0, 254, 0, 79, '2020-03-24 23:26:18', '2020-03-24 23:26:18'),
(2, 0, 254, 0, 79, '2020-03-24 23:26:18', '2020-03-24 23:26:18');

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `flowStats`
--
ALTER TABLE `flowStats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dpid` (`dpid`);

--
-- Índices de tabela `portStats`
--
ALTER TABLE `portStats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dpid` (`dpid`);

--
-- Índices de tabela `switch`
--
ALTER TABLE `switch`
  ADD PRIMARY KEY (`dpid`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `flowStats`
--
ALTER TABLE `flowStats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de tabela `portStats`
--
ALTER TABLE `portStats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `flowStats`
--
ALTER TABLE `flowStats`
  ADD CONSTRAINT `flowStats_ibfk_1` FOREIGN KEY (`dpid`) REFERENCES `switch` (`dpid`);

--
-- Restrições para tabelas `portStats`
--
ALTER TABLE `portStats`
  ADD CONSTRAINT `portStats_ibfk_1` FOREIGN KEY (`dpid`) REFERENCES `switch` (`dpid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
