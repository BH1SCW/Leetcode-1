import urllib.request
import json


# Complete the function below.
# https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic]

def getTopicCount(topic):
    contents = json.load(urllib.request.urlopen(
        "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={}".format(topic)))
    # text = json.load(contents)["text"]
    text = contents["parse"]["text"]["*"]
    # print(text)
    return text.count(topic)


if __name__ == '__main__':
    topic = "pizza"
    getTopicCount(topic)
