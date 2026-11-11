import requests
from bs4 import BeautifulSoup
import re

# رابط الهدف
url = input("Enter target URL (e.g., https://example.com): ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n[+] --- Searching for JavaScript Files ---")
        scripts = soup.find_all('script', src=True)
        for script in scripts:
            print(f"Found JS: {script['src']}")
            
        print("\n[+] --- Searching for HTML Comments ---")
        comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
        for comment in comments:
            print(f"Found Comment: {comment.strip()}")
            
        print("\n[+] --- Extracting Potential Paths/Endpoints ---")
        # البحث عن أي مسارات تبدأ بـ / داخل الـ Text
        paths = re.findall(r'href=["\'](/[^"\']+)["\']', response.text)
        for path in set(paths):
            print(f"Found Path: {path}")
            
    else:
        print("[-] Failed to retrieve the page.")
except Exception as e:
    print(f"[-] Error: {e}")
