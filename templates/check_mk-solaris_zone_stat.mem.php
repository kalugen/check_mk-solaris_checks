<?php

# this file is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

setlocale(LC_ALL, "POSIX");

$opt[1] = "--vertical-label \"Used %\" -l 0 -u 100 --title \"$servicedesc usage\" ";

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

?>
