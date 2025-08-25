#!/usr/bin/env python3
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
            print("\n🧪 Testing like functionality...")
            session.like(amount=1)
            print("✅ Like test completed")
            
            input("\nCheck if the profile was actually liked, then press Enter...")
        else:
            print("❌ Login failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test()
