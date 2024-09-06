import time
import requests

# Function to print text with color
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Function to display the welcome message
def show_welcome_message():
    welcome_message = """
    =================================
         Pentagon Auto Reff
         by gilang sgb
         thx to PENTIL.pink _/\_
    =================================
    """
    print_colored(welcome_message, '92')  # Green color

# URL destination
url = "https://pentil.pink/pentagonv1/pentil.php"

# Referral code
ref_code = input("Masukkan kode referral (contoh: ref627615207): ")

# Session object to persist cookies
session = requests.Session()

# Headers as per the screenshot information
headers = {
    "authority": "pentil.pink",
    "method": "POST",
    "path": "/pentagonv1/pentil.php",
    "scheme": "https",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://pentil.pink",
    "Referer": "https://pentil.pink/pentagonv1/",
    "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="120"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
}

# Form data sent with refString
data = {
    "refString": ref_code  # Data with refString field
}

# Function to submit the form
def submit_referral():
    try:
        response = session.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print_colored(f"Response from server: {response.text.strip()}", '94')  # Blue color
        else:
            print_colored(f"Error {response.status_code}: Failed to process referral.", '91')  # Red color
    except Exception as e:
        print_colored(f"An error occurred: {e}", '91')  # Red color

# Display the welcome message
show_welcome_message()

# Loop to submit every 33 seconds
while True:
    submit_referral()
    time.sleep(33)  # Wait 33 seconds before submitting again
