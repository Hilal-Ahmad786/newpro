#!/usr/bin/env python3
"""
🔧 Fix all wrong imports in session.py
"""

from pathlib import Path

def fix_session_imports():
    print("🔧 Fixing session.py imports...")
    
    session_path = Path("tinderbotz/session.py")
    if not session_path.exists():
        print("❌ session.py not found!")
        return False
    
    # Read the file
    content = session_path.read_text()
    
    print("🔍 Looking for incorrect imports...")
    
    # Fix all the wrong imports
    fixes = [
        ("from smart_dating_bot.addproxy import get_proxy_extension", "from tinderbotz.addproxy import get_proxy_extension"),
        ("from smart_dating_bot.helpers", "from tinderbotz.helpers"),
        ("smart_dating_bot.", "tinderbotz."),
        ("import smart_dating_bot", "import tinderbotz"),
    ]
    
    fixed_count = 0
    
    for wrong, correct in fixes:
        if wrong in content:
            print(f"🔧 Fixing: {wrong} → {correct}")
            content = content.replace(wrong, correct)
            fixed_count += 1
    
    if fixed_count > 0:
        # Create backup
        backup_path = Path("tinderbotz/session.py.backup2")
        if not backup_path.exists():
            session_path.rename(backup_path)
            print(f"✅ Created backup: {backup_path}")
        
        # Write fixed content
        with open(session_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Fixed {fixed_count} import issues in session.py")
    else:
        print("✅ No import issues found in session.py")
    
    # Also check other files
    print("\n🔍 Checking other files...")
    
    files_to_check = [
        "tinderbotz/__init__.py",
        "tinderbotz/helpers/constants_helper.py",
    ]
    
    for file_path in files_to_check:
        path = Path(file_path)
        if path.exists():
            content = path.read_text()
            if "smart_dating_bot" in content:
                print(f"🔧 Fixing imports in {file_path}")
                content = content.replace("smart_dating_bot", "tinderbotz")
                with open(path, 'w') as f:
                    f.write(content)
                print(f"✅ Fixed {file_path}")
    
    print("\n🎉 All import fixes applied!")
    print("🚀 Try running: python start_bot.py")
    
    return True

if __name__ == "__main__":
    fix_session_imports()