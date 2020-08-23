from systems.plugins.index import BaseProvider

import re


class Provider(BaseProvider('validator', 'state_code')):

    def validate(self, value):
        if not isinstance(value, str):
            self.warning("Value {} is not a string".format(value))
            return False

        if not re.match(r'^[A-Z]{2}$', value):
            self.warning("Value {} is not a valid state code".format(value))
            return False

        return True
