import requests
def save_html(content,filename):
    with open(filename,'w') as f:
        f.write(content)

base_url = "https://laptop.bg/desktop_video_cards-amd"

r = requests.get(base_url)

if r.ok:
    save_html(r.text, "AMDvideos.html")
else:print("Code error 404")