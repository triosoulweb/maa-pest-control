import os

def get_footer_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_marker = '<footer'
    end_marker = '</footer>'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Include end marker
        return content[start_idx:end_idx + len(end_marker)]
    return None

source_file = "index.html"
footer_content = get_footer_content(source_file)

if not footer_content:
    print(f"Error: Could not find footer in {source_file}")
    exit(1)

print(f"Extracted footer from {source_file} ({len(footer_content)} chars)")

import glob
files = glob.glob("*.html")

for file in files:
    if file == source_file:
        continue
        
    print(f"Updating footer in {file}...")
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_marker = '<footer'
    end_marker = '</footer>'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + footer_content + content[end_idx + len(end_marker):]
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  > Success")
    else:
        print(f"  > Footer not found in {file}")
