import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "necamark@gmail.com"
PASSWORD = "xuklpbmootnalxdi"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,sr;q=0.7"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=headers)
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")
product_name = soup.find(id="productTitle").get_text().strip()
price = soup.find(name="span", class_="aok-offscreen")
price_to_float = float(price.getText().strip()[1:])

if price_to_float < 100:
    message = (f"{product_name} is now ${price_to_float}.\n"
               f"https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
