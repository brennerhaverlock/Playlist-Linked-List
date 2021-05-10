from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    print("=" * 90)

    add_song = Song(title)
    add_song.next = self.__first_song
    self.__first_song = add_song

    print("new song added to playlist")

    print("=" * 90 )



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):

    song_num = 0
    current_song = self.__first_song

    while current_song.get_title() != title:
      song_num += 1
      current_song = current_song.get_next_song()

      if current_song == None:
        return -1

    if current_song.get_title() == title:
      return song_num


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.__first_song

    if current_song and current_song.get_title() == title:
      self.__first_song = current_song.get_next_song()

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    print("=" * 90)

    num_songs = 0
    current_song = self.__first_song

    while current_song != None:
      num_songs += 1 
      current_song = current_song.next
    return num_songs

  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):

    lst = 0
    song_file = self.__first_song
    while song_file != None:
      print(f"# {lst}. {song_file} {lst}")
      song_file = song_file.get_next_song()
      lst += 1


  