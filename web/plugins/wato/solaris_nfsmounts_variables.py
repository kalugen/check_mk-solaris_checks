

register_rule("checkparams" + "/" +  _("Inventory - automatic service detection"),
    varname   = "inventory_nfsmounts",
    title     = _("Solaris nfsmount discovery "),
    valuespec = Dictionary(
        elements = [
          ('nfs_allowed', ListOfStrings(
                title = _("Included mount points"),
                help  = _('Full name of the mount points to be considered.'),
                orientation = "horizontal",
                )),
          ('nfs_ignored', ListOfStrings(
                title = _("Excluded mount points"),
                help  = _('Full name of the mount points to be excluded.'),
                orientation = "horizontal",
                )),
        ],
    ),
  match= 'all',
)

