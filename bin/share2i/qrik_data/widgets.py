# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import Select
from django.utils.encoding import force_unicode
from itertools import chain
from django.utils.html import escape, conditional_escape

def fill_topic_tree(deep = 0, parent_id = 0, choices = []):
    if parent_id == 0:
        ts = Category.objects.filter(parent = None)
        choices[0] += (('', '---------'),)
        for t in ts:
            tmp = [()]
            fill_topic_tree(4, t.id, tmp)
            choices[0] += ((t.id, ' ' * deep + t.name,),)
            for tt in tmp[0]:
                choices[0] += (tt,)
    else:
        ts = Category.objects.filter(parent__id = parent_id)
        for t in ts:
            choices[0] += ((t.id,' ' * deep + t.name, ),)
            fill_topic_tree(deep + 4, t.id, choices)
 
            from django.forms import Select
            from django.utils.encoding import force_unicode
            from itertools import chain
            from django.utils.html import escape, conditional_escape
            
class TreeSelect(Select):
    def __init__(self, attrs=None):
        super(Select, self).__init__(attrs)

    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if option_value in selected_choices:
            selected_html = u' selected="selected"'
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return u'<option value="%s"%s>%s</option>' % (
            escape(option_value), selected_html,
            conditional_escape(force_unicode(option_label)).replace(' ', ' '))

    def render_options(self, choices, selected_choices):
        ch = [()]
        fill_topic_tree(choices = ch)
        self.choices = ch[0]
        selected_choices = set(force_unicode(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                output.append(u'<optgroup label="%s">' % escape(force_unicode(option_value)).replace(' ', ' '))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append(u'</optgroup>')
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
        return u'\n'.join(output)
