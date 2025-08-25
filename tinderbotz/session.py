# Selenium: automation of browser
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.by import By

# some other imports :-)
import os
import platform
import time
import random
import requests
import atexit
from pathlib import Path

# Hilal's Dating Bot: helper classes
from tinderbotz.helpers.geomatch import Geomatch
from tinderbotz.helpers.match import Match
from tinderbotz.helpers.profile_helper import ProfileHelper
from tinderbotz.helpers.preferences_helper import PreferencesHelper
from tinderbotz.helpers.geomatch_helper import GeomatchHelper
from tinderbotz.helpers.match_helper import MatchHelper
from tinderbotz.helpers.login_helper import LoginHelper
from tinderbotz.helpers.storage_helper import StorageHelper
from tinderbotz.helpers.email_helper import EmailHelper
from tinderbotz.helpers.xpaths import *
from tinderbotz.addproxy import get_proxy_extension


class Session:
    HOME_URL = "https://www.tinder.com/app/recs"

    def __init__(self, headless=False, store_session=False, proxy=None, user_data=False, incognito=True):
        self.email = None
        self.may_send_email = False
        self.session_data = {
            "duration": 0,
            "like": 0,
            "dislike": 0,
            "superlike": 0
        }

        start_session = time.time()

        # this function will run when the session ends
        @atexit.register
        def cleanup():
            # End session duration
            seconds = int(time.time() - start_session)
            self.session_data["duration"] = seconds

            # add session data into a list of messages
            lines = []
            for key in self.session_data:
                message = "{}: {}".format(key, self.session_data[key])
                lines.append(message)

            # print out the statistics of the session
            try:
                box = self._get_msg_box(lines=lines, title="Hilal's Dating Bot")
                print(box)
            finally:
                print("Started session: {}".format(self.started))
                y = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print("Ended session: {}".format(y))
            
            # Close browser properly
            try:
                self.browser.quit()
            except:
                pass

        # Browser setup - COMPLETELY FIXED Chrome options
        options = uc.ChromeOptions()

        # FORCE INCOGNITO MODE for privacy
        if incognito:
            options.add_argument("--incognito")
            print("🕵️ Starting browser in INCOGNITO mode...")
            store_session = False  # Don't store session in incognito mode

        # Create profile if needed
        if store_session and not incognito:
            if not user_data:
                user_data = f"{Path().absolute()}/secure_chrome_profile/"
            if not os.path.isdir(user_data):
                os.mkdir(user_data)
            Path(f'{user_data}First Run').touch()
            options.add_argument(f"--user-data-dir={user_data}")

        # SAFE Browser options - removed all problematic ones
        options.add_argument("--start-maximized")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun") 
        options.add_argument("--password-store=basic")
        options.add_argument("--lang=en-US")
        
        # Privacy & security options
        if incognito:
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--disable-blink-features=AutomationControlled")
        
        # COMPLETELY REMOVED: All experimental options that cause problems
        # NO excludeSwitches
        # NO useAutomationExtension
        # NO experimental options that could cause Chrome errors

        if headless:
            options.headless = True

        # Proxy setup
        if proxy:
            if '@' in proxy:
                parts = proxy.split('@')
                user = parts[0].split(':')[0]
                pwd = parts[0].split(':')[1]
                host = parts[1].split(':')[0]
                port = parts[1].split(':')[1]
                extension = get_proxy_extension(PROXY_HOST=host, PROXY_PORT=port, PROXY_USER=user, PROXY_PASS=pwd)
                options.add_extension(extension)
            else:
                options.add_argument(f'--proxy-server=http://{proxy}')

        # Getting ChromeDriver with multiple fallback attempts
        print("🔧 Getting ChromeDriver...")
        browser_created = False
        
        # Attempt 1: Try with current options
        try:
            self.browser = uc.Chrome(options=options, version_main=None)
            browser_created = True
        except Exception as e1:
            print(f"❌ ChromeDriver error: {e1}")
            print("💡 Trying alternative ChromeDriver setup...")
            
            # Attempt 2: Try with minimal options
            try:
                simple_options = uc.ChromeOptions()
                if incognito:
                    simple_options.add_argument("--incognito")
                simple_options.add_argument("--start-maximized")
                simple_options.add_argument("--no-first-run")
                
                self.browser = uc.Chrome(options=simple_options)
                browser_created = True
            except Exception as e2:
                print(f"❌ Fallback failed: {e2}")
                
                # Attempt 3: Try with no custom options at all
                try:
                    print("💡 Trying with default Chrome options...")
                    self.browser = uc.Chrome()
                    browser_created = True
                except Exception as e3:
                    print(f"❌ Final attempt failed: {e3}")
                    print("🛠️ Please try:")
                    print("   1. Update Chrome: chrome://settings/help")
                    print("   2. Run: pip install --upgrade undetected-chromedriver")
                    print("   3. Restart terminal and try again")
                    raise e3
        
        if not browser_created:
            raise Exception("Could not create Chrome browser")
        
        # Additional stealth settings (only if browser was created successfully)
        try:
            self.browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        except:
            pass  # Continue if this fails
        
        # Personalized banner
        print("\n" + "="*60)
        if incognito:
            print("🤖 HILAL'S SMART DATING BOT - INCOGNITO MODE")
        else:
            print("🤖 HILAL'S SMART DATING BOT")
        print("="*60)
        print("🇹🇷 Optimized for Turkey & International Dating")
        print("⚡ Fast & Secure Automation")
        print("🔒 Privacy-First Design")
        if incognito:
            print("🕵️ No data will be saved after session ends")
        print("="*60)
        time.sleep(1)

        self.started = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Started session: {}\n".format(self.started))

    # Setting a custom location
    def set_custom_location(self, latitude, longitude, accuracy="100%"):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": int(accuracy.split('%')[0])
        }
        self.browser.execute_cdp_cmd("Page.setGeolocationOverride", params)

    def set_email_notifications(self, boolean):
        self.may_send_email = boolean

    def set_distance_range(self, km):
        helper = PreferencesHelper(browser=self.browser)
        helper.set_distance_range(km)

    def set_age_range(self, min, max):
        helper = PreferencesHelper(browser=self.browser)
        helper.set_age_range(min, max)

    def set_sexuality(self, type):
        helper = PreferencesHelper(browser=self.browser)
        helper.set_sexualitiy(type)

    def set_global(self, boolean):
        helper = PreferencesHelper(browser=self.browser)
        helper.set_global(boolean)

    def set_bio(self, bio):
        helper = ProfileHelper(browser=self.browser)
        helper.set_bio(bio)

    def add_photo(self, filepath):
        helper = ProfileHelper(browser=self.browser)
        helper.add_photo(filepath)

    # Login methods
    def login_manually(self, timeout_minutes=10):
        """
        Manual login - waits for user to login manually in browser
        """
        print("\n🔑 MANUAL LOGIN MODE")
        print("=" * 60)
        print("🌐 Please login to Tinder manually in the browser window.")
        print("🤖 The bot will wait and automatically detect when you're logged in.")
        print(f"⏰ Timeout: {timeout_minutes} minutes")
        print("💡 Tip: Use Google or Facebook login for best results")
        print("=" * 60)
        
        # Navigate to Tinder
        if not "tinder" in self.browser.current_url:
            print("🌍 Opening Tinder website...")
            self.browser.get("https://tinder.com/")
            time.sleep(3)
        
        # Check if already logged in
        if self._is_logged_in():
            print("✅ Already logged in! Proceeding...")
            self._handle_potential_popups()
            return True
        
        start_time = time.time()
        timeout_seconds = timeout_minutes * 60
        
        print("⏳ Waiting for you to complete login...")
        print("💻 Please login in the browser window that opened")
        print("🔄 Checking login status every few seconds...\n")
        
        last_message_time = 0
        
        while not self._is_logged_in():
            current_time = time.time()
            elapsed = current_time - start_time
            remaining = int(timeout_seconds - elapsed)
            
            # Check timeout
            if elapsed > timeout_seconds:
                print("\n⏰ Login timeout reached!")
                print("💡 You can try again or increase timeout")
                return False
            
            # Show status every 15 seconds
            if current_time - last_message_time >= 15:
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"⏳ Still waiting... {minutes:02d}:{seconds:02d} remaining")
                last_message_time = current_time
            
            time.sleep(2)
        
        print("\n🎉 LOGIN SUCCESSFUL!")
        print("🤖 Hilal's Dating Bot is ready!")
        
        # Handle popups after login
        time.sleep(3)
        self._handle_potential_popups()
        
        return True

    def login_using_google(self, email, password):
        self.email = email
        if not self._is_logged_in():
            helper = LoginHelper(browser=self.browser)
            helper.login_by_google(email, password)
            time.sleep(5)
        if not self._is_logged_in():
            print('Manual login required. Please complete login manually.')
            return self.login_manually()

    def login_using_facebook(self, email, password):
        self.email = email
        if not self._is_logged_in():
            helper = LoginHelper(browser=self.browser)
            helper.login_by_facebook(email, password)
            time.sleep(5)
        if not self._is_logged_in():
            print('Manual login required. Please complete login manually.')
            return self.login_manually()

    def login_using_sms(self, country, phone_number):
        if not self._is_logged_in():
            helper = LoginHelper(browser=self.browser)
            helper.login_by_sms(country, phone_number)
            time.sleep(5)
        if not self._is_logged_in():
            print('Manual login required. Please complete login manually.')
            return self.login_manually()

    # Core actions
    def like(self, amount=1, ratio='100%', sleep=1, randomize_sleep=True):
        initial_sleep = sleep
        ratio = float(ratio.split('%')[0]) / 100

        if self._is_logged_in():
            helper = GeomatchHelper(browser=self.browser)
            amount_liked = 0
            self._handle_potential_popups()
            print(f"\n👍 Starting to like {amount} profiles...")
            
            while amount_liked < amount:
                if randomize_sleep:
                    sleep = random.uniform(0.5, 2.3) * initial_sleep
                    
                if random.random() <= ratio:
                    if helper.like():
                        amount_liked += 1
                        self.session_data['like'] += 1
                        print(f"✅ {amount_liked}/{amount} liked (sleep: {sleep:.1f}s)")
                    else:
                        print(f"⚠️ Like failed - may be out of profiles")
                        break
                else:
                    helper.dislike()
                    self.session_data['dislike'] += 1

                time.sleep(sleep)

            print(f"🎉 Completed! Liked {amount_liked} profiles")
            self._print_liked_stats()

    def dislike(self, amount=1):
        if self._is_logged_in():
            helper = GeomatchHelper(browser=self.browser)
            print(f"\n👎 Disliking {amount} profiles...")
            for i in range(amount):
                self._handle_potential_popups()
                helper.dislike()
                self.session_data['dislike'] += 1
                print(f"✅ {i+1}/{amount} disliked")
            self._print_liked_stats()

    def superlike(self, amount=1):
        if self._is_logged_in():
            helper = GeomatchHelper(browser=self.browser)
            print(f"\n⭐ Super-liking {amount} profiles...")
            for i in range(amount):
                self._handle_potential_popups()
                helper.superlike()
                self.session_data['superlike'] += 1
                print(f"✅ {i+1}/{amount} super-liked")
                time.sleep(1)
            self._print_liked_stats()

    # Data methods
    def get_geomatch(self, quickload=True):
        if self._is_logged_in():
            helper = GeomatchHelper(browser=self.browser)
            self._handle_potential_popups()

            # Get profile data
            name = None
            attempts = 0
            while not name and attempts < 3:
                attempts += 1
                name = helper.get_name()
                if not name:
                    time.sleep(1)

            age = helper.get_age()
            bio, passions, lifestyle, basics, anthem, looking_for = helper.get_bio_and_passions()
            image_urls = helper.get_image_urls(quickload)
            instagram = helper.get_insta(bio)
            rowdata = helper.get_row_data()

            return Geomatch(
                name=name, age=age, 
                work=rowdata.get('work'), 
                gender=rowdata.get('gender'), 
                study=rowdata.get('study'), 
                home=rowdata.get('home'), 
                distance=rowdata.get('distance'),
                bio=bio, passions=passions, 
                lifestyle=lifestyle, basics=basics, 
                anthem=anthem, looking_for=looking_for, 
                image_urls=image_urls, instagram=instagram
            )

    def get_new_matches(self, amount=100, quickload=True):
        if self._is_logged_in():
            helper = MatchHelper(browser=self.browser)
            self._handle_potential_popups()
            return helper.get_new_matches(amount, quickload)

    def get_messaged_matches(self, amount=100, quickload=True):
        if self._is_logged_in():
            helper = MatchHelper(browser=self.browser)
            self._handle_potential_popups()
            return helper.get_messaged_matches(amount, quickload)

    def send_message(self, chatid, message):
        if self._is_logged_in():
            helper = MatchHelper(browser=self.browser)
            self._handle_potential_popups()
            helper.send_message(chatid, message)

    # Utility methods
    def _handle_potential_popups(self):
        """Handle common Tinder popups"""
        delay = 0.25

        try:
            base_element = self.browser.find_element(By.XPATH, '/html/body/div[2]')
        except:
            return None

        # Common popup dismissals
        popup_buttons = [
            './/main/div/div/div[3]/button[2]',  # Deny see who liked you
            './/main/div/button[2]',  # Deny upgrade to superlike
            './/main/div/div[2]/button[2]',  # Deny add to homescreen
            './/main/div/div[3]/button[2]',  # Deny buying more superlikes
            '//button[@title="Back to Tinder"]',  # Dismiss match popup
            ".//*[contains(text(), 'No Thanks')]",  # Generic no thanks
        ]

        for xpath in popup_buttons:
            try:
                btn = base_element.find_element(By.XPATH, xpath)
                btn.click()
                time.sleep(0.5)
                return f"POPUP: Dismissed popup"
            except (NoSuchElementException, TimeoutException):
                continue

        return None

    def _is_logged_in(self):
        if not "tinder" in self.browser.current_url:
            self.browser.get("https://tinder.com/?lang=en")
            time.sleep(1.5)

        return "tinder.com/app/" in self.browser.current_url

    def _get_msg_box(self, lines, indent=1, width=None, title=None):
        """Print message-box with optional title."""
        space = " " * indent
        if not width:
            width = max(map(len, lines))
        box = f'/{"=" * (width + indent * 2)}\\\n'
        if title:
            box += f'|{space}{title:<{width}}{space}|\n'
            box += f'|{space}{"-" * len(title):<{width}}{space}|\n'
        box += ''.join([f'|{space}{line:<{width}}{space}|\n' for line in lines])
        box += f'\\{"=" * (width + indent * 2)}/'
        return box

    def _print_liked_stats(self):
        likes = self.session_data['like']
        dislikes = self.session_data['dislike']
        superlikes = self.session_data['superlike']

        if superlikes > 0:
            print(f"⭐ Super-liked: {superlikes} profiles")
        if likes > 0:
            print(f"👍 Liked: {likes} profiles")
        if dislikes > 0:
            print(f"👎 Disliked: {dislikes} profiles")

    def store_local(self, match):
        """Store match data locally"""
        if isinstance(match, Match):
            filename = 'matches'
        elif isinstance(match, Geomatch):
            filename = 'geomatches'
        else:
            print("Unknown match type, cannot store locally")
            return

        # Store images
        for url in match.image_urls:
            hashed_image = StorageHelper.store_image_as(url=url, directory='data/{}/images'.format(filename))
            match.images_by_hashes.append(hashed_image)

        # Store userdata
        StorageHelper.store_match(match=match, directory='data/{}'.format(filename), filename=filename)