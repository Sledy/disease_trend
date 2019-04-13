from flask import Blueprint, render_template, request
from main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)

    if request.method == 'POST' and form.validate():

        disease_name = form.disease_name.data
        start_date = form.start_time.data
        end_date = form.end_time.data


        return 'duasd'

    return render_template('base.html', form=form)
