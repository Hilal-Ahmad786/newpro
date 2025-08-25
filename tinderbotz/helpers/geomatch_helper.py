from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from tinderbotz.helpers.xpaths import content
from datetime import datetime

class GeomatchHelper:

    delay = 5

    HOME_URL = "https://www.tinder.com/app/recs"

    def __init__(self, browser):
        self.browser = browser
        if "/app/recs" not in self.browser.current_url:
            self._get_home_page()

    def _get_home_page(self):
        self.browser.get(self.HOME_URL)
        time.sleep(3)

    def like(self) -> bool:
        """
        OPTIMIZED like method - uses fastest approach (keyboard)
        """
        try:
            # Method 1: Keyboard shortcut (FASTEST - 0.1s)
            action = ActionChains(self.browser)
            action.send_keys(Keys.ARROW_RIGHT).perform()
            
            # Minimal delay for UI update
            time.sleep(0.1)  # Reduced from 1 second
            return True
            
        except Exception as e:
            # Fallback: Try button click (slower but more reliable)
            try:
                like_selectors = [
                    "//button[contains(@class, 'gamepad-button')]",
                    "//button[@aria-label='Like']",
                    "//button[.//svg[contains(@class, 'gamepad')]]"
                ]
                
                for selector in like_selectors:
                    try:
                        btn = self.browser.find_element(By.XPATH, selector)
                        btn.click()
                        time.sleep(0.1)
                        return True
                    except:
                        continue
                        
            except:
                pass
                
            return False

    def dislike(self) -> bool:
        """
        OPTIMIZED dislike method - uses keyboard
        """
        try:
            action = ActionChains(self.browser)
            action.send_keys(Keys.ARROW_LEFT).perform()
            
            time.sleep(0.1)  # Minimal delay
            return True
            
        except:
            return False

    def superlike(self):
        try:
            action = ActionChains(self.browser)
            action.send_keys(Keys.ARROW_UP).perform()
            time.sleep(0.1)
            return True
        except:
            return False

    def get_name(self):
        try:
            xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[1]/div/div/span'
            element = self.browser.find_element(By.XPATH, xpath)
            return element.text
        except:
            try:
                # Alternative xpath
                element = self.browser.find_element(By.XPATH, "//h1[@itemprop='name']")
                return element.text
            except:
                return None

    def get_age(self):
        try:
            xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[1]/div/span'
            element = self.browser.find_element(By.XPATH, xpath)
            age_text = element.text
            # Extract number from text
            age = int(''.join(filter(str.isdigit, age_text)))
            return age
        except:
            return None

    def get_bio_and_passions(self):
        bio = None
        passions = []
        lifestyle = []
        basics = []
        anthem = None
        looking_for = None
        
        try:
            # Get bio
            bio_xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[2]/div/div'
            bio_element = self.browser.find_element(By.XPATH, bio_xpath)
            bio = bio_element.text
        except:
            pass
        
        try:
            # Get passions
            passions_xpath = "//div[contains(@class, 'Bdrs(100px)')]"
            passion_elements = self.browser.find_elements(By.XPATH, passions_xpath)
            for element in passion_elements:
                text = element.text
                if text:
                    passions.append(text)
        except:
            pass
        
        return bio, passions, lifestyle, basics, anthem, looking_for

    def get_image_urls(self, quickload=True):
        image_urls = []
        
        try:
            # Get visible images
            image_elements = self.browser.find_elements(By.XPATH, "//div[@aria-label='Profile slider']")
            for element in image_elements:
                style = element.get_attribute('style')
                if 'background-image' in style:
                    url = style.split('url("')[1].split('")')[0]
                    if url not in image_urls:
                        image_urls.append(url)
            
            if not quickload:
                # Click through all images
                try:
                    bullets = self.browser.find_elements(By.CLASS_NAME, 'bullet')
                    for bullet in bullets:
                        bullet.click()
                        time.sleep(0.5)
                        
                        # Get new images
                        image_elements = self.browser.find_elements(By.XPATH, "//div[@aria-label='Profile slider']")
                        for element in image_elements:
                            style = element.get_attribute('style')
                            if 'background-image' in style:
                                url = style.split('url("')[1].split('")')[0]
                                if url not in image_urls:
                                    image_urls.append(url)
                except:
                    pass
        except:
            pass
        
        return image_urls

    def get_insta(self, bio):
        if bio:
            # Look for Instagram handle pattern
            pattern = r'@[\w.]+|(?:ig|instagram|insta)[:\s]+[\w.]+'
            match = re.search(pattern, bio, re.IGNORECASE)
            if match:
                return match.group(0)
        return None

    def get_row_data(self):
        rowdata = {}
        
        try:
            # Look for location/distance
            distance_elements = self.browser.find_elements(By.XPATH, "//div[contains(text(), 'kilometers away') or contains(text(), 'miles away')]")
            if distance_elements:
                text = distance_elements[0].text
                # Extract number
                distance = int(''.join(filter(str.isdigit, text.split()[0])))
                rowdata['distance'] = distance
        except:
            rowdata['distance'] = None
        
        try:
            # Look for other info rows
            info_rows = self.browser.find_elements(By.XPATH, "//div[@class='Row']")
            for row in info_rows:
                text = row.text
                if 'lives in' in text.lower():
                    rowdata['home'] = text.replace('Lives in', '').strip()
                elif 'works at' in text.lower() or 'works as' in text.lower():
                    rowdata['work'] = text
                elif 'studies' in text.lower() or 'went to' in text.lower():
                    rowdata['study'] = text
        except:
            pass
        
        return rowdata

    def handle_popups_fast(self):
        """
        OPTIMIZED popup handler - checks only common popups
        """
        # Quick check for most common popups only
        common_popups = [
            "//button[contains(text(), 'No Thanks')]",
            "//button[contains(text(), 'Maybe Later')]",
            "//button[@aria-label='Close']",
            "//button[contains(text(), 'Not Interested')]"
        ]
        
        for selector in common_popups:
            try:
                btn = self.browser.find_element(By.XPATH, selector)
                btn.click()
                return True
            except:
                continue
        
        return False