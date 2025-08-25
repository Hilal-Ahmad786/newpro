#!/usr/bin/env python3
"""
🔧 Repair GeomatchHelper Syntax Error
Fixes the indentation issue in geomatch_helper.py
"""

from pathlib import Path

def repair_geomatch_helper():
    print("🔧 Repairing geomatch_helper.py...")
    
    helper_path = Path("tinderbotz/helpers/geomatch_helper.py")
    if not helper_path.exists():
        print("❌ geomatch_helper.py not found!")
        return False
    
    # Read the current content
    try:
        with open(helper_path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Check if there's a backup
    backup_path = Path("tinderbotz/helpers/geomatch_helper.py.backup")
    if backup_path.exists():
        print("✅ Found backup file, restoring...")
        try:
            with open(backup_path, 'r') as f:
                original_content = f.read()
            
            # Write the backup content back
            with open(helper_path, 'w') as f:
                f.write(original_content)
            
            print("✅ Restored from backup")
            content = original_content
        except Exception as e:
            print(f"⚠️ Could not restore backup: {e}")
    else:
        print("⚠️ No backup found, will fix manually")
    
    # Now add the improved like method properly
    print("🔧 Adding improved like method...")
    
    # Find the like method and replace it
    lines = content.split('\n')
    new_lines = []
    in_like_method = False
    method_indent = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is the start of the like method
        if 'def like(self)' in line and not in_like_method:
            in_like_method = True
            method_indent = len(line) - len(line.lstrip())
            
            # Add the new like method
            new_like_method = f'''    def like(self) -> bool:
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
            print(f"⚠️ Keyboard method failed: {{e1}}")
            
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
                    print(f"🎯 Trying like method {{i}}/{{len(like_selectors)}}...")
                    
                    WebDriverWait(self.browser, 3).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    
                    like_button = self.browser.find_element(By.XPATH, selector)
                    like_button.click()
                    print(f"✅ Like successful with method {{i}}")
                    time.sleep(1)
                    return True
                    
                except Exception as e:
                    continue
            
            # Method 3: JavaScript fallback
            try:
                print("🔧 Trying JavaScript click...")
                result = self.browser.execute_script(\"\"\"
                    let buttons = document.querySelectorAll('button');
                    for(let btn of buttons) {{
                        if(btn.innerHTML.includes('Like') || 
                           btn.className.includes('like') || 
                           btn.className.includes('gamepad')) {{
                            btn.click();
                            return true;
                        }}
                    }}
                    return false;
                \"\"\")
                
                if result:
                    print("✅ JavaScript click successful")
                    time.sleep(1)
                    return True
                    
            except Exception as e:
                print(f"❌ JavaScript method failed: {{e}}")
            
            print("❌ All like methods failed")
            return False
            
        except Exception as e:
            print(f"❌ Unexpected error in like method: {{e}}")
            return False'''
            
            new_lines.append(new_like_method)
            
            # Skip the old like method
            i += 1
            while i < len(lines):
                line = lines[i]
                if line.strip() == '' or (line.startswith(' ' * (method_indent + 4))):
                    i += 1
                    continue
                elif line.startswith(' ' * method_indent) and 'def ' in line:
                    # Found next method
                    break
                elif not line.startswith(' '):
                    # Found next class or end of file
                    break
                else:
                    i += 1
            
            in_like_method = False
            continue
            
        new_lines.append(line)
        i += 1
    
    # Write the repaired content
    try:
        with open(helper_path, 'w') as f:
            f.write('\n'.join(new_lines))
        
        print("✅ Repaired geomatch_helper.py")
        return True
        
    except Exception as e:
        print(f"❌ Error writing repaired file: {e}")
        return False

def create_simple_test():
    """Create a simple test script"""
    
    test_script = '''#!/usr/bin/env python3
"""
🧪 Simple Like Test
"""

def test():
    print("🧪 SIMPLE LIKE TEST")
    print("="*30)
    
    try:
        from tinderbotz.session import Session
        print("✅ Import successful")
        
        session = Session(headless=False)
        print("✅ Session created")
        
        # Manual login
        success = session.login_manually(timeout_minutes=5)
        
        if success:
            print("✅ Login successful")
            
            # Try to like 1 profile
            print("\\n🧪 Testing like functionality...")
            session.like(amount=1)
            print("✅ Like test completed")
            
            input("\\nCheck if the profile was actually liked, then press Enter...")
        else:
            print("❌ Login failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test()
'''
    
    with open("simple_test.py", 'w') as f:
        f.write(test_script)
    
    import os
    os.chmod("simple_test.py", 0o755)
    print("✅ Created simple_test.py")

if __name__ == "__main__":
    print("🔧 REPAIRING GEOMATCH HELPER")
    print("="*40)
    
    success = repair_geomatch_helper()
    
    if success:
        create_simple_test()
        
        print("\\n🎉 REPAIR COMPLETE!")
        print("\\n🧪 Test the fix:")
        print("   python simple_test.py")
        
        print("\\n🚀 If test works, use:")
        print("   python smart_bot.py")
        
    else:
        print("\\n❌ Repair failed. You may need to restore the file manually.")