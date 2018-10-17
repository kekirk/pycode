class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["happy1", "happy2", "happy3"])

happy_bday.sing_me_song()
