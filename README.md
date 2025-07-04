### Setup
```sh
  pythom -m venv venv
  source venv/bin/activate
  pip install playwright
  playwright install
```

### Execution
- Set the data in tenancy_agreement_template.html
- Run a simple http server and generate the PDF
```sh
  http-server # assume server runs on 8080 port
  python run.py
```

### Output
tenancy_agreement.pdf
