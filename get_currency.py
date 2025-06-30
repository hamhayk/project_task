import requests
import xml.etree.ElementTree as ET
from datetime import date

today = date.today()

def get_rate_by_date(currency):
    url = "https://api.cba.am/exchangerates.asmx"
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.cba.am/ExchangeRatesByDateByISO"
    }

    # Construct the SOAP XML body
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <ExchangeRatesByDateByISO xmlns="http://www.cba.am/">
          <date>{today}T00:00:00</date>
          <ISO>{currency}</ISO>
        </ExchangeRatesByDateByISO>
      </soap:Body>
    </soap:Envelope>"""

    # Send the SOAP request
    response = requests.post(url, headers=headers, data=body)

    if response.status_code != 200:
        print(f"HTTP error: {response.status_code}")
        print(response.text)
        return

    namespaces = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'cba': 'http://www.cba.am/'
    }

    root = ET.fromstring(response.content)

    # Find the exchange rate info
    rate_elem = root.find('.//cba:ExchangeRate', namespaces)
    if rate_elem is None:
        print("USD exchange rate not found.")
        return
    
    #print(root)

    iso = rate_elem.find('cba:ISO', namespaces).text
    amount = float(rate_elem.find('cba:Amount', namespaces).text)
    rate = float(rate_elem.find('cba:Rate', namespaces).text)

    # print(f"USD Exchange Rate on {date_str}:")
    # print(f"  Rate    : {rate}")
    # print(f"  Amount  : {amount}")
    return rate/amount



