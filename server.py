from flask import Flask,render_template,request
from astro import Astro
from genai import AiAnswer
import markdown
from markupsafe import Markup


app= Flask(__name__)

@app.route("/" )
def main_page():
    return render_template("index.html")

@app.route("/analysis" , methods=["POST"])
def analysis():
    data = request.form.to_dict()

    int_keys = ["year", "month", "date", "hours", "minutes", "seconds"]
    float_keys = ["latitude", "longitude", "timezone"]
    try:
        for k in int_keys:
            data[k] = int(data[k])
        for k in float_keys:
            data[k] = float(data[k])
    except (KeyError,ValueError):
        return "<h1>Please Try Again a Error Was Encountered</h1>"
    caller = Astro(data)
    response = caller.make_call()
    ai_caller = AiAnswer(response)
    ai_response = ai_caller.analyze()
    ai_response_html = Markup(markdown.markdown(ai_response))

    return render_template("analysis.html", ai_response=ai_response_html)






if __name__ == "__main__":
    app.run(debug=True)
