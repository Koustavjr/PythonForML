import json 

def load_videos():
    try:
        with open('youtube.txt','r') as file:
            json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index} Video:{video["name"]} duration:{video["duration"]}")
    print("*"*70)
    print("\n")

def add_new_video(videos):
    name=input("Enter video name ")
    duration=input("Enter video duration ")
    videos.append({"name":name,"duration":duration})
    save_data_helper(videos)    
    

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter video number you want to update "))
    if 1<=index<=len(videos):
        name=input("Enter video name ")
        duration=input("Enter video duration ")
        videos[index-1]={"name":name,"duration":duration}
        save_data_helper(videos)
    else:
        print("Enter valid video number \n")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter video number you want to update "))
    if 1<=index<=len(videos):
       del videos[index-1]
       save_data_helper(videos)
    else:
        print("Enter valid index \n") 

def main():
    videos=load_videos()
    while True:
        print("\n")
        print("Enter 1 for List all Videos")
        print("Enter 2 to add new videos")
        print("Enter 3 to update video")
        print("Enter 4 to delete video")
        print("Enter 5 to exit")
        choice= input("\n Enter your choice ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("\n Enter Correct Choice")
                


if __name__=="__main__":
    main()