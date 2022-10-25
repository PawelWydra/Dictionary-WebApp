from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewCafe(FlaskForm):
    name = StringField("Online Dictionary", validators=[DataRequired()], render_kw={"placeholder": "Let's check some words..."})
    submit = SubmitField("Check word")


app = Flask(__name__)
Bootstrap(app)

@app.route("/", methods=["POST", "GET"])
def home():
    is_edit = False
    definition = False
    image_url = False
    word = False
    form = NewCafe(meta={'csrf': False})
    if form.validate_on_submit():
        import requests
        headers = {
            "Authorization": "Token 66ab3a3a00d3ff67dc360abaa73ff615cc5af22c"
        }
        word = request.form.get('name').capitalize()
        try:
            response = requests.get(f"https://owlbot.info/api/v4/dictionary/{word}", headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        data = response.json()
        definition = data["definitions"][0]["definition"]
        image_url = data["definitions"][0]["image_url"]

        is_edit = True
    return render_template("index.html", form=form, is_edit=is_edit, definition=definition, image_url=image_url, word=word)


if __name__ == '__main__':
    app.run(debug=True)
