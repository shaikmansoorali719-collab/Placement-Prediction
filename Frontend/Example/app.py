from flask import Flask, redirect, render_template, url_for

from models.load import load_data, summarize

app = Flask(__name__)


@app.route("/")
def index_page():
    return redirect(url_for("load_page"))


@app.route("/load")
def load_page():
    df = load_data()
    summary = summarize(df)
    return render_template(
        "load.html",
        shape=summary["shape"],
        columns=summary["columns"],
        preview=df.head(10).to_dict(orient="records"),
    )


@app.route("/eda")
def eda_page():
    return render_template("base.html")


@app.route("/feature-engg")
def feature_engg_page():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
