from app import app

app.run(port=3500, debug=True, host='0.0.0.0', ssl_context=('pem.crt', 'pem.key'))
