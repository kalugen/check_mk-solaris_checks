# Very simple perf-o-meter
def perfometer_check_mk_solaris_zone_stat(row, check_command, perf_data):
    left = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])

    red    = "#ff0000"
    yellow = "#ffff00"
    green  = "#00ff00"

    if left >= crit:
        color = red

    elif left >= warn:
        color = yellow
        
    else:
        color = green

    return "%.0f%%" % left, perfometer_linear(left, color)

perfometers["check_mk-solaris_zone_stat.cpu"] = perfometer_check_mk_solaris_zone_stat
perfometers["check_mk-solaris_zone_stat.mem"] = perfometer_check_mk_solaris_zone_stat
