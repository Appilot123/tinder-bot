from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode (optional)
options = Options()
options.add_argument("--headless")  # Run browser in background mode, comment out to see browser

# Set up the Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)

def login():
    driver.get("https://tinder.com/")
    time.sleep(5)

    # Click the 'Log in' button (Change the selector if necessary)
    login_button = driver.find_element(By.XPATH, '//*[@id="q-65-0-1"]/div/div[2]/div/div[1]/div[1]/button')
    login_button.click()
    time.sleep(2)

    # Login with Facebook/Google/Apple (here we select Facebook login, adjust as needed)
    fb_button = driver.find_element(By.XPATH, '//*[@id="q-65-0-1"]/div/div[2]/div/div[1]/div[2]/button')
    fb_button.click()
    time.sleep(5)

    # Enter Facebook credentials (not recommended for production, use cookies instead)
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("YOUR_EMAIL")
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)

    password_input = driver.find_element(By.NAME, "pass")
    password_input.send_keys("YOUR_PASSWORD")
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Allow location and notifications pop-ups
    allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[3]/button[1]')
    allow_location_button.click()
    time.sleep(2)

def swipe_right():
    # Find and click the 'Like' (right swipe) button
    try:
        right_swipe_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/main/div/div[1]/div[1]/div[4]/button')
        right_swipe_button.click()
        print("Swiped right!")
    except Exception as e:
        print("Error while swiping:", e)

def send_message():
    # Find the 'Message' button and click it
    try:
        message_button = driver.find_element(By.XPATH, '//*[text()="Message"]')
        message_button.click()
        time.sleep(2)

        # Find the message input field and type a message
        message_input = driver.find_element(By.XPATH, '//*[@id="message_input"]')
        message_input.send_keys("Hey! How's it going?")
        message_input.send_keys(Keys.RETURN)
        print("Message sent!")
    except Exception as e:
        print("Error while sending message:", e)

def main():
    login()  # Log into Tinder

    # Loop to automatically swipe right and send messages
    for _ in range(5):  # Swiping 5 times for demonstration
        swipe_right()
        time.sleep(2)  # Wait for a couple of seconds between actions

        send_message()  # Send message to the match
        time.sleep(5)  # Wait for some time before next interaction

    driver.quit()  # Close the browser

if __name__ == "__main__":
    main()
