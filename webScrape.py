#first assignmnet is scrape this site https://www.xpress.jobs/ [Home page] and get title,company in json format 

import requests
from bs4 import BeautifulSoup
import json

try:
    r = requests.get('https://www.xpress.jobs/')
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.find('ul', class_="job_listings").findAll("li")

    job_listings = []

    for table in tables:
        position_name = table.find('h3')
        company_name = table.find('strong')

        if position_name is not None and company_name is not None:
            job_listing = {
                'position_name': position_name.text.strip(),
                'company_name': company_name.text.strip()
            }
            job_listings.append(job_listing)

    # Convert the list of dictionaries to a JSON string
    json_output = json.dumps(job_listings, indent=2)
    print(json_output)

except Exception as e:
    print(e)
