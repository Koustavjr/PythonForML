import sqlite3

conn=sqlite3.connect('youtube_manager.db')

cursor=conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               
               ''')

def list_all_videos():
    cursor.execute("SELECT * FROM Videos")
    for row in cursor.fetchall():
        print(row)
def add_new_video(name,time):
    cursor.execute('INSERT INTO Videos(name,time) VALUES (?,?)',(name,time))
    conn.commit()
def update_video(id,name,time):
    cursor.execute("UPDATE Videos SET name=?, time=? WHERE id=? ",(name,time,id))
    conn.commit()
def delete_video(id):
    cursor.execute("DELETE FROM Videos WHERE id=?",(id,))
    conn.commit()


def main():
    while True:
        print("Youtube Manager \n")
        print("Enter 1 for list all videos")
        print("Enter 2 for add new video")
        print("Enter 3 to update video")
        print("Enter 4 to delete video")
        print("Enter 5 to exit")
        choice=input("\n Enter Choice: ")
        
        if choice=='1':
            list_all_videos()
        elif choice=='2':
            name=input("Enter Name ")
            time=input("Enter duration ")
            add_new_video(name,time)
        elif choice=='3':
            id=input("Enter video id ")
            name=input("Enter Name ")
            time=input("Enter duration ")
            update_video(id,name,time)
        elif choice=='4':
            id=input("Enter video id ")
            delete_video(id)
        elif choice=='5':
            break
        else:
            print("Enter valid choice ")


if __name__ == '__main__':
    main()