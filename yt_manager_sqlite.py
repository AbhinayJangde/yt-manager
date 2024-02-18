
import sqlite3

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name,time))
    con.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    con.commit()

def main():
    print("#" * 40)
    print("#" + " " * 38 + "#")
    print("# Youtube Manager | Choose an option   #")
    print("#" + " " * 38 + "#")
    print("#" * 40)
    print("\n")
    while True:
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("\nENTER YOUR CHOICE~# ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video id: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name,time)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
    
    # closing the database connection
    con.close()
            

if __name__ == "__main__":
    main()