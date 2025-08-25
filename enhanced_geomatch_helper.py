from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
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

    def check_out_of_matches(self):
        """
        Check if we've run out of matches in current area
        Returns True if out of matches, False otherwise
        """
        try:
            # Look for the "run out of matches" message
            out_of_matches_xpath = "//div[contains(@class, 'Mb(20px)') and contains(text(), \"We've run out of potential matches in your area\")]"
            
            out_of_matches_element = self.browser.find_element(By.XPATH, out_of_matches_xpath)
            if out_of_matches_element:
                print("🚫 Out of matches in current location!")
                return True
        except NoSuchElementException:
            pass
        
        return False

    def change_location(self, city_name):
        """
        Change location to specified city
        Returns True if successful, False otherwise
        """
        print(f"\n🌍 Changing location to: {city_name}")
        
        try:
            # Step 1: Click on profile/avatar
            print("   📋 Step 1: Opening profile...")
            profile_xpath = "//a[@title='My Profile' and @href='/app/profile']"
            
            try:
                profile_btn = WebDriverWait(self.browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, profile_xpath))
                )
                profile_btn.click()
                time.sleep(2)
                print("   ✅ Profile opened")
            except TimeoutException:
                print("   ❌ Could not find profile button")
                return False

            # Step 2: Click on Location setting
            print("   📍 Step 2: Opening location settings...")
            location_xpath = "//a[@aria-label='Location' and contains(@href, '/app/settings/plus/passport')]"
            
            try:
                location_btn = WebDriverWait(self.browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, location_xpath))
                )
                location_btn.click()
                time.sleep(2)
                print("   ✅ Location settings opened")
            except TimeoutException:
                print("   ❌ Could not find location settings")
                return False

            # Step 3: Enter city name in search
            print(f"   🔍 Step 3: Searching for {city_name}...")
            search_xpath = "//input[@aria-label='Search a Location' and @placeholder='Search a Location']"
            
            try:
                search_input = WebDriverWait(self.browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, search_xpath))
                )
                search_input.clear()
                search_input.send_keys(city_name)
                time.sleep(2)
                print("   ✅ City name entered")
            except TimeoutException:
                print("   ❌ Could not find search input")
                return False

            # Step 4: Click on dropdown result
            print("   📋 Step 4: Selecting from dropdown...")
            # More flexible xpath that looks for the city name in dropdown
            city_base_name = city_name.split(',')[0].strip()  # Get just the city name without country
            dropdown_xpath = f"//div[contains(@class, 'passport__search__item') or (h3[contains(text(), '{city_base_name}')])]"
            
            try:
                dropdown_item = WebDriverWait(self.browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
                )
                dropdown_item.click()
                time.sleep(3)
                print("   ✅ Dropdown selection made")
            except TimeoutException:
                print("   ❌ Could not find dropdown item")
                return False

            # Step 5: Click on location marker
            print("   📌 Step 5: Confirming location...")
            marker_xpath = "//div[contains(@class, 'passport__locationMarker')]"
            
            try:
                marker = WebDriverWait(self.browser, 8).until(
                    EC.element_to_be_clickable((By.XPATH, marker_xpath))
                )
                # Scroll marker into view
                self.browser.execute_script("arguments[0].scrollIntoView(true);", marker)
                time.sleep(1)
                marker.click()
                time.sleep(3)
                print("   ✅ Location marker clicked")
            except TimeoutException:
                print("   ❌ Could not find location marker")
                return False

            # Step 6: Return to swiping
            print("   🏠 Step 6: Returning to swiping...")
            self.browser.get(self.HOME_URL)
            time.sleep(3)
            
            print(f"✅ Location successfully changed to {city_name}")
            return True

        except Exception as e:
            print(f"❌ Error changing location: {e}")
            # Try to return to home page anyway
            try:
                self.browser.get(self.HOME_URL)
                time.sleep(2)
            except:
                pass
            return False

    def dismiss_upgrade_popup(self):
        """
        Dismiss the 'Upgrade Your Like' popup
        Returns True if popup was found and dismissed, False otherwise
        """
        try:
            # Look for "No Thanks" button in upgrade popup
            no_thanks_xpath = "//button[.//div[contains(@class, 'lxn9zzn') and contains(text(), 'No Thanks')]]"
            
            no_thanks_btn = self.browser.find_element(By.XPATH, no_thanks_xpath)
            no_thanks_btn.click()
            time.sleep(1)
            print("   🔧 Dismissed upgrade popup")
            return True
            
        except NoSuchElementException:
            # Also try alternative xpath patterns
            alternative_xpaths = [
                "//button[contains(@class, 'c1p6lbu0') and .//div[text()='No Thanks']]",
                "//div[contains(text(), 'No Thanks')]/ancestor::button",
                "//button[@type='button' and contains(., 'No Thanks')]"
            ]
            
            for xpath in alternative_xpaths:
                try:
                    btn = self.browser.find_element(By.XPATH, xpath)
                    btn.click()
                    time.sleep(1)
                    print("   🔧 Dismissed upgrade popup (alternative)")
                    return True
                except NoSuchElementException:
                    continue
        
        return False

    def like(self) -> bool:
        """
        ENHANCED like method with smart detection
        Only clicks if like button is actually present and clickable
        """
        try:
            # First check for popups and dismiss them
            if self.dismiss_upgrade_popup():
                time.sleep(1)
            
            # Method 1: Look for the specific like button with gamepad styling
            like_button_xpath = "//button[contains(@class, 'gamepad-button') and .//span[text()='Like']]"
            
            try:
                like_btn = WebDriverWait(self.browser, 2).until(
                    EC.element_to_be_clickable((By.XPATH, like_button_xpath))
                )
                
                # Double check that the button is actually visible and interactable
                if like_btn.is_displayed() and like_btn.is_enabled():
                    like_btn.click()
                    time.sleep(0.3)
                    print("   👍 Liked using button click")
                    return True
                else:
                    print("   ⚠️ Like button not ready, trying keyboard")
                    
            except (TimeoutException, ElementClickInterceptedException):
                pass
            
            # Method 2: Try keyboard shortcut as fallback
            try:
                action = ActionChains(self.browser)
                action.send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(0.3)
                print("   👍 Liked using keyboard")
                return True
                
            except Exception as e:
                print(f"   ❌ Keyboard like failed: {e}")
            
            # Method 3: Alternative button selectors
            alternative_selectors = [
                "//div[contains(@class, 'gamepad-button-wrapper')]//button[contains(@class, 'gamepad-button')]",
                "//button[contains(@class, 'Bgc($c-ds-background-gamepad-sparks-like-default)')]",
                "//button[@aria-label='Like' or @title='Like']"
            ]
            
            for selector in alternative_selectors:
                try:
                    btn = self.browser.find_element(By.XPATH, selector)
                    if btn.is_displayed() and btn.is_enabled():
                        btn.click()
                        time.sleep(0.3)
                        print("   👍 Liked using alternative selector")
                        return True
                except:
                    continue
            
            print("   ⚠️ No like button available - may be out of profiles")
            return False
            
        except Exception as e:
            print(f"   ❌ Like error: {e}")
            return False

    def dislike(self) -> bool:
        """
        ENHANCED dislike method with smart detection
        """
        try:
            # First check for popups
            if self.dismiss_upgrade_popup():
                time.sleep(1)
            
            # Method 1: Keyboard shortcut (most reliable)
            try:
                action = ActionChains(self.browser)
                action.send_keys(Keys.ARROW_LEFT).perform()
                time.sleep(0.3)
                return True
            except:
                pass
            
            # Method 2: Look for dislike button
            dislike_selectors = [
                "//button[contains(@class, 'gamepad-button') and .//span[text()='Pass']]",
                "//div[contains(@class, 'gamepad-button-wrapper')]//button[contains(@class, 'gamepad-button')][1]",
                "//button[@aria-label='Pass' or @title='Pass']"
            ]
            
            for selector in dislike_selectors:
                try:
                    btn = self.browser.find_element(By.XPATH, selector)
                    if btn.is_displayed() and btn.is_enabled():
                        btn.click()
                        time.sleep(0.3)
                        return True
                except:
                    continue
            
            return False
            
        except Exception as e:
            print(f"   ❌ Dislike error: {e}")
            return False

    def superlike(self):
        """Enhanced superlike with smart detection"""
        try:
            if self.dismiss_upgrade_popup():
                time.sleep(1)
            
            # Keyboard shortcut
            action = ActionChains(self.browser)
            action.send_keys(Keys.ARROW_UP).perform()
            time.sleep(0.3)
            return True
        except:
            return False

    def smart_swipe_session(self, cities, swipes_per_city=25):
        """
        Intelligent swiping session that automatically changes location when out of matches
        
        Args:
            cities: List of city names to rotate through
            swipes_per_city: Number of swipes per city
            
        Returns:
            Dict with session statistics
        """
        print(f"\n🤖 SMART SWIPE SESSION STARTED")
        print(f"   🌍 Cities: {len(cities)}")
        print(f"   👍 Swipes per city: {swipes_per_city}")
        
        stats = {
            'cities_visited': 0,
            'total_swipes': 0,
            'likes': 0,
            'dislikes': 0,
            'location_changes': 0,
            'popups_dismissed': 0
        }
        
        current_city_index = 0
        
        for city_index, city in enumerate(cities):
            print(f"\n📍 City {city_index + 1}/{len(cities)}: {city}")
            
            # Change location if not first city or if out of matches
            if city_index > 0 or self.check_out_of_matches():
                if self.change_location(city):
                    stats['location_changes'] += 1
                    stats['cities_visited'] += 1
                    time.sleep(3)  # Wait for location change to take effect
                else:
                    print(f"   ❌ Failed to change to {city}, skipping...")
                    continue
            else:
                stats['cities_visited'] += 1
            
            # Swipe in current city
            city_swipes = 0
            city_likes = 0
            city_dislikes = 0
            
            while city_swipes < swipes_per_city:
                # Check if we ran out of matches
                if self.check_out_of_matches():
                    print(f"   🚫 Ran out of matches in {city} after {city_swipes} swipes")
                    break
                
                # Dismiss any popups
                if self.dismiss_upgrade_popup():
                    stats['popups_dismissed'] += 1
                    continue
                
                # Decide like or dislike (85% like rate)
                should_like = random.random() < 0.85
                
                if should_like:
                    if self.like():
                        city_likes += 1
                        stats['likes'] += 1
                        print(f"   👍 {city_swipes + 1}/{swipes_per_city}: Liked")
                    else:
                        print(f"   ⚠️ {city_swipes + 1}/{swipes_per_city}: Like failed, may be out of profiles")
                        break
                else:
                    if self.dislike():
                        city_dislikes += 1
                        stats['dislikes'] += 1
                        print(f"   👎 {city_swipes + 1}/{swipes_per_city}: Disliked")
                    else:
                        print(f"   ⚠️ {city_swipes + 1}/{swipes_per_city}: Dislike failed")
                        break
                
                city_swipes += 1
                stats['total_swipes'] += 1
                
                # Smart delay (0.5-2.5 seconds)
                delay = random.uniform(0.5, 2.5)
                time.sleep(delay)
                
                # Progress update every 10 swipes
                if city_swipes % 10 == 0:
                    success_rate = (city_likes / city_swipes) * 100 if city_swipes > 0 else 0
                    print(f"   📊 Progress: {city_swipes}/{swipes_per_city} | Likes: {city_likes} | Rate: {success_rate:.1f}%")
            
            # City summary
            print(f"   ✅ {city} completed: {city_swipes} swipes, {city_likes} likes, {city_dislikes} dislikes")
            
            # Brief pause between cities
            if city_index < len(cities) - 1:
                print("   ⏸️ Brief pause before next city...")
                time.sleep(3)
        
        # Final statistics
        print(f"\n🎉 SMART SWIPE SESSION COMPLETED!")
        print(f"   🌍 Cities visited: {stats['cities_visited']}")
        print(f"   📍 Location changes: {stats['location_changes']}")  
        print(f"   👍 Total likes: {stats['likes']}")
        print(f"   👎 Total dislikes: {stats['dislikes']}")
        print(f"   📊 Total swipes: {stats['total_swipes']}")
        print(f"   🔧 Popups dismissed: {stats['popups_dismissed']}")
        
        if stats['total_swipes'] > 0:
            like_rate = (stats['likes'] / stats['total_swipes']) * 100
            print(f"   📈 Overall like rate: {like_rate:.1f}%")
        
        return stats

    # Keep existing methods for compatibility
    def get_name(self):
        try:
            xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[1]/div/div/span'
            element = self.browser.find_element(By.XPATH, xpath)
            return element.text
        except:
            try:
                element = self.browser.find_element(By.XPATH, "//h1[@itemprop='name']")
                return element.text
            except:
                return None

    def get_age(self):
        try:
            xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[1]/div/span'
            element = self.browser.find_element(By.XPATH, xpath)
            age_text = element.text
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
            bio_xpath = f'{content}/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div/div[2]/div/div'
            bio_element = self.browser.find_element(By.XPATH, bio_xpath)
            bio = bio_element.text
        except:
            pass
        
        try:
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
            image_elements = self.browser.find_elements(By.XPATH, "//div[@aria-label='Profile slider']")
            for element in image_elements:
                style = element.get_attribute('style')
                if 'background-image' in style:
                    url = style.split('url("')[1].split('")')[0]
                    if url not in image_urls:
                        image_urls.append(url)
            
            if not quickload:
                try:
                    bullets = self.browser.find_elements(By.CLASS_NAME, 'bullet')
                    for bullet in bullets:
                        bullet.click()
                        time.sleep(0.5)
                        
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
            pattern = r'@[\w.]+|(?:ig|instagram|insta)[:\s]+[\w.]+'
            match = re.search(pattern, bio, re.IGNORECASE)
            if match:
                return match.group(0)
        return None

    def get_row_data(self):
        rowdata = {}
        
        try:
            distance_elements = self.browser.find_elements(By.XPATH, "//div[contains(text(), 'kilometers away') or contains(text(), 'miles away')]")
            if distance_elements:
                text = distance_elements[0].text
                distance = int(''.join(filter(str.isdigit, text.split()[0])))
                rowdata['distance'] = distance
        except:
            rowdata['distance'] = None
        
        try:
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