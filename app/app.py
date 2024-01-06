from flask import Flask 
import routes
from cli import bp
from db import conn
import decorators

# class Application:

#     def __init__(self) -> None:
#         self.app = Flask(__name__)

#         self.app.config.from_pyfile("config.py")
#         self.app.config['JSON_AS_ASCII'] = False # для кириллицы в конфиге
#         conn.init_app(self.app)

#         self.app.register_blueprint(bp)
#         self.app.register_blueprint(routes.bp)
    
#     def __run_app(self):
#          self.app.run(debug=True, host="0.0.0.0")

#     def verification_run(self):
#         if __name__ == "__main__":
#             self.__run_app()
#         else:
#             print(f'Импорт Application из {__name__} ')
#             return 'Закрыт метод'

#     def get_app(self):

#         return self.app
    


# appl=Application()
# appl.verification_run()


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")


app = Flask(__name__)

app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False # для кириллицы в конфиге

conn.init_app(app)

app.register_blueprint(bp)
app.register_blueprint(routes.bp)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


"""


app = Flask(__name__)

app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False # для кириллицы в конфиге
conn.init_app(app)

app.register_blueprint(bp)
app.register_blueprint(routes.bp)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

    
    
    
    """

