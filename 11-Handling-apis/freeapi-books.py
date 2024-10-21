import requests
import random
def fetch_random_book():
    url="https://api.freeapi.app/api/v1/public/books"
    response=requests.get(url)
    data=response.json()
    if data["statusCode"]==200 and "data" in data:
        book=data["data"]["data"]
        ind=round(random.random()*10)
        title=book[ind]["volumeInfo"]["title"]
        author=book[ind]["volumeInfo"]["authors"]
        return title,author
    else:
        raise Exception("Invalid request")

def main():
    try:
      title,author=  fetch_random_book()
      print(f"Title: {title} \n Author: {author}")
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    main()