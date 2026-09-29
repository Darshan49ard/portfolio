from pathlib import Path
p = Path(r"c:\Users\darsh\OneDrive\Desktop\darshan-portfolio\iot session\iot task 5f\iot task 5f.html")
text = p.read_text(encoding="utf-8")
marker = '<p class="c2"><span class="c0">Evidence to add:</span></p>'
if marker not in text:
    raise SystemExit("marker not found")
img1 = '<figure><img src="./images/image1.png" alt="Firebase project overview" loading="lazy"><figcaption>Firebase project overview</figcaption></figure>'
img2 = '<figure><img src="./images/image2.png" alt="Realtime Database with the database address" loading="lazy"><figcaption>Realtime Database</figcaption></figure>'
img3 = '<figure><img src="./images/image3.png" alt="Authentication and user accounts" loading="lazy"><figcaption>Authentication and users</figcaption></figure>'
video = '<h3>Demonstration Video</h3><video class="demonstration-video" controls preload="auto" playsinline muted><source src="./iot%20task%205.mp4" type="video/mp4">Your browser does not support the video tag.</video><p><a href="./iot%20task%205.mp4" target="_blank" rel="noopener">Open the video directly</a></p>'
insert = '<div class="evidence-gallery" aria-label="Task 5 evidence screenshots">' + img1 + img2 + img3 + '</div>' + video
text = text.replace(marker, marker + insert, 1)
p.write_text(text, encoding="utf-8")
print("updated")
