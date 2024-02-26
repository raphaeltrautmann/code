"""FACTORY DO APP"""

from flask import Flask


def init_app():
    """
    init_app é uma factory que retorna
    uma instancia da aplcação Flask.

    Para configurar a aplicação deve-se Intanciar
    o objeto de configuração de acordo com o ambiente.

    O banco de dodos é manipulado através da biblioteca
    SQLAlchemy. Todos os arquivos para interação com
    o banco de dados esta em ./src/database/, sendo que
    dentro desse diretorio existe outras duas pastas essenciais,
    que são:
    ../models que contens os models da aplicão e
    ../querys que contém as interações com o banco de dados


    SQLAlchemy - Website: https://www.sqlalchemy.org/

    As Blueprints da aplicação estão setadas dentro de
    ./src/blueprints/blueprint_name/. Cada uma
    possui um url próprio para suas rotas que é
    setado em url_prefix. Ela pode conter um diretório
    src para manter os objetos utilizados pela blueprints

    """
    app = Flask(__name__, static_url_path="/static")
    
    with app.app_context():
        
        from .blueprints import home_app
        app.register_blueprint(home_app)

        return app

