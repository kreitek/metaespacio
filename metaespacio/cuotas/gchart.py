from graphos.renderers.gchart import BaseChart

from django.template.loader import render_to_string


class ComboChart(BaseChart):

    def get_template(self):
        return "gchart/combo_chart.html"

    def get_options(self):
        options = super(ComboChart, self).get_options()
        if not 'vAxis' in options:
            vaxis = self.data_source.get_header()[0]
            options['vAxis'] = {'title': vaxis}
        return options
