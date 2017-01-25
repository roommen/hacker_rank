<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
fscanf($_fp,"%d\n",$T);
for($j=0; $j<$T; $j++) {
    fscanf($_fp, "%s\n", $S);
    $A = str_split($S);
    $N = count($A);
    for ($i=0;$i<$N;$i = $i+2) {
        echo $A[$i];
    }
    echo " ";
    for ($i=1;$i<$N;$i = $i+2) {
        echo $A[$i];
    }
    echo "\n";
}


?>
