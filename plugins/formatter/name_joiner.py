from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'name_joiner')):

    def format(self, value):
        date = self.format_value(value[1], self.field_date_formatter_provider,
            format = self.field_date_format
        )
        return self.field_join.join([
            str(int(value[0])),
            date.strftime("%Y-%m-%d")
        ])
