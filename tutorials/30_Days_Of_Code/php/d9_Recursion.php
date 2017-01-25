<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
fscanf($_fp,"%d",$n);
function factorial($x) {
    if ($x <= 1) return 1;
    else return $x * factorial($x - 1);
}
echo factorial($n);
?>
