## Tenancy Agreement Template
Convert tenancy agreement in HTML to PDF using [playwright-python](https://github.com/microsoft/playwright-python)

Rental contract source: [!WOON](https://www.wooninfo.nl/vraagbaak/huurprijs/voorbeeld-huurcontracten/)

### Setup
```sh
  pythom -m venv venv
  source venv/bin/activate
  pip install playwright
  playwright install
```

### Execution
- Set the rental data in the tenancy_agreement_template.html
- Run a simple http server and generate the PDF
```sh
  http-server # assume server runs on 8080 port
  python run.py
```

### Output
Checkout tenancy_agreement.pdf
