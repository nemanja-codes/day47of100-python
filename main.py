import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,sr;q=0.7"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=headers)
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")
price = soup.find(name="span", class_="aok-offscreen")
price_to_float = float(price.getText().strip()[1:])
print(price_to_float)
