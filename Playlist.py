from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #create a new node
    new_song = Song(title)

    #sets the next song to the head of the linked list
    new_song.set_next_song(self.__first_song)

    #set new node to next pointer to point at the new node
    self.__first_song = new_song


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.


  def find_song(self, title):
    current_song = self.__first_song
    #start at position 0
    index = 0

    #while the song that is being searched and doesnt equal the title keep going to the loop
    while current_song.get_title() != title:
      # if the song that is being searched matches the same one in the list
      index += 1

      # changes the current song to the next song then repeats the loop
      current_song = current_song.get_next_song()

      # if the song that is being searched doesnt match the one in that index go through the if statement
      if current_song.get_title() == None:
        # return -1
        return -1

      #after the while loop can no longer loop it goes outside and returns the index position
    if current_song.get_title == title:
        #this will run of the title matches
      return index


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    #the last song as well as the current song have the same song
    last_song = self.__first_song #a
    current_song = self.__first_song #a

  # we get the title of the current song if it matches title
    if current_song.get_title() == title: 

      # sets the head of the first song to the next song making the old one link to nothing
      self.__first_song = self.__first_song.get_next_song()

    # while the current song(a) does not equal the title(being searched)
    while current_song.get_title() != title:
      # change the last song to the current song
      last_song = current_song
      # and make the current song the next song
      current_song = current_song.get_next_song()

      if current_song == None:
        return f"Song not in the list."

      # if the title of the current song matches the one being searched run the statement
      if current_song.get_title() == title:
        # make the next song the current song 
        next_song = current_song.get_next_song()
        # set the last song to the next song
        last_song.set_next_song(next_song)



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    # start by the length being 0
    length = 0
    # the current_song is the first song
    current_song = self.__first_song

  # while the song is not equal to none keep going to the loop until the loop is none
    while current_song != None:
      length += 1
      # changes the current song to the next song
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