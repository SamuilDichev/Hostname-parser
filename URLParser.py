import urllib.parse as urlparse

class URLParser(object):

  def parseURLs(self, file):
    hostnames = {}
    with open(file) as f:
      for line in f:
        hostname = urlparse.urlsplit(line).netloc.replace("www.", "")
        if hostname in hostnames.keys():
          hostnames[hostname] += 1
        else:
          hostnames[hostname] = 1

    return hostnames

  def sortHostnames(self, names):
    return sorted(names.items(), key=lambda kv: (-kv[1], kv[0]))