import os
import re

directory = r'e:\I2O\03. Website Subdomain\SIET'

# Get the logo from index.html
with open(os.path.join(directory, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the block of logo from index.html
logo_block_match = re.search(r'(<div id="logo">.*?</div><!-- #logo end -->)', index_content, re.DOTALL)
if not logo_block_match:
    print("Could not find logo block in index.html")
    exit(1)
correct_logo_block = logo_block_match.group(1)

html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html']

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the logo block in the target file
    content = re.sub(r'<div id="logo">.*?</div><!-- #logo end -->', correct_logo_block, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished fixing logo in copied files.")
