import os
import re

directory = r'e:\I2O\03. Website Subdomain\SIET'
filepath = os.path.join(directory, 'committees.html')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_committees_html = """<div id="committees">

	<div class="committee-section">
		<div class="member-group">
			<h2 class="committee-heading">Steering Committee</h2>
			<ul>
				<li><strong>Fitri Utaminingrum</strong>, Universitas Brawijaya</li>
				<li><strong>Arief Andy Soebroto</strong>, Universitas Brawijaya</li>
				<li><strong>Azlan Mohd Zain</strong>, Universiti Teknologi Malaysia</li>
				<li><strong>Wan Azani Bin Wan Mustafa</strong>, Universiti Malaysia Perlis</li>
				<li><strong>Hashem Salarzadeh Jenatabadi</strong>, Monash University Malaysia</li>
				<li><strong>Md Atiqur Rahman Ahad</strong>, University of East London</li>
				<li><strong>Hsing-Kuo Pao</strong>, National Taiwan University of Science and Technology</li>
				<li><strong>Jenq-Shiou Leu</strong>, National Taiwan University of Science and Technology</li>
				<li><strong>Masayoshi Aritsugi</strong>, Kumamoto University</li>
				<li><strong>Nobuo Funabiki</strong>, Okayama University</li>
				<li><strong>Mustafa Mat Deris</strong>, Universitas Muhammadiyah Malaysia</li>
				<li><strong>Suraya Hamid</strong>, Universiti Malaya, Malaysia</li>
			</ul>
		</div>
	</div>

	<div class="committee-section">
		<div class="member-group">
			<h2 class="committee-heading">General Chairs</h2>
			<ul>
				<li><strong>Diva Kurnianingtyas</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
				<li><strong>Lailil Muflikhah</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
			</ul>
		</div>

		<div class="member-group">
			<h2 class="committee-heading">Program Committee Chairs</h2>
			<ul>
				<li><strong>Haruna Chiroma</strong>, University of Hafr Al Batin, Saudi Arabia (freedonchi@yahoo.com; charuna@uhb.edu.sa; chiromaharun@fcetgombe.edu.ng)</li>
			</ul>
		</div>

		<div class="member-group">
			<h2 class="committee-heading">International Liasion</h2>
			<ul>
				<li><strong>Azlan Mohd Zain</strong>, Universiti Teknologi Malaysia</li>
				<li><strong>Azah ANir Norman</strong>, Universiti Malaya, Malaysia</li>
				<li><strong>Tutut Herawan</strong>, Universiti Malaya, Malaysia</li>
			</ul>
		</div>

		<div class="member-group">
			<h2 class="committee-heading">Organizing Committee</h2>
			<ul>
				<li><strong>Anis Rahmawati Amna</strong>, Universitas Brawijaya</li>
				<li><strong>Agus Wahyu Widodo</strong>, Universitas Brawijaya</li>
				<li><strong>Muh. Arif Rahman</strong>, Universitas Brawijaya</li>
				<li><strong>Bayu Rahayudi</strong>, Universitas Brawijaya</li>
				<li><strong>Dian Eka Ratnawati</strong>, Universitas Brawijaya</li>
				<li><strong>Ismiarta Aknuranda</strong>, Universitas Brawijaya</li>
				<li><strong>Arief Andy Soebroto</strong>, Universitas Brawijaya</li>
			</ul>
		</div>
	</div>

	<div class="info-notice">We have invited many prominent researchers in the related fields to be our conference reviewer. This page will be updated with new names.</div>

</div>"""

# Replace the existing <div id="committees">...</div>
# We can use re.sub with DOTALL
new_content = re.sub(r'<div id="committees">.*?</div>\s*<div class="extra-data-content"', new_committees_html + '\n                            \n                                                            <div class="extra-data-content"', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Finished updating Committees content.")
