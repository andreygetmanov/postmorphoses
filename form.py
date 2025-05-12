from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def gfg():
    """
    Handles GET and POST requests to the root route.

        If a POST request is received, it retrieves text from the form data,
        writes it to 'data/text_for_gen.txt', and renders the 'form.html' template
        with the submitted text as history.  If a GET request is received, it
        renders the 'form.html' template with an empty history string.

        Parameters:
            None

        Returns:
            str: The rendered HTML content of the 'form.html' template.
    """
    if request.method == "POST":
        text_for_gen = request.form.get("txtgen")
        with open("data/text_for_gen.txt", "w") as f:
            f.write(text_for_gen)
        f.close()
        return render_template("form.html", history=text_for_gen)
    return render_template("form.html", history="")


if __name__ == "__main__":
    app.run()
