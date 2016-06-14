register_check_parameters(
    _("Operating System Resources"),
    "solaris_zone_stat",
    _("Solaris Zone CPU and Memory Usage Levels"),
    Dictionary(
        elements = [
            ("cpu_levels",
                Tuple(
                    title = _("Levels for zone cpu usage"),
                    label = _("Levels for zone cpu usage"),
                    elements = [
                        Percentage(title = _("Warning at:"), maxvalue = None),
                        Percentage(title = _("Critical at:"), maxvalue = None),
                    ]
                ),
            ),
            ("mem_levels",
                Tuple(
                    title = _("Levels for zone mem usage"),
                    label = _("Levels for zone mem usage"),
                    elements = [
                        Percentage(title = _("Warning at:"), maxvalue = None),
                        Percentage(title = _("Critical at:"), maxvalue = None),
                    ]
                ),
            ),

        ],
    ),
    TextAscii(
        title = _("Zone Name"),
        help  = _(""),
        allow_empty = True,
    ),
    "dict"
)

