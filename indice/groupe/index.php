<!DOCTYPE html>
<?php

$chemin = "/var/www/html/cimm/indice/groupe";

if(isset($_FILES['fichier'])){   
$fileInput="FileInput.csv";
move_uploaded_file($_FILES['fichier']['tmp_name'],"$chemin/$fileInput");
exec("python3 ../../cgi-bin/brecalc.py");
}
?>

<html>
<head>
    <meta charset="UTF-8">
    <title>Calculette indice Gendermarie</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <style>
    body {background-color: #d6e0f3;}
    main {background-color: whitesmoke;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        padding-left: 4em;
        padding-right: 4em;
        border : 1px solid black;
        border-radius : 15%;
        }
    p{width: 45em;}
    #post{text-align: center;}
</style>
</head>
<body>
    <main>
        <div id=ante>
        <h1>Simulateur d'entrée dans la grille LOPMI</h1>
        <form method="post" action="#" enctype="multipart/form-data">
            <fieldset>
            <label for="fichier"> Téléverser votre grille :</label>
            <input type="file" id="fichier" name="fichier">
            </fieldset>
            <input type="submit" value="Reclassement">
        </form>
        <hr>
        </div>
        <?php
        if(isset($fileInput)){
        echo "<br>";
            ?>
            <div id="post">
            <?php echo "<a href='FileOutput.csv' download><p>Votre fichier :</p></a>";?>
            </p>
            <?php
            }
            ?>
        </div>
    </main>
</body>
<script>
</script>
</html>