<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$mealCost);
fscanf($handle,"%d",$tipPercent);
fscanf($handle,"%d",$taxPercent);
$mealCost = round($mealCost);
$tip = $mealCost * $tipPercent / 100;
$tax = $mealCost * $taxPercent / 100;
$tip = round($tip);
$tax = round($tax);
$totalCost = $mealCost + $tip + $tax;
$total = round($totalCost);
print("The total meal cost is ".$total." dollars.");
