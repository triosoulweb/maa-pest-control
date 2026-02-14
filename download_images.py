import os
import urllib.request

# Added .jpg to dimensions to force JPEG format
images = {
    "hero-bg.jpg": "https://placehold.co/1920x1080.jpg/064e3b/white?text=Hero+Background",
    "technician.jpg": "https://placehold.co/800x600.jpg/10b981/white?text=Technician",
    "service-termite.jpg": "https://placehold.co/800x600.jpg/f59e0b/white?text=Termite+Control",
    "service-cockroach.jpg": "https://placehold.co/800x600.jpg/ef4444/white?text=Cockroach+Control",
    "service-bedbug.jpg": "https://placehold.co/800x600.jpg/b91c1c/white?text=Bed+Bug+Treatment",
    "service-rodent.jpg": "https://placehold.co/800x600.jpg/78350f/white?text=Rodent+Control",
    "service-general.jpg": "https://placehold.co/800x600.jpg/374151/white?text=General+Pest+Control",
    "service-mosquito.jpg": "https://placehold.co/800x600.jpg/0f766e/white?text=Mosquito+Fogging",
    "service-fly.jpg": "https://placehold.co/800x600.jpg/1e3a8a/white?text=Fly+Control",
    "service-ant.jpg": "https://placehold.co/800x600.jpg/b91c1c/white?text=Ant+Control",
    "service-lizard.jpg": "https://placehold.co/800x600.jpg/059669/white?text=Lizard+Control",
    "service-snake.jpg": "https://placehold.co/800x600.jpg/dc2626/white?text=Snake+Rescue",
    "about-team.jpg": "https://placehold.co/800x600.jpg/15803d/white?text=Our+Team",
}

if not os.path.exists("assets"):
    os.makedirs("assets")

# Force download even if exists to fix potential format issues
for name, url in images.items():
    path = os.path.join("assets", name)
    try:
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, path)
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
