import re

from django.utils.translation import ugettext_lazy as _

DE_POSTCODE_RE = re.compile(r'^\d{5}$')


def validate(postcode):
    if DE_POSTCODE_RE.search(postcode):
        return postcode

    raise ValueError(_('Invalid ZIP code'))
