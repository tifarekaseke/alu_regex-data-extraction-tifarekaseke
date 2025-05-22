# Import the 're' module, which provides support for regular expressions
import re

# Define a function to extract specific data patterns from a given string
def extract_data(your_string):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    url_pattern = r'https?://[^\s]+'
    phone_pattern = r'(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})'
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

 # Find all occurrences of the patterns in the input string
    emails = re.findall(email_pattern, your_string)
    urls = re.findall(url_pattern, your_string)
    phone_numbers = re.findall(phone_pattern, your_string)
    currency_amounts = re.findall(currency_pattern, your_string)

    # Return the extracted data as a dictionary
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


# Call the function with the example string and store the result
extracted_data = extract_data(your_string)

# Print the extracted data
print(extracted_data)
