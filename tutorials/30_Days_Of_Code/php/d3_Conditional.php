<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$N);
if ($N%2 != 0) 
    print("Weird");
else 
    if ($N >=2 && $N <= 5)
        print("Not Weird");
    else if ($N >=6 && $N<=20)
        print("Weird");
    else 
        print("Not Weird");
?>
