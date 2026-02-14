import os

def insert_og_tags(content, filename):
    # Skip if already has OG tags
    if 'property="og:title"' in content:
        return content

    title_start = content.find('<title>')
    title_end = content.find('</title>')
    
    if title_start != -1 and title_end != -1:
        page_title = content[title_start+7:title_end]
        
        # Extract description
        desc_start = content.find('<meta name="description" content="')
        if desc_start != -1:
            desc_end = content.find('">', desc_start)
            page_desc = content[desc_start+34:desc_end]
        else:
            page_desc = "Professional pest control services in West Gudur Rural."

        og_tags = f"""
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{page_title}" />
    <meta property="og:description" content="{page_desc}" />
    <meta property="og:image" content="https://www.sgpestcontrol.com/assets/SGPS_Logo.jpeg" />
    <meta property="og:url" content="https://www.sgpestcontrol.com/{filename}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="SG Pest Control Service" />
    <meta property="og:locale" content="en_IN" />
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{page_title}" />
    <meta name="twitter:description" content="{page_desc}" />
    <meta name="twitter:image" content="https://www.sgpestcontrol.com/assets/SGPS_Logo.jpeg" />
"""
        # Insert after title
        return content[:title_end+8] + og_tags + content[title_end+8:]
    return content

def insert_breadcrumb_schema(content, filename):
    # Only for service pages basically, but Breadcrumb is good everywhere.
    # Let's add a generic Breadcrumb for Home > Current Page
    
    if "BreadcrumbList" in content:
        return content
        
    page_name = filename.replace(".html", "").replace("-", " ").title()
    if filename == "index.html":
        page_name = "Home"
        
    schema = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://www.sgpestcontrol.com/index.html"
      }},{{
        "@type": "ListItem",
        "position": 2,
        "name": "{page_name}",
        "item": "https://www.sgpestcontrol.com/{filename}"
      }}]
    }}
    </script>
"""
    # Insert before </head>
    head_end = content.find('</head>')
    if head_end != -1:
        return content[:head_end] + schema + content[head_end:]
    return content

def process_file(filepath):
    filename = os.path.basename(filepath)
    print(f"Enhancing SEO for {filename}...")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = insert_og_tags(content, filename)
    new_content = insert_breadcrumb_schema(new_content, filename)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

import glob
html_files = glob.glob("*.html")
for file in html_files:
    process_file(file)
