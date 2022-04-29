from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import services.quotes_service

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/quotes/all')
def index():
    all_quotes = services.quotes_service.get_all_quotes()
    return render_template('quotes_all.html', all_quotes=all_quotes)
