register_check_parameters(
    _("Operating System Resources"),
    "solaris_ldom_stat",
    _("Solaris LDOM CPU Usage Levels"),
    Dictionary(
        elements = [
            ("cpu_levels",
                Tuple(
                    title = _("Levels for ldom cpu usage (%)"),
                    label = _("Levels for ldom cpu usage (%)"),
                    elements = [
                        Percentage(title = _("Warning at:" ), maxvalue = 1500.0),
                        Percentage(title = _("Critical at:"), maxvalue = 1500.0),
                    ]
                ),
            ),
            ("core_levels",
                Tuple(
                    title = _("Levels for ldom CORE usage (#.#)"),
                    label = _("Levels for ldom CORE usage (#.#)"),
                    elements = [
                        Float(title = _("Warning at:" ), maxvalue = 1000.0),
                        Float(title = _("Critical at:"), maxvalue = 1000.0),
                    ]
                ),
            ),
        ],
    ),
    TextAscii(
        title = _("LDOM Name"),
        help  = _(""),
        allow_empty = True,
    ),
    "dict"
)

