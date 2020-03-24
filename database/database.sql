-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 24/03/2020 às 13:10
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
  `switch_id` int(11) NOT NULL,
  `datapath` varchar(255) NOT NULL,
  `in-port` int(11) NOT NULL,
  `out-port` int(11) NOT NULL,
  `eth-dst` varchar(18) NOT NULL,
  `packets` int(11) NOT NULL,
  `bytes` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura para tabela `portStats`
--

CREATE TABLE `portStats` (
  `id` int(11) NOT NULL,
  `switch_id` int(11) NOT NULL,
  `datapath` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `rx-pkts` int(11) NOT NULL,
  `rx-bytes` int(11) NOT NULL,
  `rx-error` int(11) NOT NULL,
  `tx-pkts` int(11) NOT NULL,
  `tx-bytes` int(11) NOT NULL,
  `tx-error` int(11) NOT NULL,
  `insertedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura para tabela `switch`
--

CREATE TABLE `switch` (
  `id` int(11) NOT NULL,
  `auxiliary_id` int(11) NOT NULL,
  `n_tables` int(11) NOT NULL,
  `n_buffers` int(11) NOT NULL,
  `datapath_id` int(11) NOT NULL,
  `capabilities` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `flowStats`
--
ALTER TABLE `flowStats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `switch_id` (`switch_id`);

--
-- Índices de tabela `portStats`
--
ALTER TABLE `portStats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `switch_id` (`switch_id`);

--
-- Índices de tabela `switch`
--
ALTER TABLE `switch`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT de tabela `switch`
--
ALTER TABLE `switch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `flowStats`
--
ALTER TABLE `flowStats`
  ADD CONSTRAINT `flowStats_ibfk_1` FOREIGN KEY (`switch_id`) REFERENCES `switch` (`id`);

--
-- Restrições para tabelas `portStats`
--
ALTER TABLE `portStats`
  ADD CONSTRAINT `portStats_ibfk_1` FOREIGN KEY (`switch_id`) REFERENCES `switch` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
