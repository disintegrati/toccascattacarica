import time
import facebook
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "./toupload/"
    patterns = ['*.jpg']
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod

    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            file = event.src_path
            print(file)
            if file.endswith(".jpg"):
               upload(file)

def upload(f):
	cfg = {
   	 "page_id"      : "128948843981105",
   	 "access_token" : "EAAZA2bZAAeZAt8BAPnXkMkQguqEcq2Idhh9ygSRZBZBFsE8rheMO88I1KrSYC540et5mTAKbs1oRsQQOkB9qB7ZBm1PVEJA6gdG3S2KOEddzErfNcbzptXAbuHIptqILl7rSwHk7ePl4GUlp7jRoZCbG1ZCoFZC2C0mEZD"   # Step 3
   	 }
	api = get_api(cfg)
#	msg = "WE ARE THE ROBOT!"
	api.put_photo(image=open(f, 'rb'), message="E ALLORA #MOOOOSECA")
	print(f)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

if __name__ == '__main__':
    w = Watcher()
    w.run()

