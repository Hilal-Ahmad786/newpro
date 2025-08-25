#!/usr/bin/env python3
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
        print("\n🎯 Testing like button detection...")
        
        from tinderbotz.helpers.geomatch_helper import GeomatchHelper
        helper = GeomatchHelper(session.browser)
        
        for test_num in range(3):
            print(f"\n🧪 Test {test_num + 1}/3:")
            print("   Attempting to like current profile...")
            
            success = helper.like()
            
            if success:
                print("   ✅ Like button clicked successfully!")
            else:
                print("   ❌ Like button click failed")
            
            # Wait a bit before next test
            import time
            time.sleep(3)
        
        print("\n🎯 Test completed!")
        print("Check if profiles were actually liked in the Tinder interface")
        
        input("\nPress Enter to exit...")
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_like_button()
