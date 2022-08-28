import imp
from flask import Flask
import os
from Project.db import db

#Application Factory Function
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
       app.config.from_mapping(

        CORS_HEADERS= 'Content-Type',
        SQLALCHEMY_DATABASE_URI = "sqlite:///project.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,

 
    )
    else:
        # load the test config if passed in , resources=r'/*'
        app.config.from_mapping(test_config)
    

    from Project.courseUnits.index import courseUnits
    from Project.program.index import program
 
    #registering blueprints    
  
    app.register_blueprint(courseUnits)
    app.register_blueprint(program)
     
    db.app = app
    db.init_app(app)
    db.create_all()
   
    return app