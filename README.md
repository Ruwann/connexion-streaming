# Connexion streaming example

Start the server:

```bash
python run.py
```

Then, in another terminal, run the client:

```bash
curl -X 'POST' \
    'http://localhost:8080/openapi/streaming' \
    -H 'accept: text/plain' \
    -N
```

You should see the server streaming data to the client.
