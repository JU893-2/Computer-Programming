# list with playlists
playlist = ["Filter", "All My Time", "GOYD", "Magnetic"]

# asking user for input
new_song = input("Put in one more song: ")
# cleaning new_song
new_song = new_song.strip().title()
# using append to add to the variable
playlist.append(new_song)

# using len to show the amount
print("Number of songs:", len(playlist))
# bonus song at index 0
playlist.insert(0, "Century")
# changed my mind by removing it from variable playlist
playlist.remove("GOYD")
# deleting another item
del playlist[2]

# alphabetical reversal switch
print("Order:", sorted(playlist))
playlist.sort()
playlist.reverse()

# checking certain songs
print("Photograph" in playlist)

for song in playlist:
    print(song.upper())
# showcasing tracklist i think
for i in range(len(playlist)):
    print(i + 1, playlist[i])





