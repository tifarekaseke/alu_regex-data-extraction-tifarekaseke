import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})'
currency_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
