# class definition
class Song:
   def __init__(self,artist,track,album,year):
      self.artist = artist
      self.track = track
      self.album = album
      self.year = year
   def __str__(self):
      return f'Performer : {self.artist}\nTitle : {self.track}\nAlbum : {self.album}\nYear : {self.year}'
    

# object creation
song1 = Song('Taylor Swift', 'The Prophecy', "TTPD", 2024)
song2 = Song("The Score", "Revolution", "Atlas", 2017)

## object usage
print(song1)
print(song2)