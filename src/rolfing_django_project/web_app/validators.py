from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class UnicodeSpaceUsernameValidator(UnicodeUsernameValidator):
    regex = r'^[\w.\" \"@+-]+\Z'
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, @/./+/-/_ characters and space."
    )
