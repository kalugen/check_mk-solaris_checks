register_rule("checkparams" + "/" +  _("Inventory - automatic service detection"),
    varname   = "inventory_solaris_extend_processes_rules",
    title     = _('Solaris Process Discovery'),
    help      = _("This ruleset defines criteria for automatically creating checks based on 7usr/ucb/ps for running processes "
                  "based upon what is running when the service discovery is done. "),
    #valuespec = Transform(
    valuespec =  Dictionary(
            elements = [
                ('descr', TextAscii(
                    title = _('Process Name'),
                    style = "dropdown",
                    allow_empty = False,
                    help  = _('<p>The process name may contain one or more occurances of <tt>%s</tt>. If you do this, then the pattern must be a regular '
                              'expression and be prefixed with ~. For each <tt>%s</tt> in the description, the expression has to contain one "group". A group '
                              'is a subexpression enclosed in brackets, for example <tt>(.*)</tt> or <tt>([a-zA-Z]+)</tt> or <tt>(...)</tt>. When the inventory finds a process '
                              'matching the pattern, it will substitute all such groups with the actual values when creating the check. That way one '
                              'rule can create several checks on a host.</p>'
                              '<p>If the pattern contains more groups then occurrances of <tt>%s</tt> in the service description then only the first matching '
                              'subexpressions  are used for the  service descriptions. The matched substrings corresponding to the remaining groups '
                              'are copied into the regular expression, nevertheless.</p>'
                              '<p>As an alternative to <tt>%s</tt> you may also use <tt>%1</tt>, <tt>%2</tt>, etc. '
                              'These will be replaced by the first, second, ... matching group. This allows you to reorder things.</p>'
                              ),
                )),
                ('match', Alternative(
                    title = _("Process Matching"),
                    style = "dropdown",
                    elements = [
                        TextAscii(
                            title = _("Exact name of the process and its arguments"),
                            label = _("Executable:"),
                            size = 50,
                        ),
                        Transform(
                            RegExp(size = 50),
                            title = _("Regular expression matching command line"),
                            label = _("Command line:"),
                            help = _("This regex must match the <i>beginning</i> of the complete "
                                     "command line of the process including arguments"),
                            forth = lambda x: x[1:],   # remove ~
                            back  = lambda x: "~" + x, # prefix ~
                        ),
                        FixedValue(
                            None,
                            totext = "",
                            title = _("Match all processes"),
                        )
                    ],
                    match = lambda x: (not x and 2) or (x[0] == '~' and 1 or 0),
                    default_value = '/usr/sbin/foo',
                )),
                ('levels', Tuple(
                    title = _('Levels for process count'),
                    help = _("Please note that if you specify and also if you modify levels here, the change is activated "
                         "only during an inventory.  Saving this rule is not enough. This is due to the nature of inventory rules."),
                    elements = [
                         Integer(
                            title = _("Critical below"),
                            unit = _("processes"),
                            default_value = 1,
                         ),
                         Integer(
                            title = _("Warning below"),
                            unit = _("processes"),
                            default_value = 1,
                         ),
                         Integer(
                            title = _("Warning above"),
                            unit = _("processes"),
                            default_value = 99999,
                         ),
                         Integer(
                            title = _("Critical above"),
                            unit = _("processes"),
                            default_value = 99999,
                        ),
                    ],
                )),
            ],
            required_keys = [ "descr" ],
        ),
    match = 'all',
)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
