import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

def play_music(folder, songname):
    file_path = os.path.join(folder, songname)
    
    if not os.path.isfile(file_path):
        print(f"The file '{songname}' does not exist.")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"Playing: {songname}")
    print("Commands: 'p' to pause, 'r' to resume, 's' to stop")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == 'p':
            pygame.mixer.music.pause()
            print("Music paused.")
        elif command == 'r':
            pygame.mixer.music.unpause()
            print("Music resumed.")
        elif command == 's':
            pygame.mixer.music.stop()
            print("Music stopped.")
            break
        else:
            print("Invalid command. Please enter 'p', 'r', or 's'.")

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing the mixer: {e}")
        return
    
    folder = "music"    

    if not os.path.isdir(folder):
        print(f"The folder '{folder}' does not exist.")
        return
    mp3_files = [f for f in os.listdir(folder) if f.endswith('.mp3')]
    if not mp3_files:
        print(f"No mp3 files found in the folder '{folder}'.")
        return
    
    while True:
        print("**** Music Player ****")
        print("My song list:")

        for index, file in enumerate(mp3_files, start=1):
            print(f"{index}. {file}")
        
        choice_input = input("Enter the number of the song to play (or 'q' to quit): ")
        if choice_input.lower() == 'q':
            print("Exiting the music player.")
            break
        if not choice_input.isdigit() or not (1 <= int(choice_input) <= len(mp3_files)):
            print("Invalid choice. Please try again.")
            continue
        choice = int(choice_input) - 1
        if 0<= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
    
if __name__ == "__main__":
    main()  