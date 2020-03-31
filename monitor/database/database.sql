-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 31/03/2020 às 11:59
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
  `in-port` varchar(50) CHARACTER SET utf8 NOT NULL,
  `out-port` varchar(50) CHARACTER SET utf8 NOT NULL,
  `eth-src` varchar(17) CHARACTER SET utf8 NOT NULL,
  `eth-dst` varchar(17) CHARACTER SET utf8 NOT NULL,
  `packets` varchar(255) CHARACTER SET utf8 NOT NULL,
  `bytes` varchar(255) CHARACTER SET utf8 NOT NULL,
  `eth-type` int(11) DEFAULT NULL,
  `ip-proto` int(11) DEFAULT NULL,
  `ipv4-src` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `ipv4-dst` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `port-src` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `port-dst` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura para tabela `portStats`
--

CREATE TABLE `portStats` (
  `id` int(11) NOT NULL,
  `dpid` int(11) NOT NULL,
  `port_no` varchar(255) CHARACTER SET utf8 NOT NULL,
  `rx-packets` varchar(255) CHARACTER SET utf8 NOT NULL,
  `rx-bytes` varchar(255) CHARACTER SET utf8 NOT NULL,
  `rx-error` varchar(255) CHARACTER SET utf8 NOT NULL,
  `tx-packets` varchar(255) CHARACTER SET utf8 NOT NULL,
  `tx-bytes` varchar(255) CHARACTER SET utf8 NOT NULL,
  `tx-error` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de tabela `portStats`
--
ALTER TABLE `portStats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
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
