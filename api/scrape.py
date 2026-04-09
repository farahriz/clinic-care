import requests

website_url = "https://www.icd10data.com/ICD10CM/Codes"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(website_url, headers=headers)
if(response.status_code == 200):
    html_content = response.content
    print(html_content)
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