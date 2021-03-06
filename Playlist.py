from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    print("=" * 90)

    pop_song = Song(title)
    pop_song.set_next_song(self.__first_song)
    self.__first_song = pop_song

    print("new song added to playlist")

    print("=" * 90 )



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    print("=" * 90)

    pick_song = self.__first_song
    song_num = 0 

    while pick_song != None:
      if pick_song.get_title() == title:
        return song_num
      pick_song = pick_song.get_next_song()
      song_num += 1 

    print("=" * 90)

    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pick_song = self.__first_song

    if pick_song.get_title() == title:
      self.__first_song = pick_song.get_next_song()
      return

    while pick_song != None:
      print(pick_song)
      print(pick_song.get_next_song())
      return

    while pick_song != None:
      print(pick_song)
      print(pick_song.get_next_song())

      if pick_song.get_next_song() == None:
        break
      elif pick_song.get_next_song().get_title() == title:
        pick_song.set_next_song(pick_song.get_next_song().get_next_song())
        break



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    print("=" * 90)

    num_songs = 0
    current_song = self.__first_song

    while current_song != None:
      num_songs += 1 
      current_song = current_song.get_next_song()

    print("=" * 90)

    return num_songs


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    print("=" * 90)

    lst = 0
    song_file = self.__first_song
    while song_file != None:
      lst += 1
      print(f"# {lst}. {song_file}")
      song_file = song_file.get_next_song()

    print("=" * 90)

  