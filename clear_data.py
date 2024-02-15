import os
import shutil

history = r"C:\Users\Tushar\AppData\Local\Google\Chrome\User Data\Default\History"
visited_links = r"C:\Users\Tushar\AppData\Local\Google\Chrome\User Data\Default\Visited Links"
cache = r"C:\Users\Tushar\AppData\Local\Google\Chrome\User Data\Default\Cache"

def clearChromeData():
    if os.path.exists(history):
        os.remove(history)

    if os.path.exists(visited_links):
        os.remove(visited_links)

    if os.path.exists(cache):
        shutil.rmtree(cache)

if __name__ == "__main__":
    clearChromeData()