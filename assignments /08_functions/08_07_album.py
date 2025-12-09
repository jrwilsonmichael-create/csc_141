# I will make an album
def make_album(artist, title, tracks=None):
    """Return a dictionary representing a music album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album['tracks'] = tracks
    return album
# Example usage
album1 = make_album('Tyler The Creator', 'CHROMAKOPIA', tracks=16)
print(album1)
album2 = make_album('Travis Scott', 'Astroworld', tracks=12)
print(album2)
album3 = make_album('Cochise', 'WHY ALWAYS ME', tracks=18)
print(album3)