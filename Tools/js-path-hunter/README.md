# JS-PathHunter 🕵️‍♂️🔍

A lightweight and efficient reconnaissance tool designed for Penetration Testers and Bug Bounty Hunters to extract hidden JavaScript files, HTML comments, and potential endpoints/parameters from target web applications.

---

## 🚀 Features
- **JS Discovery:** Finds and extracts JavaScript file paths linked in the target webpage.
- **Comment Scraping:** Scans the page source and HTML comments for potential sensitive information or developer notes.
- **Endpoint Extraction:** Automatically parses JS and HTML content to uncover hidden paths, API endpoints, and parameters (e.g., `/product?id=...`, `/my-account`).

---

## 🛠️ Installation & Setup

Make sure you have Python 3 installed on your system. Follow these steps to set up the tool:

1. **Clone the repository (or navigate to your tool directory):**
   ```bash
   cd /usr/My_Tools/

2. **Install the required dependencies:**
The tool relies on `requests` and `beautifulsoup4`. Install them via pip:
```bash
pip install requests beautifulsoup4

```



---

## 💻 Usage

Run the script using Python 3:

```bash
python3 JS-PathHunter.py

```

When prompted, enter the target URL (e.g., a target lab or application URL):

```text
Enter target URL (e.g., [https://example.com](https://example.com)): [https://your-target-url.web-security-academy.net/](https://your-target-url.web-security-academy.net/)

```

---

## 📌 Example Output

```text
[+] --- Searching for JavaScript Files ---
Found JS: /resources/labheader/js/labHeader.js

[+] --- Searching for HTML Comments ---
[+] --- Extracting Potential Paths/Endpoints ---
Found Path: /product?productId=18
Found Path: /my-account
Found Path: /product?productId=5

```

---

## 🛡️ Disclaimer

*This tool is created for educational purposes and authorized security testing (Penetration Testing / Bug Bounties) only. The author is not responsible for any misuse or illegal activities.*


