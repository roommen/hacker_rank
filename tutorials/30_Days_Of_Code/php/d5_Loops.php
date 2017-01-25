<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);
for ($i = 1; $i<=10; $i++) {
    echo $n ." x ". $i ." = ". ($n*$i)."\n";
}
?>
