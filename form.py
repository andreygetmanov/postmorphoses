from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        text_for_gen = request.form.get("txtgen")
        with open('data/text_for_gen.txt', 'w') as f:
            f.write(text_for_gen)
        f.close()
        return render_template('form.html', history=text_for_gen)
    return render_template("form.html", history='')


if __name__ == '__main__':
    app.run()