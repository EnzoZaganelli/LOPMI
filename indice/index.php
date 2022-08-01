<!DOCTYPE html>
<?php
if(isset($_POST['grade'])){
$grade=$_POST['grade'];
$aindice=$_POST['aindice'];
$ancienneteechelon=$_POST['ancienneteechelon'];
$ancienneteservicean=$_POST['ancienneteservicean'];
$ancienneteservicemois=$_POST['ancienneteservicemois'];
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
        text-align: center;
        }
    button {
        margin : 0.5em;
    }
</style>
</head>
<body>
    <main>
        <div>
            <p>Veuillez choisir quel calculateur vous souhaitez utiliser :<p>
            <p><a href="individuel/"><button>Individuel</button></a><a href="groupe/"><button>Groupe</button></a></p>
        </div>
    </main>
</body>
</html>