import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "128948843981105",  # Step 1
    "access_token" : "EAAZA2bZAAeZAt8BAPnXkMkQguqEcq2Idhh9ygSRZBZBFsE8rheMO88I1KrSYC540et5mTAKbs1oRsQQOkB9qB7ZBm1PVEJA6gdG3S2KOEddzErfNcbzptXAbuHIptqILl7rSwHk7ePl4GUlp7jRoZCbG1ZCoFZC2C0mEZD"   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  api.put_photo(image=open('img.jpg', 'rb'), message='Look at this cool photo!')
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()

