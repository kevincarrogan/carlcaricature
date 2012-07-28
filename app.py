import os
import pystache
import requests

from bs4 import BeautifulSoup
from pystache.loader import Loader

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    loader = Loader()
    template = loader.load_name('index')

    response = requests.get('http://www.unboxedconsulting.com/people/carl-whittaker')
    status = response.status_code
    if status == 200:
        content = response.content

        soup = BeautifulSoup(content)
        image = 'http://www.unboxedconsulting.com' + soup.select('.vcard .photo')[0]['src']
    else:
        image = ''

    return pystache.render(
        template,
        {
            'has_caricature': status == 200,
            'image': image
        }
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
