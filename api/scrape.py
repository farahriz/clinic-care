import requests
import json
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

    example_href = "/ICD10CM/Codes/A00-B99/B20-B20"
    target_code_group_links = [link for link in code_group_links if len(link)==len(example_href)]

    i = 0
    while i < 10:
        path = target_code_group_links[i]
        print(f"{root_url}{path}")
        i += 1
        sum_response = requests.get(f"{root_url}{path}", headers=headers)   
        if(sum_response.status_code == 200):
            soup2 = BeautifulSoup(sum_response.content, 'html.parser')

            def has_name_attr(tag):
                return tag.has_attr('name')

            code_points = soup2.find_all(has_name_attr, "a", class_="identifier")
            for point in code_points:
                codes.append({"code": point.text, "name": point.parent.text})
                if(len(codes) > 150):
                    break
        if(len(codes) > 150):
            break
            
    json_data = json.dumps(codes, indent=2)

    print('codes aquired:', len(codes))

    with open("code_dump.json", "w") as json_file:
        json_file.write(json_data)


else:
    print("Big issue happened")
    # print(response)