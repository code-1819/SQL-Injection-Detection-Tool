from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# Setting up session and headers to mimic a browser
s = requests.Session()
s.headers[
    "User-Agent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                     "Version/17.4.1 Safari/605.1.15")


# Function to fetch all forms present on a webpage
def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")


# Function to extract details of a form
def form_details(form):
    details_of_form = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []

    # Extracting details of each input field within the form
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type,
            "name": input_name,
            "value": input_value
        })

    details_of_form['action'] = action
    details_of_form['method'] = method
    details_of_form['inputs'] = inputs
    return details_of_form


# Function to check if the response indicates SQL injection vulnerability
def vulnerable(response):
    errors = [
        "you have an error in your SQL syntax",
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string"
    ]
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False


# Function to scan for SQL injection vulnerabilities
def sql_injection_scan(url):
    forms = get_forms(url)
    print(f"[+] detected {len(forms)} forms on {url}.")

    for form in forms:
        details = form_details(form)

        res = None  # Define res here before the loop
        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                # Manipulating input values to check for SQL injection
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag["name"]] = input_tag["value"] + str(1)
                elif input_tag["type"] != "submit":
                    data[input_tag['name']] = f"test{i}"

            if details["method"] == "post":
                res = s.post(url, data=data)
            elif details["method"] == "get":
                res = s.get(url, params=data)
            # Checking if the response indicates vulnerability
            if res and vulnerable(res):  # Check if res is not None
                print("SQL Injection Attack Vulnerability in Link: ", url)
            else:
                print("No SQL Injection Attack Vulnerability Detected")
                break


if __name__ == "__main__":
    url_to_be_checked = input("Enter the URL to scan: ")
    sql_injection_scan(url_to_be_checked)
