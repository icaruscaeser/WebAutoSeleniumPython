from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Firefox()

driver.get('http://www.chat.chatkaro.in/chatonlineroom/')

username = 'icarus'
password = 'icarus'

# wait for login element to appear, then hover it
wait = WebDriverWait(driver, 30)
time.sleep(20)

guest_check_box = wait.until(expected_conditions.visibility_of_element_located((By.ID, "topcmm-123flashchat-loginview-guest-checkbox")))
ActionChains(driver).move_to_element(guest_check_box).click().perform()

login_element = wait.until(expected_conditions.visibility_of_element_located((By.ID, "topcmm-123flashchat-loginview-username-input")))
login_element.clear()
login_element.send_keys(username)
try:
    password_input_field = driver.find_element_by_id('topcmm-123flashchat-loginview-password-input')
    password_input_field.clear()
    password_input_field.send_keys(password)
except Exception as exc:
    print(exc)


login_button = wait.until(expected_conditions.visibility_of_element_located((By.ID,'topcmm-123flashchat-loginview-login-btn')))
login_button.click()

time.sleep(15)
rooms = driver.find_elements_by_class_name('topcmm-123flashchat-roomlist-container-one-room-block')
print(rooms)

tamil_room = rooms[12]
tamil_room.click()

x = '''1. Romeo and Juliet

My bounty is as boundless as the sea,

My love as deep; the more I give to thee,

The more I have, for both are infinite.

2. The Tempest

Hear my soul speak:

The very instant that I saw you, did

My heart fly to your service.

3. As You Like It

If thou remember’st not the slightest folly

That ever love did make thee run into,

Thou hast not loved.

4. Sonnet 116

Love alters not with his brief hours and weeks,

But bears it out even to the edge of doom.

If this be error and upon me proved,

I never writ, nor no man ever loved.

5. Hamlet

Doubt thou the stars are fire;

Doubt that the sun doth move;

Doubt truth to be a liar;

But never doubt I love.

6. Love’s Labour’s Lost

When Love speaks, the voice of all the gods

Makes heaven drowsy with the harmony.

7. Venus and Adonis

Love is a spirit all compact of fire.

8. Romeo and Juliet (there had to be at least 2 from this play)

Love goes toward love as school-boys from their books,

But love from love, toward school with heavy looks.

9. Twelfth Night

If music be the food of love, play on;

Give me excess of it, that, surfeiting,

The appetite may sicken, and so die.

'''



#while True:
for i in x.split('\n'):
    text_area = wait.until(expected_conditions.visibility_of_element_located((By.ID,'topcmm-123flashchat-main-message-input')))
    text_area.clear()
    #text_area.send_keys("Pala vedikkai manitharai pol naan veezhven endru ninaithaayo....")
    text_area.send_keys(i)
    send_button = driver.find_element_by_id('topcmm-123flashchat-main-send-msg-btn')
    send_button.click()

    time.sleep(4)
