import requests
from bs4 import BeautifulSoup

def check_product(product_url):
    response = requests.get(product_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_name = soup.find(name="div", class_="jsx-bb40b49043b26d53 buy_box_text ellipsis")
        product_price = soup.find(name="h1", class_="jsx-bb40b49043b26d53")
        return True, f"Product Name: {product_name}, Product Price: {product_price}"
    else:
        return False, f"Error accessing product page! Status code: {response.status_code}"

product_url = "https://torob.com/p/b7fe3c1c-0d74-4a3a-bed3-7e29e92f3fda/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s24-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
status, message = check_product(product_url)

if status:
    print(message)
else:
    print(message)