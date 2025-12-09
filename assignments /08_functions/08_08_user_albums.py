# I will make user albums 
def make_album(artist, title, tracks=None):
    """Return a dictionary representing a music album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album['tracks'] = tracks
    return album
# I will add my user albums
user_albums = {}
polling_active = True
while polling_active:
    artist = input("Enter the artist's name: ")
    title = input("Enter the album title: ")
    tracks_input = input("Enter the number of tracks (or press Enter to skip): ")
    tracks = int(tracks_input) if tracks_input.isdigit() else None
    album = make_album(artist, title, tracks)
    user_albums[f"{artist} - {title}"] = album
    repeat = input("Would you like to add another album? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
print("\n--- User Album Collection ---")
for album_key, album_info in user_albums.items():
    print(f"{album_key}: {album_info}")