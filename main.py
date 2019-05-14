#!/usr/bin/env python
from flask import Flask
from dns import resolver

dnsResolver = resolver.Resolver()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/v1/<record_type>/<domain>', methods=['GET'])
def record_lookup(record_type, domain):
    try:
        response = dnsResolver.query(domain, record_type.upper())
        return str([str(r) for r in response])
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
