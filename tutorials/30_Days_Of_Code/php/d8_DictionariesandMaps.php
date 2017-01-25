<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
fscanf($_fp,"%d",$n);
$phonebook = array();
for ($i=0; $i<$n; $i++) {
    fscanf($_fp,"%s %s",$key,$value);
    $phonebook[$key] = $value;
}
while($person = trim(fgets($_fp))){
    if (array_key_exists($person, $phonebook)) {
        echo $person."=".$phonebook[$person]."\n";
    } else {
        echo "Not found\n";
    }
    
}
?>
