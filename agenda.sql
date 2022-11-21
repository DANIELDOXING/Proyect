-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2022 a las 21:49:06
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comenta`
--

CREATE TABLE `comenta` (
  `id` int(3) NOT NULL,
  `correo` varchar(35) NOT NULL,
  `comentarios` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `comenta`
--

INSERT INTO `comenta` (`id`, `correo`, `comentarios`) VALUES
(4, 'r@gmail.hahsjhsa', 'swqjiohq'),
(9, 'diego@gmail.com', 'HASHSAJHASK'),
(12, 'u@yuyiuyiuy', 'swqjiohq');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `code` varchar(255) NOT NULL,
  `name` varchar(70) NOT NULL,
  `image` varchar(255) NOT NULL,
  `category` varchar(70) NOT NULL,
  `price` int(11) NOT NULL,
  `discount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `product`
--

INSERT INTO `product` (`pid`, `code`, `name`, `image`, `category`, `price`, `discount`) VALUES
(1, 'EDNALAN01', 'Jordan-grandesote', '1.jpg', 'Tenis', 120, 5),
(2, 'EDNALAN02', 'Tenis-chidos', '2.jpg', 'Zapatillas', 2300, 5),
(3, 'EDNALAN03', 'Papu-tenis', '3.jpg', 'Tenis', 3000, 5),
(4, 'EDNALAN04', 'Papos-cars', '4.jpg', 'Papos', 1000, 5),
(5, 'EDNALAN05', 'Crocs_de_Shrek', '5.jpg', 'Crocs-Chanclas', 9999999, 5),
(6, 'EDNALAN06', 'Papos-Cars-con-lucesitas', '6.jpg', 'Papos-y-mas', 1500, 5),
(7, 'EDNALAN07', 'CROCS-DE-VILLERO-PAPAAAAAA', '7.jpg', 'crocs-y-mas', 49999, 5),
(8, 'EDNALAN08', 'Tenis-rotos', '9.jpg', 'Segunda-mano', 10000, 5),
(9, 'EDNALAN09', 'Tenis-que-uso-el-bicho', '9.jpg', 'El-bicho-siu', 777777, 5),
(10, 'EDNALAN10', 'Tenis-colaboracion-Doritos', '10.jpg', 'Colaboraciones-epicas', 123123, 5),
(11, 'EDNALAN11', 'Crocs-Botellas-de-plástico', '11.jpg', 'Reciclados', 500000, 5),
(12, 'EDNALAN12', 'Pan-tuflas-Gucci', '12.jpg', 'Panaderia-comestible', 20000, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `r_empresa`
--

CREATE TABLE `r_empresa` (
  `id` int(3) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contrasena` varchar(50) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `r_empresa`
--

INSERT INTO `r_empresa` (`id`, `correo`, `contrasena`, `nombre`) VALUES
(1, 'rdzdiegooo72@gmail.com', '1233', ''),
(2, 'rdz@gmail.com', '123', 'RICARDO ALBERTO ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tenis`
--

CREATE TABLE `tenis` (
  `idTenis` int(5) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `fechanac` date NOT NULL,
  `sexo` varchar(11) NOT NULL,
  `telefono` int(10) NOT NULL,
  `correo` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tenis`
--

INSERT INTO `tenis` (`idTenis`, `nombre`, `apellidos`, `fechanac`, `sexo`, `telefono`, `correo`) VALUES
(5, 'Nike, talla 7', 'Diego', '0122-12-12', 'Indistinto', 12212, 'rdzdiego72@');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comenta`
--
ALTER TABLE `comenta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- Indices de la tabla `r_empresa`
--
ALTER TABLE `r_empresa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tenis`
--
ALTER TABLE `tenis`
  ADD PRIMARY KEY (`idTenis`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comenta`
--
ALTER TABLE `comenta`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `r_empresa`
--
ALTER TABLE `r_empresa`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tenis`
--
ALTER TABLE `tenis`
  MODIFY `idTenis` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
