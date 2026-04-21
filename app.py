from flask import Flask, request, render_template
from search import search
from agents import research_agent, writer_agent, reviewer_agent
from memory import save
from pdf_export import export_pdf

app = Flask(__name__)


def run_agent(topic):
    print("🔍 Searching...")
    data = search(topic)

    print("🧠 Researching...")
    r = research_agent(data)

    print("✍️ Writing...")
    w = writer_agent(r)

    print("🔍 Reviewing...")
    final = reviewer_agent(w)

    save(topic, final)
    export_pdf(final)

    return final


@app.route("/")
def home():
    return '''
    <h2>AI Agent Pro</h2>
    <form action="/generate" method="post">
        <input name="topic" placeholder="Enter topic">
        <button>Generate</button>
    </form>
    '''


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]
    result = run_agent(topic)
    return f"<pre>{result}</pre>"


if __name__ == "__main__":
    app.run(debug=True)