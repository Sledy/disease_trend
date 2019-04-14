from flask import Blueprint, render_template, request
from main.forms import SearchForm
from main.pubmed_utils.entrez_search import SearchReport


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)

    if request.method == 'POST' and form.validate():

        disease_name = form.disease_name.data
        start_date = form.start_time.data.year
        end_date = form.end_time.data.year

        graph_uri = SearchReport(query=disease_name, mindate=start_date, maxdate=end_date).give_trend()

        return render_template('graph.html', graph_data=graph_uri)

    return render_template('base.html', form=form)
