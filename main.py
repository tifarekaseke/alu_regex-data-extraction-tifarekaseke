import re

def extract_data(your_string):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    url_pattern = r'https?://[^\s]+'
    phone_pattern = r'(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})'
    currency_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'

    emails = re.findall(email_pattern, your_string)
    urls = re.findall(url_pattern, your_string)
    phone_numbers = re.findall(phone_pattern, your_string)
    currency_amounts = re.findall(currency_pattern, your_string)

    return {
        "emails": emails,
        "urls": urls,
        "phone_numbers": phone_numbers,
        "currency_amounts": currency_amounts,
    }

# Example usage
your_string = """
Contact us at user@example.com or visit https://www.example.com. 
Call (123) 456-7890. Price is $19.99. 
Also check https://subdomain.example.org/page for more info.
"""
extracted_data = extract_data(your_string)
print(extracted_data)
