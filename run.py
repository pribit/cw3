import logging
from json import JSONDecodeError

from flask import abort, Flask

from app.api.views import api_bp
from app.html.views import html_bp
from app.logger import create_logger

create_logger()
logger = logging.getLogger('basic')

app = Flask(__name__)

app.register_blueprint(html_bp)
app.register_blueprint(api_bp)


@app.errorhandler(FileNotFoundError)
@app.errorhandler(JSONDecodeError)
def bad_file(error):
    logger.error(f'Получена ошибка {str(error)}')
    abort(500)


if __name__ == '__main__':
    logger.info('Приложение стартует')
    app.run()
