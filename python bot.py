from pytube import YouTube
import os
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(output_path)
        return video_stream.default_filename
    except Exception as e:
        print("Une erreur est survenue lors du téléchargement de la vidéo :", str(e))
        return None

def extract_audio(video_filename, output_path):
    try:
        video_clip = VideoFileClip(video_filename)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(os.path.join(output_path, "audio.mp3"))
        video_clip.close()
        return "audio.mp3"
    except Exception as e:
        print("Erreur lors de l'extraction de l'audio :", str(e))
        return None

if __name__ == "__main__":
    youtube_url = input("Entrez l'URL de la vidéo YouTube : ").strip()

    # Définir le répertoire de sortie pour les fichiers importés
    
    output_directory = r'C:\Users\Kevin\Desktop\import'

    if "youtube.com" not in youtube_url:
        print("L'URL fournie n'est pas une URL YouTube valide.")
        exit()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    video_filename = download_youtube_video(youtube_url, output_directory)
    if video_filename:
        print("La vidéo a été téléchargée avec succès :", video_filename)
        convert = input("Voulez-vous extraire l'audio au format MP3 ? (oui/non) : ").strip().lower()
        if convert == "oui":
            audio_filename = extract_audio(os.path.join(output_directory, video_filename), output_directory)
            if audio_filename:
                print("L'audio a été extrait et sauvegardé en tant que fichier MP3 avec succès :", audio_filename)
            else:
                print("Une erreur est survenue lors de l'extraction de l'audio.")
    else:
        print("Impossible de télécharger la vidéo depuis l'URL fournie.")
