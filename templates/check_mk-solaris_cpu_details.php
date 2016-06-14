<?php

setlocale(LC_ALL, "POSIX");

$opt[1] = "--vertical-label \"Context Switches" title \"$servicedesc\" ";
$def[1]  = "DEF:used=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:used#2080ff:\"Usage\:\" ";
$def[1] .= "GPRINT:used:LAST:\"%.2lf%%\" ";
$def[1] .= "LINE1:used#000080:\"\" ";
$def[1] .= "GPRINT:used:MAX:\"(Max\: %.2lf%%,\" ";
$def[1] .= "GPRINT:used:AVERAGE:\"Avg\: %.2lf%%)\" ";
if ($WARN[1] != "") {
    $def[1] .= "HRULE:$WARN[1]#FFFF00:\"Warning\: $WARN[1]%\" ";
    $def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1]%\" ";
}

$opt[3] = "--vertical-label \"Context Switches" title \"$servicedesc\" ";
$def[3]  = "DEF:used=$RRDFILE[3]:$DS[3]:MAX ";
$def[3] .= "AREA:used#2080ff:\"Usage\:\" ";
$def[3] .= "GPRINT:used:LAST:\"%.2lf%%\" ";
$def[3] .= "LINE1:used#000080:\"\" ";
$def[3] .= "GPRINT:used:MAX:\"(Max\: %.2lf%%,\" ";
$def[3] .= "GPRINT:used:AVERAGE:\"Avg\: %.2lf%%)\" ";
if ($WARN[3] != "") {
    $def[3] .= "HRULE:$WARN[3]#FFFF00:\"Warning\: $WARN[3]%\" ";
    $def[3] .= "HRULE:$CRIT[3]#FF0000:\"Critical\: $CRIT[3]%\" ";
}

$opt[5] = "--vertical-label \"Context Switches" title \"$servicedesc\" ";
$def[5]  = "DEF:used=$RRDFILE[5]:$DS[5]:MAX ";
$def[5] .= "AREA:used#2080ff:\"Usage\:\" ";
$def[5] .= "GPRINT:used:LAST:\"%.2lf%%\" ";
$def[5] .= "LINE1:used#000080:\"\" ";
$def[5] .= "GPRINT:used:MAX:\"(Max\: %.2lf%%,\" ";
$def[5] .= "GPRINT:used:AVERAGE:\"Avg\: %.2lf%%)\" ";
if ($WARN[5] != "") {
    $def[5] .= "HRULE:$WARN[5]#FFFF00:\"Warning\: $WARN[5]%\" ";
    $def[5] .= "HRULE:$CRIT[5]#FF0000:\"Critical\: $CRIT[5]%\" ";
}

?>

