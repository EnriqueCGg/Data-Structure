class SongNode:
    """Represents a single song in the playlist."""
    def __init__(self, title):
        self.title = title
        self.next = None 
        self.prev = None  

class Playlist:
    """Manages the circular playlist of songs."""
    def __init__(self):
        self.head = None
        self.current_song = None

    def add_song(self, title):
        """Adds a new song to the end of the playlist."""
        new_song = SongNode(title)
        
        if not self.head:
            self.head = new_song
            new_song.next = self.head
            new_song.prev = self.head
            self.current_song = self.head
        else:
            tail = self.head.prev

            tail.next = new_song
            new_song.prev = tail
            new_song.next = self.head
            self.head.prev = new_song
        
        print(f"Added '{title}' to the playlist.")

    def play_next(self):
        """Moves to and plays the next song."""
        if not self.current_song:
            print("The playlist is empty!")
            return
        
        self.current_song = self.current_song.next
        print(f"Now playing: {self.current_song.title}")

    def play_previous(self):
        """Moves to and plays the previous song."""
        if not self.current_song:
            print("The playlist is empty!")
            return
            
        self.current_song = self.current_song.prev
        print(f"Now playing: {self.current_song.title}")

    def show_current(self):
        """Shows the currently selected song."""
        if not self.current_song:
            print("The playlist is empty!")
            return
        print(f"Current song: {self.current_song.title}")
        
#Test
my_playlist = Playlist()

my_playlist.add_song("Perfect Peace -   Sondae")
my_playlist.add_song("Day or Night - Jervis Campbell")
my_playlist.add_song("Air I breath - Sondae")
print("-" * 30)
my_playlist.show_current()
print("-" * 30)
my_playlist.play_next() 
my_playlist.play_next()
my_playlist.play_next()
print("-" * 30)
my_playlist.play_previous() 
my_playlist.play_previous() 