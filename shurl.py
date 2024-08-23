shurl = {}

def addshurl(inurl):
  temp = len(shurl) + 1
  newurl = "https://shurl/"+str(temp)
  shurl[newurl] = inurl
  return newurl

def access():
  print("Retrieve url: ")
  key = str(input())
  return shurl.get(key)