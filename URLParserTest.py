import unittest
from URLParser import URLParser

class URLParserTest(unittest.TestCase):

  def test_parseURLs(self):
    parser = URLParser()
    hostnames = parser.parseURLs("urls.txt")

    self.assertEqual(len(hostnames), 5)
    self.assertEqual(hostnames["twitter.com"], 3)
    self.assertEqual(hostnames["abcnews.go.com"], 2)
    self.assertEqual(hostnames["google.co.uk"], 1)
    self.assertEqual(hostnames["newsfeed.time.com"], 1)
    self.assertEqual(hostnames["world.time.com"], 1)

  def test_sortHostnames(self):
    parser = URLParser()
    hostnames = {
      "ccc.com" : 2,
      "bbb.com": 3,
      "aaa.com": 2
    }

    sortedNames = parser.sortHostnames(hostnames)
    self.assertEquals(sortedNames[0], ('bbb.com', 3))
    self.assertEquals(sortedNames[1], ('aaa.com', 2))
    self.assertEquals(sortedNames[2], ('ccc.com', 2))


if __name__ == '__main__':
  unittest.main()