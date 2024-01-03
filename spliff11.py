import os 
import xml.etree.ElementTree as ET 
import xml.dom.minidom

def choose_songs(): 
    home_directory = os.path.expanduser("~") 
    print("Select the songs you want to add to the playlist:\n") 
    count = 1 
    songs = [] 
    for root, dirs, files in os.walk(home_directory): 
        for file in files: 
            if file.endswith(".mp3"): 
                print(f"{count}: {file}") 
                songs.append(os.path.join(root, file)) 
                count += 1

    selected_songs = []
    while True:
        try:
            song_index = int(input("Enter the song number you want to add (0 to exit): "))
            if song_index == 0:
                break
            elif song_index < 1 or song_index > len(songs):
                print("Invalid song number. Please try again.")
                continue
            selected_songs.append(songs[song_index-1])
        except ValueError:
            print("Invalid input. Please enter a number.")

    return selected_songs

def update_playlist(root_element):
    track_list = root_element.find("trackList") 
    if track_list is None: 
        track_list = ET.Element("trackList") 
        root_element.append(track_list)

    selected_songs = choose_songs()

    for i, selected_song in enumerate(selected_songs):
        track = ET.Element("track")

        location = ET.Element("location")
        location.text = selected_song
        track.append(location)

        identifier = ET.Element("identifier")
        identifier.text = input(f"Enter the identifier of track {i+1} (optional): ")
        track.append(identifier)

        title = ET.Element("title")
        title.text = input(f"Enter the title of track {i+1} (optional): ")
        track.append(title)

        creator = ET.Element("creator")
        creator.text = input(f"Enter the creator of track {i+1} (optional): ")
        track.append(creator)

        album = ET.Element("album")
        album.text = input(f"Enter the album of track {i+1} (optional): ")
        track.append(album)

        annotation = ET.Element("annotation")
        annotation.text = input(f"Enter the annotation of track {i+1} (optional): ")
        track.append(annotation)

        info = ET.Element("info")
        info.text = input(f"Enter the info of track {i+1} (optional): ")
        track.append(info)

        image = ET.Element("image")
        image.text = input(f"Enter the image of track {i+1} (optional): ")
        track.append(image)

        album_artist = ET.Element("albumArtist")
        album_artist.text = input(f"Enter the album artist of track {i+1} (optional): ")
        track.append(album_artist)

        track_num = ET.Element("trackNum")
        track_num.text = input(f"Enter the track number of track {i+1} (optional): ")
        track.append(track_num)

        duration = ET.Element("duration")
        duration.text = input(f"Enter the duration of track {i+1} (optional): ")
        track.append(duration)

        link_flag = input(f"Enter the link of track {i+1} (true/false, optional): ")
        if link_flag.lower() == "true":
            link = ET.Element("link")
            link.text = "true"
            track.append(link)
        
        rel_flag = input(f"Enter the rel link {i+1} (true/false, optional): ")
        if rel_flag.lower() == "true":
            rel = ET.Element("rel")
            rel.text = "true"
            track.append(rel)
        
        meta_flag = input(f"Enter meta {i+1} (true/false, optional): ")
        if meta_flag.lower() == "true":
            meta = ET.Element("meta")
            meta.text = "true"
            track.append(meta)
        
        extensions_flag = input(f"Enter XML extensions {i+1} (true/false, optional): ")
        if extensions_flag.lower() == "true":
            extensions = ET.Element("extensions")
            extensions.text = "true"
            track.append(extensions)
            
        track_list.append(track)

    return root_element

def create_playlist(): 
    playlist = ET.Element("playlist")
    
    title = ET.Element("title")
    title.text = input("Enter the playlist title: ")
    playlist.append(title)
    
    creator = ET.Element("creator")
    creator.text = input("Enter the playlist creator: ")
    playlist.append(creator)
    
    annotation = ET.Element("annotation")
    annotation.text = input("Enter the playlist annotation: ")
    playlist.append(annotation)
    
    info = ET.Element("info")
    info.text = input("Enter the playlist info: ")
    playlist.append(info)
    
    location = ET.Element("location")
    location.text = input("Enter the playlist location: ")
    playlist.append(location)
    
    identifier = ET.Element("identifier")
    identifier.text = input("Enter the playlist identifier: ")
    playlist.append(identifier)
    
    image = ET.Element("image")
    image.text = input("Enter the playlist image: ")
    playlist.append(image)
    
    attribution = ET.Element("attribution")
    attribution.text = input("Enter the playlist attribution: ")
    playlist.append(attribution)
    
    date = ET.Element("date")
    date.text = input("Enter the playlist date (YYYY-MM-DD): ")
    playlist.append(date)
    
    license = ET.Element("license")
    license.text = input("Enter the playlist license: ")
    playlist.append(license)
    
    link_flag = input("Enter the playlist link (true/false): ")
    if link_flag.lower() == "true":
        link = ET.Element("link")
        link.text = "true"
        playlist.append(link)
        
    attribution_flag = input("Enter the attribution (true/false): ")
    if attribution_flag.lower() == "true":
        attribution = ET.Element("attribution")
        attribution.text = "true"
        playlist.append(attribution)
    
    rel_flag = input("Enter the playlist rel (true/false): ")
    if rel_flag.lower() == "true":
        rel = ET.Element("rel")
        rel.text = "true"
        playlist.append(rel)
    
    playlist = update_playlist(playlist)
    
    playlist.extend([title, creator, annotation, info, location, identifier, image, attribution, date, license])
    
    playlist.set("xmlns", "http://xspf.org/ns/0/")
    playlist.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    playlist.set("xsi:schemaLocation", "http://xspf.org/ns/0/ http://www.xspf.org/xspf-v1.xsd")
    playlist.set("version", "1")
    
    tree = ET.ElementTree(playlist)
    try:
        file_name = input("Enter the playlist file name: ")
        xml_string = ET.tostring(playlist, encoding="utf-8")
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml(indent="  ")
        with open(f"{file_name}.xspf", "w") as file:
            file.write(pretty_xml)
        print("Playlist created successfully.")
    except Exception as e:
        print(f"Error creating playlist: {str(e)}")

if __name__ == "__main__":
    create_playlist()
