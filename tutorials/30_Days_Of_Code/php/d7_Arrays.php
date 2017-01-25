<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);
$arr_temp = fgets($handle);
$arr = explode(" ",$arr_temp);
array_walk($arr,'intval');
$raa = array_reverse($arr);
for ($i=0; $i<$n; $i++) {
    echo $raa[$i]." ";
}
echo "\n";
?>
