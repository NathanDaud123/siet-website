import os
import re

siet_dir = r'e:\I2O\03. Website Subdomain\SIET'
icomit_dir = r'e:\I2O\03. Website Subdomain\ICOMIT'

# 1. Read ICOMIT's call-for-papers.html
with open(os.path.join(icomit_dir, 'call-for-papers.html'), 'r', encoding='utf-8') as f:
    icomit_content = f.read()

# Extract the Tracks from ICOMIT
icomit_match = re.search(r'(<h3>General Tracks</h3>.*?</ul>\n</div>)', icomit_content, re.DOTALL)
if not icomit_match:
    print("Could not find ICOMIT tracks.")
    exit(1)
tracks_content = icomit_match.group(1)

# 2. Read SIET's call-for-papers.html
siet_filepath = os.path.join(siet_dir, 'call-for-papers.html')
with open(siet_filepath, 'r', encoding='utf-8') as f:
    siet_content = f.read()

# Replace SIET's topics with ICOMIT's tracks
# SIET's topics start around <p style="text-align:justify"><strong>Theme:
# and end at </ul>\n\n</div>
siet_match = re.search(r'(<p style="text-align:justify"><strong>Theme:.*?</ul>\n\n</div>)', siet_content, re.DOTALL)
if not siet_match:
    print("Could not find SIET topics.")
    exit(1)

# Do the replacement
new_siet_content = siet_content.replace(siet_match.group(1), tracks_content)

with open(siet_filepath, 'w', encoding='utf-8') as f:
    f.write(new_siet_content)

print("Finished updating Call for Papers content.")
