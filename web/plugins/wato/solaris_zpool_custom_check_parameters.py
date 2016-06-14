# (subgroup, checkgroup, title, valuespec, itemspec, matchtype, has_inventory=True, register_static_check=True)

register_check_parameters(
    _("Storage, Filesystems and Files"),
    "solaris_zpool",
    _("Solaris Zpool (used space and state)"),
    Dictionary(
        elements = [
            ("levels",
                Tuple(
                    title = _("Levels for Zpools usage"),
                    label = _("Levels for Zpools usage"),
                    elements = [
                        Percentage(title = _("Warning at:"), maxvalue = None),
                        Percentage(title = _("Critical at:"), maxvalue = None),
                    ]
                ),
            ),
            ("critical_state",
                TextAscii(
                    title = _("Critical zpool state"),
                    label = _("State string:"),
                    help  = _("State string as returned by zpool -H"),
                )
            )
        ],
        optional_keys=["critical_state"]
    ),
    TextAscii(
        title = _("Zpool name"),
        help  = _(""),
        allow_empty = True,
    ),
    "dict"
)
