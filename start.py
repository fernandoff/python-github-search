#!pip install PyGithub

import io
import os

from github import Github

user =""
password = ""
g = Github(user, password)

token = ""
#g = Github(token)
repositories = g.search_repositories(query='dxf')

#f = open("github.txt", "a")
fname = "github.txt"

if os.path.exists(fname):
  os.remove(fname)
else:
  print("The file does not exist")

for repo in repositories:

  # attempt to avoid limit rate
  # core_rate_limit = g.get_rate_limit().core
  # reset_timestamp = calendar.timegm(core_rate_limit.reset.timetuple())
  # sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 5  # add 5 seconds to be sure the rate limit has been reset
  # time.sleep(sleep_time)

  name = repo.full_name
  html_url = repo.html_url
  description = repo.description

  row = (name or "") + "|" + (html_url or "") + "|" + (description or "")

  print(name or "")

  with io.open(fname, "a", encoding="utf-8") as f:
    f.write(row + "\n")

f.close()