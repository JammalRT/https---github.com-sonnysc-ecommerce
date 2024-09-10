<?php

// Obtener los datos de conexión
$host = "localhost";
$usuario = "root";
$contraseña = "Jammal12345";
$base_de_datos = "Citas_Medicas";

// Conectar a la base de datos
$conexion = mysqli_connect($host, $usuario, $contraseña, $base_de_datos);

// Comprobar la conexión
if (!$conexion) {
  die("Error al conectar a la base de datos: " . mysqli_connect_error());
}

// Obtener los datos del formulario
$nombre = $_POST["nombre"];

// Insertar los datos en la base de datos
$consulta = "INSERT INTO usuarios (nombre) VALUES ('$nombre')";

$resultado = mysqli_query($conexion, $consulta);

// Cerrar la conexión
mysqli_close($conexion);

?>