import os

# Service Links configuration
services_links = [
    ("Termite Control", "termite-control.html"),
    ("Cockroach Control", "cockroach-control.html"),
    ("Bed Bug Treatment", "bed-bug-treatment.html"),
    ("Rodent Control", "rodent-control.html"),
    ("Ant Control", "ant-control.html"),
    ("Fly Control", "fly-control.html"),
    ("Mosquito Control", "mosquito-control.html"),
    ("Lizard Control", "lizard-control.html"),
    ("Snake Control", "snake-control.html"),
]

def generate_desktop_links(current_file):
    html = ""
    for name, link in services_links:
        # Default active state for desktop: hover effects
        # Active state: remove hover, add active colors
        # In the original, the active link had bg-light text-primary font-bold
        # The inactive links had hover:bg-light hover:text-primary
        
        if link == current_file:
             active_class = "bg-light text-primary font-bold"
        else:
             active_class = "hover:bg-light hover:text-primary"
        
        html += f'                        <a href="{link}" class="block px-4 py-2 {active_class}">{name}</a>\n'
    return html

def generate_mobile_links(current_file):
    html = '                <span class="text-xs font-semibold text-gray-400 uppercase">Services</span>\n'
    for name, link in services_links:
        if link == current_file:
            active_class = "text-primary font-bold"
        else:
            active_class = "text-gray-600"
        
        html += f'                <a href="{link}" class="block {active_class}">{name}</a>\n'
    return html

def process_file(filepath):
    filename = os.path.basename(filepath)
    # print(f"Processing {filename}...")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update Desktop Menu
    desktop_start_marker = 'class="absolute top-full left-0 w-56 bg-white shadow-lg rounded-xl py-2 hidden group-hover:block border border-gray-100">'
    desktop_end_marker = '</div>'
    
    # We need to find the START of the div, which is after the marker.
    # The marker is the opening tag properties.
    # But wait, content.find returns the start of the string.
    # So we want to replace what's INSIDE the div.
    
    # Find the start of the opening tag
    tag_start = content.find(desktop_start_marker)
    
    if tag_start != -1:
        # The content starts after the opening tag >
        # The marker above is just the attributes. The tag is <div attributes>
        # Let's search for the marker, find the closing > of that tag.
        
        # Actually my marker includes the closing > if I copied it right?
        # In the file it is:
        # <div
        #     class="...">
        # so it spans multiple lines. My marker is single line. This will fail.
        
        # Let's try a regex or a more robust find.
        pass
    else:
        # Re-try with a simpler marker or just read the structure I saw in index.html
        # In index.html, it was split across lines.
        # 102:                     <div
        # 103:                         class="absolute top-full left-0 w-56 bg-white shadow-lg rounded-xl py-2 hidden group-hover:block border border-gray-100">
        pass

    # Alternative approach: Find "termite-control.html" and replace the whole block of links?
    # The links are surrounded by <div ...> and </div>.
    # Let's find the start of the services block by looking for "Services <i class" button?
    # No, let's look for the unique class string.
    
    unique_class = "absolute top-full left-0 w-56 bg-white shadow-lg rounded-xl py-2 hidden group-hover:block border border-gray-100"
    
    idx = content.find(unique_class)
    if idx != -1:
        # Found the class. Now find the opening <div before it?
        # properties are inside <div ... >
        # Find the first '>' after the class.
        content_start = content.find('>', idx) + 1
        
        # Find the matching closing div. 
        # Since we know the indentation, we can look for "                    </div>" (20 spaces + </div>)
        # or just the next </div>
        # But there are links inside.
        
        # Let's look for the next </div>
        content_end = content.find('</div>', content_start)
        
        if content_start != -1 and content_end != -1:
             new_links = "\n" + generate_desktop_links(filename) + "                    "
             content = content[:content_start] + new_links + content[content_end:]
             print(f"Updated Desktop Menu in {filename}")
        else:
             print(f"Could not find content bounds for desktop menu in {filename}")
    else:
        print(f"Could not find desktop menu class in {filename}")

    # 2. Update Mobile Menu
    # Marker: <span class="text-xs font-semibold text-gray-400 uppercase">Services</span>
    # The container is <div class="border-l-2 border-gray-100 pl-4 space-y-2">
    
    mobile_class = "border-l-2 border-gray-100 pl-4 space-y-2"
    m_idx = content.find(mobile_class)
    
    if m_idx != -1:
        m_content_start = content.find('>', m_idx) + 1
        m_content_end = content.find('</div>', m_content_start)
        
        if m_content_start != -1 and m_content_end != -1:
             new_mobile_links = "\n" + generate_mobile_links(filename) + "            "
             content = content[:m_content_start] + new_mobile_links + content[m_content_end:]
             print(f"Updated Mobile Menu in {filename}")
        else:
             print(f"Could not find content bounds for mobile menu in {filename}")
    else:
        print(f"Could not find mobile menu class in {filename}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Get all HTML files
import glob
files = glob.glob("*.html")

for file in files:
    try:
        process_file(file)
    except Exception as e:
        print(f"Error processing {file}: {e}")
