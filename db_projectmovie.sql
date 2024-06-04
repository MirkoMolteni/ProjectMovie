-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Giu 04, 2024 alle 08:09
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_projectmovie`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `tipi`
--

CREATE TABLE `tipi` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `tipi`
--

INSERT INTO `tipi` (`ID`, `Nome`) VALUES
(1, 'Sto guardando'),
(2, 'Completato'),
(3, 'Da vedere'),
(4, 'Droppato');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `ID` int(11) NOT NULL,
  `Username` varchar(32) NOT NULL,
  `Password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`ID`, `Username`, `Password`) VALUES
(1, 'test', '098f6bcd4621d373cade4e832627b4f6'),
(2, 'Frittella12', '7e82b9af1f886f4fb7d8881f2c6416e3');

-- --------------------------------------------------------

--
-- Struttura della tabella `watchlist`
--

CREATE TABLE `watchlist` (
  `ID` int(11) NOT NULL,
  `IDUtente` int(11) NOT NULL,
  `IDFilm` int(11) NOT NULL,
  `IDTipo` int(11) NOT NULL DEFAULT 3,
  `NomeFilm` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `watchlist`
--

INSERT INTO `watchlist` (`ID`, `IDUtente`, `IDFilm`, `IDTipo`, `NomeFilm`) VALUES
(1, 1, 235044, 3, 'Un fantasma per amico'),
(2, 1, 929590, 2, 'Civil War'),
(3, 1, 693134, 2, 'Dune - Parte due'),
(4, 2, 385687, 3, 'Fast X'),
(5, 2, 653346, 2, 'Il regno del pianeta delle scimmie');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `tipi`
--
ALTER TABLE `tipi`
  ADD PRIMARY KEY (`ID`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`ID`);

--
-- Indici per le tabelle `watchlist`
--
ALTER TABLE `watchlist`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK1_watch` (`IDTipo`),
  ADD KEY `FK2_watch` (`IDUtente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `tipi`
--
ALTER TABLE `tipi`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `utenti`
--
ALTER TABLE `utenti`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `watchlist`
--
ALTER TABLE `watchlist`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `watchlist`
--
ALTER TABLE `watchlist`
  ADD CONSTRAINT `FK1_watch` FOREIGN KEY (`IDTipo`) REFERENCES `tipi` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK2_watch` FOREIGN KEY (`IDUtente`) REFERENCES `utenti` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
