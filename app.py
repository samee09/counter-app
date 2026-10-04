from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="cache", port=6379)

@app.route("/")
def home():
  n = r.incr("hits")
  return f"<h1>Samee ki app</h1><p>Visits: {n}</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
