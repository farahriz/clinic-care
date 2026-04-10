import requests
from bs4 import BeautifulSoup

root_url="https://www.icd10data.com"
website_url = "https://www.icd10data.com/ICD10CM/Codes"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
codes = []

response = requests.get(website_url, headers=headers)
if(response.status_code == 200):
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    code_group_links = []
    for link in soup.find_all('a'):
        # A__-A__ or B__-B-- ; letters should match so we know we've got the links that contain code descriptions
        if (len(link.text) == 7 and link.text[0] == link.text[4]):
            code_group_links.append(link.get('href'))

    # for path in code_group_links:
    path = code_group_links[0]
    print(f"{root_url}{path}")
    sum_response = requests.get(f"{root_url}{path}", headers=headers)   
    if(sum_response.status_code == 200):
        soup2 = BeautifulSoup(sum_response.content)
        # find li in soup 
        # a will be the code
        # get the text
        # format an object



else:
    print(response)

target_page_group = "A00-B99"

# find link to group page
code_groups = ["A00-A09", "A15-A19", "A20-A28", "A30-A49", "A50-A64", "A65-A69"]


# for each group page, find link to individaul code
code_subgroups = ["A00", "A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09"]

# go to individual code page

#find section with code

# Get code
# e.g. code = "A00"

# Get name
# e.g. name = "Cholera"


#once there are no more codes, go back