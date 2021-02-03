from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #create a new node
    new_song = Song(title)

    new_song.set_next_song(self.__first_song)

    #set new node to next pointer to point at the new node
    new_song.next = self.__first_song

    #set head pointer to point at the new node
    self.__first_song = new_song


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    search_song = self.__first_song
    #start at position 0
    index = 0

    #while the song that is being searched 
    while search_song != None:
      # if the song that is being searched matches the same one in the list
      if search_song.get_title() == title:
        # return the position of the song
        return index

      # if the song that is being searched doesnt match the one in that index go through the if statement
      if search_song.get_title() != title:
        # adds one to the index
        index += 1
        #then go to the next song
        search_song = search_song.get_next_song()
        index = -1
        return index


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    previous_song = None
    search_song = self.__first_song

    



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    length = 0
    # the current_song is the first song
    current_song = self.__first_song

  # while the song is not equal to none keep going to the loop until the loop is none
    while current_song != None:
      length += 1
      current_song = current_song.get_next_song()
      return length


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.__first_song
    index = 1
    # if the current_song is not None proceed to the loop
    while current_song != None:
      print(f"{str(index)}. {current_song}")
      current_song = current_song.get_next_song()
      index += 1

  