import argparse
from URLParser import URLParser

parser = argparse.ArgumentParser(description="Parse hostnames from a text file.")
parser.add_argument('file', help="A file containing hostnames")
args = parser.parse_args()

parser = URLParser()
hostnames = parser.parseURLs(args.file)
for hostname, count in parser.sortHostnames(hostnames):
  print(count, hostname)