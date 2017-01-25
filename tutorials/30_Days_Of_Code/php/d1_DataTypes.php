<?php
// Declare second integer, double, and String variables.
$vi = 0;
$vd = 0.0;
$vs = "";
// Read and save an integer, double, and String to your variables.
fscanf($handle,"%d\n",$vi);
fscanf($handle,"%lf\n",$vd);
fscanf($handle,"%[^\n]\n",$vs);
// Print the sum of both integer variables on a new line.
printf("%d\n", ($i + $vi)).PHP_EOL;
// Print the sum of the double variables on a new line.
printf("%.1lf\n", ($d + $vd)).PHP_EOL;
// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.
printf("%s\n", ($s.$vs)).PHP_EOL;
