from flask import Flask, render_template

app = Flask("Blueprint")

from app.main import main
app.register_blueprint(main)

from app.result import result
app.register_blueprint(result)

    

    

