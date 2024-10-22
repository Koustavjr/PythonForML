from pymongo import MongoClient
from bson import ObjectId

url ="mongodb+srv://youtubemanager:youtubemanager@cluster0.luc0r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url,tlsAllowInvalidCertificates=True)

db=client["ytmanager"]
videos_collections=db["videos"]
print(client)
def list_videos():
  for video in videos_collections.find():
      print(f"{video["_id"]} name: {video["name"]} duration: {video["duration"]}")

def add_video(name,time):
    videos_collections.insert_one({
        "name":name,
        "duration":time
    })

def update_video(vid_id,new_name,new_time):
    videos_collections.update_one({
        "_id":ObjectId(vid_id)
    },{"$set":{
        "name":new_name,
        "duration":new_time
    }})
    

def delete_video(vid_id):
    videos_collections.delete_one({
        "_id":ObjectId(vid_id)
    })
    
    


def main():
    while True:
        print("Welcome to yt manager")
        print("Enter 1 for list all videos")
        print("Enter 2 to add new video")
        print("Enter 3 to update video")
        print("Enter 4 for delete video")
        print("Enter 5 to exit")
        choice=input("Enter Choice: ")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter name ")
            time=input("Enter time ")
            add_video(name,time)
        elif choice=='3':
             vid_id=input("Enter id ")
             name=input("Enter name ")
             time=input("Enter time ")
             update_video(vid_id,name,time)
        elif choice=='4':
            vid_id=input("Enter video id ")
            delete_video(vid_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")


if __name__=="__main__":
    main()