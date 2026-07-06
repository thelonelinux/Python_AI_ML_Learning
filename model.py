import argparse
from collections.abc import Iterator

from flask import Flask, request, render_template_string
import ollama

app = Flask(__name__)

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Ollama Gemma3 Web UI</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; max-width: 800px; }
      textarea, input[type=text] { width: 100%; margin: .5rem 0; }
      button { padding: .6rem 1rem; font-size: 1rem; }
      pre { background:#f5f5f5; padding:1rem; white-space: pre-wrap; word-wrap: break-word; }
    </style>
  </head>
  <body>
    <h1>Ollama Gemma3 Browser Demo</h1>
    <form method="post">
      <label for="prompt">Prompt</label>
      <textarea id="prompt" name="prompt" rows="5">{{ prompt }}</textarea>
      <label for="system">System instruction (optional)</label>
      <input id="system" name="system" type="text" value="{{ system or '' }}">
      <button type="submit">Generate</button>
    </form>
    {% if answer is not none %}
      <h2>Model response</h2>
      <pre>{{ answer }}</pre>
    {% endif %}
  </body>
</html>"""


def generate_gemma3(prompt: str, system: str | None = None, stream: bool = False) -> str:
    """Generate text from the Ollama gemma3 model."""
    response = ollama.generate(model="gemma3", prompt=prompt, system=system, stream=stream)

    if stream and isinstance(response, Iterator):
        return "".join(chunk.response or "" for chunk in response)

    return getattr(response, "response", "") or ""


@app.route("/", methods=["GET", "POST"])
def index():
    prompt = "Hello from gemma3!"
    system = ""
    answer = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        system = request.form.get("system", "")
        answer = generate_gemma3(prompt=prompt, system=system or None, stream=False)

    return render_template_string(HTML_TEMPLATE, prompt=prompt, system=system, answer=answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Ollama gemma3 web app.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind the web app.")
    parser.add_argument("--port", type=int, default=8000, help="Port for the web app.")
    parser.add_argument("--debug", action="store_true", help="Run Flask in debug mode.")
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
