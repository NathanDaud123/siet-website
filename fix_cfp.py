import os
import re

siet_dir = r'e:\I2O\03. Website Subdomain\SIET'
icomit_dir = r'e:\I2O\03. Website Subdomain\ICOMIT'

# 1. Read ICOMIT's call-for-papers.html
with open(os.path.join(icomit_dir, 'call-for-papers.html'), 'r', encoding='utf-8') as f:
    icomit_content = f.read()

# Extract all Tracks from ICOMIT (until <hr>)
icomit_match = re.search(r'(<h3>General Tracks</h3>.*?)\n<hr>', icomit_content, re.DOTALL)
if not icomit_match:
    print("Could not find ICOMIT tracks.")
    exit(1)
tracks_content = icomit_match.group(1)

# 2. Read SIET's call-for-papers.html
siet_filepath = os.path.join(siet_dir, 'call-for-papers.html')
with open(siet_filepath, 'r', encoding='utf-8') as f:
    siet_content = f.read()

# Replace SIET's current faulty block (which has only Track 1) with all Tracks
siet_match = re.search(r'(<h3>General Tracks</h3>.*?)\n                            \n                                                            <div class="extra-data-content"', siet_content, re.DOTALL)
if not siet_match:
    print("Could not find SIET tracks to replace.")
    exit(1)

# Do the replacement
new_siet_content = siet_content.replace(siet_match.group(1), tracks_content)

with open(siet_filepath, 'w', encoding='utf-8') as f:
    f.write(new_siet_content)

print("Finished fixing Call for Papers content with all 3 tracks.")
