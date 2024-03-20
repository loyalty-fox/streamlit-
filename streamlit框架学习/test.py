import requests

url = "https://img2024.cnblogs.com/blog/1809841/202403/1809841-20240313132347219-13618990.jpg"
response = requests.get(url)

if response.status_code == 200:
    # If the request was successful, you can access the content
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully")
else:
    print("Failed to download image. Status code:", response.status_code)


