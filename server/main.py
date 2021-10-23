from flask import Flask
from api.article_features_hander import article_features_hander
from flask_cors import CORS


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(article_features_hander)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
