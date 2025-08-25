#!/usr/bin/env python3
"""
🔧 Fix Like Button Detection for Current Tinder Interface
Updates the GeomatchHelper to work with the new Tinder button structure
"""

from pathlib import Path
import re

def fix_like_button():
    print("🔧 Fixing like button detection...")
    
    # Update GeomatchHelper
    geomatch_helper_path = Path("tinderbotz/helpers/geomatch_helper.py")
    if not geomatch_helper_path.exists():
        print("❌ geomatch_helper.py not found!")
        return False
    
    content = geomatch_helper_path.read_text()
    
    # Create improved like method
    new_like_method = '''    def like(self) -> bool:
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
                # New Tinder like button (from your HTML)
                "//button[contains(@class, 'gamepad-button') and contains(@class, 'Bgc($c-ds-background-gamepad-sparks-like-default)')]",
                
                # Alternative selectors for like button
                "//button[.//span[contains(text(), 'Like')]]",
                "//button[@aria-label='Like']",
                "//button[contains(@class, 'like')]",
                
                # SVG-based detection (heart icon)
                "//button[.//svg[contains(@class, 'gamepad-icon')]]",
                "//button[.//path[contains(@d, 'M24 8.845')]]",  # Heart SVG path from your HTML
                
                # Fallback selectors
                "//div[@role='button' and contains(@aria-label, 'Like')]",
                "//button[contains(@class, 'button') and contains(@class, 'gamepad')]"
            ]
            
            for i, selector in enumerate(like_selectors, 1):
                try:
                    print(f"🎯 Trying like method {i}/{len(like_selectors)}: {selector[:50]}...")
                    
                    WebDriverWait(self.browser, 3).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    
                    like_button = self.browser.find_element(By.XPATH, selector)
                    
                    # Scroll into view if needed
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", like_button)
                    time.sleep(0.5)
                    
                    # Try clicking
                    like_button.click()
                    print(f"✅ Like successful with method {i}")
                    time.sleep(1)
                    return True
                    
                except Exception as e:
                    print(f"   ❌ Method {i} failed: {str(e)[:100]}")
                    continue
            
            # Method 3: Try JavaScript click as last resort
            try:
                print("🔧 Trying JavaScript click method...")
                
                # Find any button that looks like a like button
                js_script = """
                // Find like button by various methods
                let likeButton = null;
                
                // Method 1: Look for heart SVG
                const heartButtons = document.querySelectorAll('button svg');
                for(let svg of heartButtons) {
                    if(svg.innerHTML.includes('M24 8.845') || svg.innerHTML.includes('path')) {
                        likeButton = svg.closest('button');
                        break;
                    }
                }
                
                // Method 2: Look for like class names
                if(!likeButton) {
                    likeButton = document.querySelector('button[class*="like"], button[class*="gamepad"]');
                }
                
                // Method 3: Look for button with heart characteristics
                if(!likeButton) {
                    const buttons = document.querySelectorAll('button');
                    for(let btn of buttons) {
                        if(btn.innerHTML.includes('Like') || btn.innerHTML.includes('heart') || 
                           btn.className.includes('sparks-like')) {
                            likeButton = btn;
                            break;
                        }
                    }
                }
                
                if(likeButton) {
                    likeButton.click();
                    return true;
                } else {
                    return false;
                }
                """
                
                result = self.browser.execute_script(js_script)
                if result:
                    print("✅ JavaScript click successful")
                    time.sleep(1)
                    return True
                else:
                    print("❌ No like button found via JavaScript")
                    
            except Exception as e:
                print(f"❌ JavaScript method failed: {e}")
            
            print("❌ All like methods failed")
            return False
            
        except Exception as e:
            print(f"❌ Unexpected error in like method: {e}")
            return False'''
    
    # Replace the existing like method
    like_method_pattern = r'def like\(self\).*?(?=\n    def|\nclass|\Z)'
    
    if re.search(like_method_pattern, content, re.DOTALL):
        content = re.sub(like_method_pattern, new_like_method, content, flags=re.DOTALL)
        print("✅ Replaced existing like method")
    else:
        print("⚠️ Could not find existing like method, appending new one")
        # Find a good place to insert
        insert_point = content.find("def dislike(self):")
        if insert_point > 0:
            content = content[:insert_point] + new_like_method + "\n\n    " + content[insert_point:]
        else:
            content += "\n" + new_like_method
    
    # Write the updated content
    with open(geomatch_helper_path, 'w') as f:
        f.write(content)
    
    print("✅ Updated like method in geomatch_helper.py")
    return True

def create_test_script():
    """Create a test script to verify the like button works"""
    
    test_script = '''#!/usr/bin/env python3
"""
🧪 Test Like Button Functionality
Quick test to see if the like button detection works
"""

def test_like_button():
    print("🧪 TESTING LIKE BUTTON DETECTION")
    print("="*50)
    
    try:
        from tinderbotz.session import Session
        
        # Create session
        print("🔧 Creating session...")
        session = Session(headless=False, store_session=False)
        
        # Manual login
        print("🔑 Please login manually...")
        success = session.login_manually(timeout_minutes=5)
        
        if not success:
            print("❌ Login failed")
            return
        
        print("✅ Login successful!")
        
        # Test like button detection
        print("\\n🎯 Testing like button detection...")
        
        from tinderbotz.helpers.geomatch_helper import GeomatchHelper
        helper = GeomatchHelper(session.browser)
        
        for test_num in range(3):
            print(f"\\n🧪 Test {test_num + 1}/3:")
            print("   Attempting to like current profile...")
            
            success = helper.like()
            
            if success:
                print("   ✅ Like button clicked successfully!")
            else:
                print("   ❌ Like button click failed")
            
            # Wait a bit before next test
            import time
            time.sleep(3)
        
        print("\\n🎯 Test completed!")
        print("Check if profiles were actually liked in the Tinder interface")
        
        input("\\nPress Enter to exit...")
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_like_button()
'''
    
    with open("test_like.py", 'w') as f:
        f.write(test_script)
    
    import os
    os.chmod("test_like.py", 0o755)
    
    print("✅ Created test_like.py")

def main():
    print("🔧 FIXING LIKE BUTTON DETECTION")
    print("="*50)
    
    # Fix the like button method
    success = fix_like_button()
    
    if success:
        # Create test script
        create_test_script()
        
        print("\n🎉 LIKE BUTTON FIX COMPLETE!")
        print("\n✅ What was fixed:")
        print("   - Updated like button selectors for current Tinder interface")
        print("   - Added multiple detection methods (keyboard, click, JavaScript)")
        print("   - Enhanced error handling and debugging")
        print("   - Added fallback methods for reliability")
        
        print("\n🧪 Testing:")
        print("   python test_like.py    # Test the like button detection")
        
        print("\n🚀 Usage:")
        print("   python smart_bot.py    # Use the updated bot")
        
        print("\n💡 The new like method tries:")
        print("   1. ⌨️ Keyboard shortcut (most reliable)")
        print("   2. 🖱️ Button clicking with multiple selectors")
        print("   3. 🔧 JavaScript injection as fallback")
        
    else:
        print("❌ Failed to apply like button fix")

if __name__ == "__main__":
    main()