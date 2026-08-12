import os

directory = r'e:\I2O\03. Website Subdomain\SIET'
files_to_fix = ['publication.html', 'venue.html', 'contact.html']

for filename in files_to_fix:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace URLs and names
    content = content.replace('icomit', 'siet')
    content = content.replace('ICOMIT', 'SIET')
    content = content.replace('Icomit', 'Siet')
    content = content.replace('2027', '2026')
    content = content.replace('The 6th International Conference on Multidiciplinary Application of Information Technology', 'The 11th International Conference on Sustainable Information Engineering and Technology')
    content = content.replace('The 6th International Conference On Multidisciplinary Applications of Information Technology', 'The 11th International Conference on Sustainable Information Engineering and Technology')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished fixing text in copied files.")
