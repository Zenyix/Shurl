import shurl

def newurl():
  print("Input url: ")
  inurl = str(input())
  output = shurl.addshurl(inurl)
  print(output)