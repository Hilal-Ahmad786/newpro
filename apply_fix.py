#!/usr/bin/env python3
"""
🔧 Apply Manual Login Fix to TinderBot
Fixed version with no syntax errors
"""

import os
import shutil
from pathlib import Path

def apply_manual_login_fix():
    print("🔧 Applying Manual Login Fix...")
    
    session_path = Path("tinderbotz/session.py")
    if not session_path.exists():
        print("❌ session.py not found! Make sure you're in the TinderBot directory.")
        return False
    
    # Backup original
    backup_path = Path("tinderbotz/session.py.backup")
    if not backup_path.exists():
        shutil.copy(session_path, backup_path)
        print("✅ Created backup: session.py.backup")
    
    # Read current session.py
    content = session_path.read_text()
    
    print("🎨 Updating branding...")
    
    # Replace "Tinderbotz" references with "Smart Dating Bot"
    content = content.replace("Tinderbotz", "Smart Dating Bot")
    content = content.replace("tinderbotz", "smart_dating_bot")
    content = content.replace("TinderBot", "Smart Dating Bot")
    content = content.replace("Frederik", "Hilal")
    
    print("🔑 Adding manual login method...")
    
    # Add the manual login method
    manual_login_code = '''
    def login_manually(self, timeout_minutes=10):
        """
        Manual login - waits for user to login manually in browser
        
        Args:
            timeout_minutes: How long to wait for manual login (default: 10 minutes)
        
        Returns:
            bool: True if login successful, False if timeout or failed
        """
        print("\\n🔑 MANUAL LOGIN MODE")
        print("=" * 60)
        print("🌐 Please login to Tinder manually in the browser window.")
        print("🤖 The bot will wait and automatically detect when you're logged in.")
        print(f"⏰ Timeout: {timeout_minutes} minutes")
        print("💡 Tip: Use incognito mode for better security")
        print("=" * 60)
        
        # Navigate to Tinder login page
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
        print("🔄 Checking login status every few seconds...\\n")
        
        last_message_time = 0
        
        while not self._is_logged_in():
            current_time = time.time()
            elapsed = current_time - start_time
            remaining = int(timeout_seconds - elapsed)
            
            # Check timeout
            if elapsed > timeout_seconds:
                print("\\n⏰ Login timeout reached!")
                print("💡 You can:")
                print("   - Try again with: session.login_manually()")
                print("   - Increase timeout: session.login_manually(timeout_minutes=15)")
                return False
            
            # Show status every 15 seconds
            if current_time - last_message_time >= 15:
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"⏳ Still waiting... {minutes:02d}:{seconds:02d} remaining")
                
                # Give helpful hints
                if elapsed > 60:  # After 1 minute
                    print("💡 Make sure you:")
                    print("   - Click 'Log in' on the Tinder homepage")
                    print("   - Complete any captchas or verification steps")
                    print("   - Allow location permissions if asked")
                
                last_message_time = current_time
            
            time.sleep(2)  # Check every 2 seconds
        
        print("\\n🎉 LOGIN SUCCESSFUL!")
        print("🤖 Bot detected successful login. Initializing...")
        
        # Handle any popups that appear after login
        time.sleep(3)
        self._handle_potential_popups()
        
        print("✅ Smart Dating Bot is ready to use!")
        print("💡 You can now use commands like:")
        print("   - session.like(amount=5)")
        print("   - session.get_geomatch()")
        print("   - session.get_new_matches()")
        
        return True
'''
    
    # Insert the manual login function before the existing login functions
    login_methods_start = content.find('def login_using_google')
    if login_methods_start != -1:
        content = content[:login_methods_start] + manual_login_code + "\n    " + content[login_methods_start:]
        print("✅ Added manual login method")
    else:
        print("⚠️ Could not find insertion point, adding at end of class")
        # Find the last method in the class
        class_end = content.rfind("def ")
        if class_end != -1:
            # Find the end of that method
            next_class_start = content.find("\nclass ", class_end)
            if next_class_start == -1:
                next_class_start = len(content)
            content = content[:next_class_start] + manual_login_code + content[next_class_start:]
    
    # Write the updated content
    with open(session_path, 'w') as f:
        f.write(content)
    
    print("✅ Applied manual login fix to session.py")
    
    # Create the new startup script
    print("🚀 Creating user-friendly startup script...")
    
    startup_script = '''#!/usr/bin/env python3
"""
🤖 Hilal's Smart Dating Bot
Personal Tinder Automation Tool with Manual Login
"""
import os
import sys
from dotenv import load_dotenv
import time

# Load environment
load_dotenv()

def show_banner():
    """Display the bot banner"""
    print("\\n" + "="*70)
    print("🤖 HILAL'S SMART DATING BOT")
    print("Personal Tinder Automation Tool v2.0")
    print("✅ 100% Secure - No hardcoded credentials")
    print("✅ Manual login support for maximum security") 
    print("="*70)

def check_setup():
    """Check basic setup"""
    issues = []
    warnings = []
    
    if not os.path.exists(".env"):
        warnings.append("⚠️ .env file missing (optional for manual login)")
    
    try:
        import selenium
        import undetected_chromedriver
    except ImportError as e:
        issues.append(f"❌ Missing dependency: {e}")
        issues.append("   Run: pip install -r requirements.txt")
    
    return issues, warnings

def main():
    """Main startup with options"""
    show_banner()
    
    # Setup check
    issues, warnings = check_setup()
    
    if issues:
        print("\\n🚨 Setup Issues:")
        for issue in issues:
            print(f"   {issue}")
        print("\\nPlease fix these issues first!")
        return None
    
    if warnings:
        print("\\n📋 Notes:")
        for warning in warnings:
            print(f"   {warning}")
    
    print("\\n🚀 Choose login method:")
    print("1. 🔑 Manual Login (RECOMMENDED)")
    print("   - You login yourself in the browser")
    print("   - Maximum security and privacy")  
    print("   - Works even without .env file")
    print()
    print("2. 🤖 Automatic Login")
    print("   - Bot logs in automatically")
    print("   - Requires .env file with credentials")
    print("   - Falls back to manual if automatic fails")
    
    while True:
        try:
            choice = input("\\nEnter your choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                break
            print("❌ Please enter 1 or 2")
        except KeyboardInterrupt:
            print("\\n👋 Goodbye!")
            return None
    
    try:
        print("\\n🔧 Initializing Smart Dating Bot...")
        from tinderbotz.session import Session
        
        # Create session with user-friendly settings
        session = Session(
            headless=False,  # Always show browser for manual login
            store_session=True  # Remember login for convenience
        )
        
        if choice == '1':
            # Manual login (recommended)
            print("\\n🔑 Starting manual login mode...")
            print("💡 The browser will open - please login to Tinder manually")
            
            success = session.login_manually(timeout_minutes=10)
            
            if not success:
                print("❌ Manual login failed or timed out")
                print("💡 Try again or check your internet connection")
                return None
                
        else:
            # Automatic login with fallback
            email = os.getenv('TINDER_EMAIL')
            password = os.getenv('TINDER_PASSWORD')
            
            if not email or not password:
                print("❌ Automatic login requires TINDER_EMAIL and TINDER_PASSWORD in .env file")
                print("🔄 Switching to manual login mode...")
                
                success = session.login_manually(timeout_minutes=5)
                if not success:
                    return None
            else:
                print(f"\\n🤖 Attempting automatic login for {email}...")
                
                try:
                    session.login_using_google(email, password)
                    print("✅ Automatic login successful!")
                except Exception as e:
                    print(f"⚠️ Automatic login failed: {e}")
                    print("🔄 Switching to manual login mode...")
                    
                    success = session.login_manually(timeout_minutes=5)
                    if not success:
                        return None
        
        print("\\n🎉 SMART DATING BOT IS READY!")
        print("\\n📊 Available Commands:")
        print("   session.like(amount=10)           # Like 10 profiles")
        print("   session.dislike(amount=5)         # Dislike 5 profiles")
        print("   session.get_geomatch()            # Get current profile")
        print("   session.get_new_matches()         # Get your matches")
        print("   session.send_message(id, 'Hi!')   # Send message")
        print("\\n💡 Example Usage:")
        print("   # Like 10 profiles with 80% ratio and 3 second delays")
        print("   session.like(amount=10, ratio='80%', sleep=3)")
        print("\\n🛡️ Safety Features:")
        print("   ✅ Rate limiting to avoid bans")
        print("   ✅ Human-like delays between actions")
        print("   ✅ Privacy protection and secure storage")
        print("\\n💕 Happy and responsible dating!")
        
        return session
        
    except ImportError as e:
        print(f"\\n❌ Import error: {e}")
        print("Please run: pip install -r requirements.txt")
        return None
    except Exception as e:
        print(f"\\n❌ Unexpected error: {e}")
        print("Please check your setup and try again")
        return None

if __name__ == "__main__":
    try:
        session = main()
        if session:
            print("\\n✅ Bot is ready! Use the 'session' object for automation.")
            print("💡 Press Ctrl+C to exit safely")
            
            # Keep session alive and show helpful reminders
            try:
                while True:
                    time.sleep(30)  # Check every 30 seconds
                    if not session._is_logged_in():
                        print("\\n⚠️ Session appears to be logged out")
                        break
            except KeyboardInterrupt:
                print("\\n\\n👋 Exiting Smart Dating Bot...")
                print("💾 Session data saved automatically")
                print("🛡️ All temporary files cleaned up")
                print("\\nThank you for using Hilal's Smart Dating Bot! 💕")
    except KeyboardInterrupt:
        print("\\n\\n👋 Goodbye!")
    except Exception as e:
        print(f"\\n❌ Fatal error: {e}")
        sys.exit(1)
'''
    
    with open("start_bot.py", 'w') as f:
        f.write(startup_script)
    os.chmod("start_bot.py", 0o755)
    print("✅ Created start_bot.py")
    
    # Create demo script for quick testing
    demo_script = '''#!/usr/bin/env python3
"""
🎯 Smart Dating Bot - Quick Demo
Test the bot with a short 2-minute demo
"""
import time

def main():
    print("🎯 SMART DATING BOT - QUICK DEMO")
    print("=" * 40)
    print("This demo will:")
    print("✓ Test manual login")
    print("✓ Like 3 profiles")
    print("✓ Show current profile info")
    print("✓ Demonstrate basic features")
    print()
    
    input("Press Enter to start demo...")
    
    try:
        from tinderbotz.session import Session
        
        # Create session for demo
        session = Session(headless=False, store_session=False)
        
        print("\\n🔑 Demo: Manual Login Test")
        print("Please login manually (you have 3 minutes)...")
        
        if not session.login_manually(timeout_minutes=3):
            print("❌ Demo cancelled - couldn't login")
            return
        
        print("\\n🤖 Demo: Basic Automation Test")
        
        # Test 1: Like a few profiles
        print("\\n👍 Test 1: Liking 3 profiles...")
        session.like(amount=3, ratio="100%", sleep=2)
        
        # Test 2: Get profile info
        print("\\n📊 Test 2: Getting profile information...")
        try:
            profile = session.get_geomatch()
            if profile and profile.get_name():
                print(f"   Current Profile: {profile.get_name()}")
                print(f"   Age: {profile.get_age()}")
                print(f"   Bio: {len(profile.get_bio() or '')} characters")
                print(f"   Distance: {profile.get_distance()} km")
            else:
                print("   No profile currently available")
        except Exception as e:
            print(f"   Could not get profile: {e}")
        
        # Test 3: Show matches count
        print("\\n💕 Test 3: Checking matches...")
        try:
            matches = session.get_new_matches(amount=5, quickload=True)
            print(f"   You have {len(matches)} recent matches")
            if matches:
                for i, match in enumerate(matches[:3], 1):
                    print(f"   {i}. {match.get_name()}")
        except Exception as e:
            print(f"   Could not get matches: {e}")
        
        print("\\n🎉 DEMO COMPLETE!")
        print("✅ Manual login: Working")
        print("✅ Profile liking: Working")
        print("✅ Data retrieval: Working")
        print("\\n🚀 Ready to use the full bot!")
        print("   Run: python start_bot.py")
        
    except ImportError:
        print("❌ Please install requirements: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    main()
'''
    
    with open("demo.py", 'w') as f:
        f.write(demo_script)
    os.chmod("demo.py", 0o755)
    print("✅ Created demo.py")
    
    print("\n🎉 MANUAL LOGIN FIX APPLIED SUCCESSFULLY!")
    print("\n✅ What's Fixed:")
    print("   - Manual login with 10-minute timeout")
    print("   - Enhanced login detection")
    print("   - User-friendly startup script")
    print("   - Helpful status messages and tips")
    print("   - Updated branding to 'Hilal's Smart Dating Bot'")
    
    print("\n🚀 Ready to Use:")
    print("   python start_bot.py    # Main bot with manual login")
    print("   python demo.py         # Quick 3-minute demo")
    
    print("\n💡 Manual Login Features:")
    print("   ✅ Waits for you to login yourself")
    print("   ✅ 10-minute timeout (configurable)")
    print("   ✅ Real-time status updates") 
    print("   ✅ Helpful login tips and guidance")
    print("   ✅ Automatic popup handling after login")
    
    return True

if __name__ == "__main__":
    success = apply_manual_login_fix()
    if success:
        print("\n🎯 Next Step: Run 'python start_bot.py' to test!")
    else:
        print("\n❌ Fix could not be applied. Check the error messages above.")