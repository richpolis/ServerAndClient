-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.6.25-log


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema gv_solo_tablas_basicas
--

CREATE DATABASE IF NOT EXISTS gv_solo_tablas_basicas;
USE gv_solo_tablas_basicas;

--
-- Definition of table `tabla_862894021949113`
--

DROP TABLE IF EXISTS `tabla_862894021949113`;
CREATE TABLE `tabla_862894021949113` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Tipo_Dispositivo` varchar(255) DEFAULT NULL,
  `Protocolo_Version` varchar(255) DEFAULT NULL,
  `Version_Hardware` varchar(255) DEFAULT NULL,
  `Version_Software` varchar(255) DEFAULT NULL,
  `IMEI` varchar(255) DEFAULT '862894021949113',
  `Nombre_Dispositivo` varchar(255) DEFAULT NULL,
  `Reporte_ ID_Reporte_Type` varchar(255) DEFAULT NULL,
  `Number` int(10) unsigned DEFAULT '0',
  `Heading` varchar(255) DEFAULT NULL,
  `Fecha_Envio` varchar(255) DEFAULT NULL,
  `Hora_Envio` varchar(255) DEFAULT NULL,
  `Count_Number` varchar(255) DEFAULT NULL,
  `Tail_Character` varchar(255) DEFAULT NULL,
  `ICCID` varchar(255) DEFAULT NULL,
  `Alerta` varchar(255) DEFAULT NULL,
  `Last_Fix_UTC_Time` varchar(255) DEFAULT NULL,
  `Report_Composition_Mask` varchar(255) DEFAULT NULL,
  `Azimuth` varchar(255) DEFAULT NULL,
  `Altitud` varchar(255) DEFAULT NULL,
  `Precision_GPS` double DEFAULT '0',
  `Velocidad` double DEFAULT '0',
  `Longitud` double DEFAULT '0',
  `Latitud` double DEFAULT '0',
  `GPS_UTC_Time` varchar(255) DEFAULT NULL,
  `Estado_Movimiento_Actual` varchar(255) DEFAULT NULL,
  `Kilometraje` double DEFAULT '0',
  `Tiempo_Acumulado_Encendido` varchar(255) DEFAULT NULL,
  `Curso` double DEFAULT '0',
  `LAC` varchar(255) DEFAULT NULL,
  `MCC` varchar(255) DEFAULT NULL,
  `MNC` varchar(255) DEFAULT NULL,
  `Cell_ID` varchar(255) DEFAULT NULL,
  `CSQ_RSSI` varchar(255) DEFAULT NULL,
  `CSQ_BER` varchar(255) DEFAULT NULL,
  `Fuente_Corriente_Externa` varchar(255) DEFAULT NULL,
  `Prcentaje_Bateria_Backup` varchar(255) DEFAULT NULL,
  `Corriente_Externa_VCC` double DEFAULT '0',
  `Bateria_Backup_VCC` double DEFAULT '0',
  `Charging` varchar(255) DEFAULT NULL,
  `Entrada_Analogica_1` double DEFAULT '0',
  `Entrada_Analogica_2` double DEFAULT '0',
  `Entrada_Analogica_VCC` varchar(255) DEFAULT NULL,
  `Mode_Pin_l5` varchar(255) DEFAULT NULL,
  `Entrada_Analogica_VCC1` double DEFAULT '0',
  `Entrada_Analogica_VCC2` double DEFAULT '0',
  `Entrada_Digital` varchar(255) DEFAULT NULL,
  `Salida_Digital` varchar(255) DEFAULT NULL,
  `LED_On` varchar(255) DEFAULT NULL,
  `GPS_On_Need` varchar(255) DEFAULT NULL,
  `Antena_GPS_Externa` varchar(255) DEFAULT NULL,
  `Time_Zone_Offset` varchar(255) DEFAULT NULL,
  `Daylight_Saving` varchar(255) DEFAULT NULL,
  `Call_Number` varchar(255) DEFAULT NULL,
  `Stealthy_Phone_Number_Incoming_call_Number` varchar(255) DEFAULT NULL,
  `MON_Type` varchar(255) DEFAULT NULL,
  `Duration_of_Ignition_Off` varchar(255) DEFAULT NULL,
  `Stealthy_Microphone` varchar(255) DEFAULT NULL,
  `Stealthy_Speaker` varchar(255) DEFAULT NULL,
  `Duration_of_Id1ing_Status` varchar(255) DEFAULT NULL,
  `Duration_of_Ignition_On` varchar(255) DEFAULT NULL,
  `Motion_State` varchar(255) DEFAULT NULL,
  `Comandos_entrada` varchar(255) DEFAULT NULL,
  `Comandos_salida` varchar(255) DEFAULT NULL,
  `fecha_servidor` varchar(255) DEFAULT NULL,
  `hora_servidor` varchar(255) DEFAULT NULL,
  `Estatus_Dispositivo` varchar(255) DEFAULT NULL,
  `State` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id` (`Id`),
  KEY `Cell_ID` (`Cell_ID`),
  KEY `ICCID` (`ICCID`)
) ENGINE=InnoDB AUTO_INCREMENT=559479 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tabla_862894021949113`
--

/*!40000 ALTER TABLE `tabla_862894021949113` DISABLE KEYS */;
/*!40000 ALTER TABLE `tabla_862894021949113` ENABLE KEYS */;


--
-- Definition of trigger `tabla_862894021949113_AFTER_INSERT`
--

DROP TRIGGER /*!50030 IF EXISTS */ `tabla_862894021949113_AFTER_INSERT`;

DELIMITER $$

CREATE DEFINER = `root`@`%` TRIGGER `tabla_862894021949113_AFTER_INSERT` AFTER INSERT ON `tabla_862894021949113` FOR EACH ROW BEGIN
	IF NEW.Alerta != 'Rastreo' THEN
		INSERT INTO alertas
		(IMEI,Nombre_Dispositivo,Alerta,fecha,hora,Latitud,Longitud,id_tabla_imei,status)
		VALUES(NEW.IMEI,NEW.Nombre_Dispositivo,NEW.Alerta, NEW.fecha_servidor, NEW.hora_servidor, NEW.Latitud, NEW.Longitud, NEW.Id, NEW.state);
	END IF;

END $$

DELIMITER ;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
