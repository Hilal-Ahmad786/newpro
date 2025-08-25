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

    def like(self) -> bool:
        """
        Enhanced like method that works with current Tinder interface
        """
        try:
            # Method 1: Try keyboard shortcut (most reliable)
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.action_chains import ActionChains
            
            action = ActionChains(self.browser)
            action.send_keys(Keys.ARROW_RIGHT).perform()
            print("✅ Like sent via keyboard shortcut")
            time.sleep(1)
            return True
            
        except Exception as e1:
            print(f"⚠️ Keyboard method failed: {e1}")
            
            # Method 2: Try multiple button selectors
            like_selectors = [
                # New Tinder like button
                "//button[contains(@class, 'gamepad-button') and contains(@class, 'Bgc')]",
                "//button[.//span[contains(text(), 'Like')]]",
                "//button[@aria-label='Like']",
                "//button[contains(@class, 'like')]",
                "//button[.//svg[contains(@class, 'gamepad-icon')]]",
                "//div[@role='button' and contains(@aria-label, 'Like')]",
            ]
            
            for i, selector in enumerate(like_selectors, 1):
                try:
                    print(f"🎯 Trying like method {i}/{len(like_selectors)}...")
                    
                    WebDriverWait(self.browser, 3).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    
                    like_button = self.browser.find_element(By.XPATH, selector)
                    like_button.click()
                    print(f"✅ Like successful with method {i}")
                    time.sleep(1)
                    return True
                    
                except Exception as e:
                    continue
            
            # Method 3: JavaScript fallback
            try:
                print("🔧 Trying JavaScript click...")
                result = self.browser.execute_script("""
                    let buttons = document.querySelectorAll('button');
                    for(let btn of buttons) {
                        if(btn.innerHTML.includes('Like') || 
                           btn.className.includes('like') || 
                           btn.className.includes('gamepad')) {
                            btn.click();
                            return true;
                        }
                    }
                    return false;
                """)
                
                if result:
                    print("✅ JavaScript click successful")
                    time.sleep(1)
                    return True
                    
            except Exception as e:
                print(f"❌ JavaScript method failed: {e}")
            
            print("❌ All like methods failed")
            return False
            
        except Exception as e:
            print(f"❌ Unexpected error in like method: {e}")
            return False