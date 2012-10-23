"""
Stolen from: http://tomcoote.co.uk/code-bank/django-email-munger/

"""
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import re

register = template.Library()

@register.filter
@stringfilter
def mungify(email, text=None, autoescape=None):
    '''
    Template filter to hide an email address away from any sort of email harvester
    type web scrapers and so keep away from spam etc.

    The filter should be applied on a string which represents an email address. You
    can optionally give the filter a parameter which will represent the name of the
    resulting email href link. If no extra parameter is given the email address will
    be used as the href text.

    {{ email|mungify:"contact me" }}
    or
    {{ email|mungify }}

    The output is javascript which will write out the email href link in a way so
    as to not actually show the email address in the source code as plain text.
    '''
    text = text or email

    if autoescape:
        email = conditional_escape(email)
        text = conditional_escape(text)

    emailArrayContent = ''
    textArrayContent = ''
    r = lambda c: '"' + str(ord(c)) + '",'

    for c in email: emailArrayContent += r(c)
    for c in text: textArrayContent += r(c)

    result = """<script>
        var _tyjsdf = [%s], _qplmks = [%s];
        document.write('<a href="mailto:');
        for(_i=0;_i<_tyjsdf.length;_i++){document.write('&#'+_tyjsdf[_i]+';');}
        document.write('">');
        for(_i=0;_i<_qplmks.length;_i++){document.write('&#'+_qplmks[_i]+';');}
        document.write('</a>');
        </script>""" % (re.sub(r',$', '', emailArrayContent), re.sub(r',$', '', textArrayContent))

    return mark_safe(result)

mungify.needs_autoescape = True
