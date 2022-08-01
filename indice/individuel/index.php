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
        }
    p{width: 45em;}
    #post{text-align: center;}
</style>
</head>
<body>
    <main>
        <div id=ante>
        <h1>Simulateur d'entrée dans la grille LOPMI</h1>
        <form method="post" action="#">
            <label for="grade">Grade :</label>
            <select name="grade" id="grade">
                <option value="GENDARME">Gendarme</option>
                <option value="MDC">Maréchal des Logis</option>
                <option value="ADJ">Adjudant</option>
                <option value="ADC">Adjudant-chef</option>
                <option value="MJR">Major</option>
            </select>
            <p>
                <label for="aindice">Indice majoré :</label>
                <select name="aindice" id="aindice">
                </select>
                <label for="ancienneteechelon">Ancienneté dans l'échelon (en mois) : </label>
                <input type="number" name="ancienneteechelon" id="ancienneteechelon">
            </p>
            <p>
                <label for="ancienneteservicean">Ancienneté de service (Années) : </label>
                <input type="number" name="ancienneteservicean" id="ancienneteservicean">
                <label for="ancienneteservicemois">Ancienneté de service (Mois) : </label>
                <input type="number" name="ancienneteservicemois" id="ancienneteservicemois" max="12">
            </p>
            <input type="submit" value="Reclassement">
        </form>
        <hr>
        </div>
        <?php
        if(isset($grade)){
        $donnees = $grade." ".$aindice." ".$ancienneteechelon." ".$ancienneteservicean." ".$ancienneteservicemois;
        echo "<br>";
        $result = exec("python3 ../../cgi-bin/recalc3.py $donnees", $output, $result_code);
        foreach($output as $item){
        ?>
        <div id="post">
        <?php echo "<p>".$item."</p>";?>
        </p>
        <?php
        }
        }
        ?>
        </div>
    </main>
</body>
<script>
    var grade = $('select[name="grade"]').val();
    aindices_gnd=[343,348,353,364,379,391,401,411,422,435,454,477];
    aindices_mdc=[388,398,412,426,445,463,481];
    aindices_adj=[422,429,439,449,467,473,482,484,503];
    aindices_adc=[466,476,484,488,493,505,517,527,539];
    aindices_mjr=[495,515,536,550,564,574,590];
    $( document ).ready(function() {
        if(grade == "GENDARME"){
            $.each(aindices_gnd, function(val, text) {
            $('#aindice').append( $('<option></option>').val(text).html(text) )
            });
                }else if(grade == "MDC"){
                $.each(aindices_mdc, function(val, text) {
                $('#aindice').append( $('<option></option>').val(text).html(text) )
                });
                    }else if(grade == "ADJ"){
                    $.each(aindices_adj, function(val, text) {
                    $('#aindice').append( $('<option></option>').val(text).html(text) )
                    });
                        }else if(grade == "ADC"){
                        $.each(aindices_adc, function(val, text) {
                        $('#aindice').append( $('<option></option>').val(text).html(text) )
                        });
                            }else if(grade == "MJR"){
                            $.each(aindices_mjr, function(val, text) {
                            $('#aindice').append( $('<option></option>').val(text).html(text) )
                            });
                            }
        $('select[name="grade"').change(function () {
            location.reload();
        });
    });
</script>
</html>