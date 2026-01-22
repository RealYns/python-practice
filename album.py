def make_album(artist_name, album_title, tracks_number=''):
    album = {
        'artist' : artist_name ,
        'title' : album_title ,
    }
    if tracks_number:
        album['tracks_number'] = tracks_number
    return album

while True:
    print("Press Q to quit.")
    artist = input("Enter an artist: ")
    if artist == "Q":
        break
    album_title = input("Enter an album of his: ")
    if album_title == "Q":
       break
    trk_num = input("Enter the number of tracks: ")
    if trk_num == "Q":
        break
    album = make_album(artist, album_title, trk_num)
    print(album)
