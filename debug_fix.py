#!/usr/bin/env python3
"""
🔧 Debug and Fix the Import Issue
Let's check what's wrong and fix it
"""

from pathlib import Path

def debug_and_fix():
    print("🔍 Debugging the import issue...")
    
    # Check if start_bot.py exists
    start_bot_path = Path("start_bot.py")
    if not start_bot_path.exists():
        print("❌ start_bot.py doesn't exist!")
        return
    
    print("✅ start_bot.py exists")
    
    # Read and check the content
    content = start_bot_path.read_text()
    
    print("\n🔍 Checking imports in start_bot.py...")
    
    # Find all import lines
    lines = content.split('\n')
    import_lines = [line for line in lines if 'import' in line and ('session' in line.lower() or 'smart_dating' in line.lower() or 'tinderbotz' in line.lower())]
    
    print("📋 Found these import lines:")
    for i, line in enumerate(import_lines):
        print(f"   {i+1}. {line.strip()}")
    
    # Check for the problematic import
    if 'smart_dating_bot' in content:
        print("\n❌ Found 'smart_dating_bot' references!")
        print("🔧 Fixing them...")
        
        # Fix all references
        fixed_content = content.replace('smart_dating_bot', 'tinderbotz')
        
        # Write the fixed content
        with open(start_bot_path, 'w') as f:
            f.write(fixed_content)
        
        print("✅ Fixed all 'smart_dating_bot' references to 'tinderbotz'")
    
    elif 'tinderbotz' in content:
        print("✅ Imports look correct (using 'tinderbotz')")
    else:
        print("❌ No Session import found!")
    
    # Double-check the fix
    print("\n🔍 Verifying the fix...")
    updated_content = start_bot_path.read_text()
    
    if 'from tinderbotz.session import Session' in updated_content:
        print("✅ Correct import found: 'from tinderbotz.session import Session'")
    elif 'smart_dating_bot' in updated_content:
        print("❌ Still has 'smart_dating_bot' references!")
    else:
        print("⚠️ Import line not found - let me add it")
        
        # Find where to insert the import
        lines = updated_content.split('\n')
        insert_index = -1
        
        for i, line in enumerate(lines):
            if 'def main():' in line:
                # Go back to find a good place to insert
                for j in range(i-1, -1, -1):
                    if lines[j].strip().startswith('from ') or lines[j].strip().startswith('import '):
                        insert_index = j + 1
                        break
                break
        
        if insert_index > 0:
            lines.insert(insert_index, '        from tinderbotz.session import Session')
            updated_content = '\n'.join(lines)
            
            with open(start_bot_path, 'w') as f:
                f.write(updated_content)
            
            print("✅ Added correct import line")
    
    # Also check if tinderbotz module exists
    tinderbotz_path = Path("tinderbotz")
    if tinderbotz_path.exists() and tinderbotz_path.is_dir():
        print("✅ tinderbotz module directory exists")
        
        session_file = tinderbotz_path / "session.py"
        if session_file.exists():
            print("✅ tinderbotz/session.py exists")
        else:
            print("❌ tinderbotz/session.py missing!")
            
        init_file = tinderbotz_path / "__init__.py"
        if init_file.exists():
            print("✅ tinderbotz/__init__.py exists")
        else:
            print("⚠️ tinderbotz/__init__.py missing (creating it)")
            with open(init_file, 'w') as f:
                f.write('# Tinderbotz module\n')
    else:
        print("❌ tinderbotz module directory doesn't exist!")
        return
    
    print("\n🎯 Summary:")
    print("✅ All fixes applied")
    print("🚀 Try running: python start_bot.py")

if __name__ == "__main__":
    debug_and_fix()