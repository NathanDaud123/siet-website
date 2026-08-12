import os
import re

directory = r'e:\I2O\03. Website Subdomain\SIET'
files_to_fix = ['publication.html', 'venue.html', 'contact.html']

# Get the CSS links from index.html
with open(os.path.join(directory, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the block of link tags from index.html
# It starts around <link href="https://siet.ub.ac.id/assets/skin/jtif/css/landing.min.css" and ends before <script
link_block_match = re.search(r'(<link href="https://siet.ub.ac.id/assets/skin/jtif/css/landing\.min\.css".*?zabuto_calendar\.min\.css" rel="stylesheet">)', index_content, re.DOTALL)
if not link_block_match:
    print("Could not find link block in index.html")
    exit(1)
correct_link_block = link_block_match.group(1)

# Now extract the JS scripts at the bottom
script_block_match = re.search(r'(<script src="https://siet.ub.ac.id/assets/ptiik/js/jquery-2\.2\.4\.min\.js"></script>.*?</script>)', index_content, re.DOTALL)
# Actually, the scripts at the bottom of index.html contain calendar scripts which might not be needed, but it's safe to include them.
# Let's just do the CSS for now, as that fixes the layout issue. The user showed a broken layout (missing CSS).

for filename in files_to_fix:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the link block in the target file
    target_link_match = re.search(r'(<link href="https://siet.ub.ac.id/assets/skin/jtif/css/landing\.min\.css".*?rel="stylesheet">)', content, re.DOTALL)
    if target_link_match:
        # We replace the entire block of CSS links with the correct one from SIET index.html
        # We need to make sure we don't accidentally match too much.
        # Let's replace everything from the first link to the last link before <style> or <script>
        target_link_block = re.search(r'(<link href="https://siet.ub.ac.id/assets/skin/jtif/css/landing\.min\.css".*?select2\.css" rel="stylesheet">)', content, re.DOTALL)
        if target_link_block:
             content = content.replace(target_link_block.group(1), correct_link_block)
        else:
             print(f"Could not find exact link block in {filename}")
             
    # Fix the JS scripts block just in case
    # The target files have <script src="https://siet.ub.ac.id/assets/ptiik/js/jquery-2.2.4.min.js"></script>
    # and end at <script src="https://siet.ub.ac.id/assets/select/select2.js"></script>
    target_js_block = re.search(r'(<script src="https://siet.ub.ac.id/assets/ptiik/js/jquery-2\.2\.4\.min\.js"></script>.*?select2\.js"></script>)', content, re.DOTALL)
    
    correct_js_block_match = re.search(r'(<script src="https://siet.ub.ac.id/assets/ptiik/js/jquery-2\.2\.4\.min\.js"></script>.*?zabuto_calendar\.min\.js"></script>)', index_content, re.DOTALL)
    
    if target_js_block and correct_js_block_match:
        content = content.replace(target_js_block.group(1), correct_js_block_match.group(1))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished fixing CSS/JS links in copied files.")
