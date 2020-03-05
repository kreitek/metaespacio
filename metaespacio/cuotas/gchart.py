from graphos.renderers.gchart import BaseChart


class ComboChart(BaseChart):
    def get_template(self):
        return "gchart/combo_chart.html"

    def get_options(self):
        options = super(ComboChart, self).get_options()
        if 'vAxis' not in options:
            vaxis = self.data_source.get_header()[0]
            options['vAxis'] = {'title': vaxis}
        return options
