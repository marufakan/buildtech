import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

# Direct image URLs from Unsplash and Pexels
image_urls = {
    "hero-bg.jpg": "https://images.pexels.com/photos/157811/pexels-photo-157811.jpeg",
    "about.jpg": "https://images.pexels.com/photos/416405/pexels-photo-416405.jpeg",
    "project1.jpg": "https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg",
    "project2.jpg": "https://images.pexels.com/photos/236698/pexels-photo-236698.jpeg",
    "project3.jpg": "https://images.pexels.com/photos/271667/pexels-photo-271667.jpeg",
    # Yeni slider resimleri
    "slider1.jpg": "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg",
    "slider2.jpg": "https://images.pexels.com/photos/1838640/pexels-photo-1838640.jpeg",
    "slider3.jpg": "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg"
}

# Create images directory if it doesn't exist
os.makedirs("assets/images", exist_ok=True)

# Download images
for filename, url in image_urls.items():
    download_image(url, f"assets/images/{filename}")

print("Image download process completed!") 