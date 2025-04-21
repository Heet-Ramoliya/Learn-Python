import sqlite3

def connect_db() -> sqlite3.Connection:
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('youtube_videos.db')

def create_table(conn: sqlite3.Connection) -> None:
    """Create the videos table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()

def list_videos(conn: sqlite3.Connection) -> None:
    """List all videos in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No records found.")
    else:
        print("\n" + "*" * 70)
        print(f"{'ID':<5} {'Name':<30} {'Duration':<10}")
        print("-" * 70)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<30} {row[2]:<10}")
        print("*" * 70)

def add_video(conn: sqlite3.Connection, name: str, time: str) -> None:
    """Add a new video to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
        conn.commit()
        print("Video added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding video: {e}")

def update_video(conn: sqlite3.Connection, video_id: int, name: str, time: str) -> None:
    """Update an existing video's details."""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Video updated successfully.")
        else:
            print("No video found with the given ID.")
    except sqlite3.Error as e:
        print(f"Error updating video: {e}")

def delete_video(conn: sqlite3.Connection, video_id: int) -> None:
    """Delete a video from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Video deleted successfully.")
        else:
            print("No video found with the given ID.")
    except sqlite3.Error as e:
        print(f"Error deleting video: {e}")

def main() -> None:
    """Main function to run the YouTube Manager application."""
    conn = connect_db()
    create_table(conn)

    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos(conn)
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(conn, name, time)
        elif choice == "3":
            try:
                video_id = int(input("Enter the video ID to update: "))
                name = input("Enter the new video name: ")
                time = input("Enter the new video duration: ")
                update_video(conn, video_id, name, time)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "4":
            try:
                video_id = int(input("Enter the video ID to delete: "))
                delete_video(conn, video_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()