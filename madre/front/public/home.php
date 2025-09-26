<?php
include('../layout/parte1.php');
$src_gato_truco = "https://i.ytimg.com/vi/etxjQPVtE5s/hqdefault.jpg?sqp=-oaymwEmCOADEOgC8quKqQMa8AEB-AHKA4AC6AKKAgwIABABGGIgRihyMA8=&rs=AOn4CLBFKL_LxLCXg5JvjKNbn0ay114F4w";
?>

<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <div class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1 class="m-0">Inicio</h1>
                </div><!-- /.col -->
            </div><!-- /.row -->
        </div><!-- /.container-fluid -->
    </div>
    <!-- /.content-header -->

    <!-- Main content -->

    <!-- Contenedor principal -->
    <div class="_custom-main-container">
        <!-- Contendor de filas -->
        <div class="_custom-main-rows-container">
            <!-- Contenedor de cartas -->
            <div class="_custom-main-cards-container">
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Alumnos</h3>
                    </div>
                </button>
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Personal</h3>
                    </div>
                </button>
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Grupos</h3>
                    </div>
                </button>
            </div>
            <!-- Contenedor de cartas -->
            <div class="_custom-main-cards-container">
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Módulos</h3>
                    </div>
                </button>
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Inventario</h3>
                    </div>
                </button>
                <!-- Carta -->
                <button class="_custom-main-card-button">
                    <div class="_custom-main-card-container">
                        <img src=<?= $src_gato_truco; ?> alt="">
                        <h3>Administración</h3>
                    </div>
                </button>
            </div>
        </div>
    </div>

    <!-- /.content -->
</div>
<!-- /.content-wrapper -->

<?php
include('../layout/parte2.php');
?>