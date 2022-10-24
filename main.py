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
    form = NewCafe(meta={'csrf': False})
    if form.validate_on_submit():
        pass
        ### API Call ###
        ### word = request.form.get("name")###
        ### api return json with 3 values, last is nested dict with 5 k,v ###
        is_edit = True
    return render_template("index.html", form=form, is_edit=is_edit)


if __name__ == '__main__':
    app.run(debug=True)
