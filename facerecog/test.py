from flask import Flask, render_template

from qrscanner import qrcodescanner_bp
from deepfacerecog import deepfacerecog_bp
from registerface import registerface_bp

app = Flask(__name__)

app.register_blueprint(qrcodescanner_bp, url_prefix="/qrcodescanner")
app.register_blueprint(deepfacerecog_bp, url_prefix="/deepfacerecog")
app.register_blueprint(registerface_bp, url_prefix="/registerface")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# I-print lahat ng registered routes
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)