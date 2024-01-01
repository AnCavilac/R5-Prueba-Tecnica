import json   
import pandas as pd

#Rutas de los archivos
archivo_json_input = 'insumos/taylor_swift_spotify.json'
archivo_csv_output = 'primer_entregable/dataset.csv'

#En modo lectura se abre el archivo, se extrae la información y se asigna a la variable una vez es interpretada
with open(archivo_json_input, 'r') as obtener_data:
    data = json.load(obtener_data)

#Se inicializa una lista vacía, esto para almacenar las filas del df
rows = []

#Función para cambiar nombres y evitar el acceso al mismo subdiccionario audio_features varias veces en el for
def obtener_detalles_pista(track):
    detalles_pista = track['audio_features']
    return {
        'audio_features.danceability': detalles_pista['danceability'],
        'audio_features.energy': detalles_pista['energy'],
        'audio_features.key': detalles_pista['key'],
        'audio_features.loudness': detalles_pista['loudness'],
        'audio_features.mode': detalles_pista['mode'],
        'audio_features.speechiness': detalles_pista['speechiness'],
        'audio_features.acousticness': detalles_pista['acousticness'],
        'audio_features.instrumentalness': detalles_pista['instrumentalness'],
        'audio_features.liveness': detalles_pista['liveness'],
        'audio_features.valence': detalles_pista['valence'],
        'audio_features.tempo': detalles_pista['tempo'],
        'audio_features.id': detalles_pista['id'],
        'audio_features.time_signature': detalles_pista['time_signature'],
    }

#Iteración encargada de obtener y construir los registros del álbum
for album in data['albums']:
    for track in album['tracks']:
        row = {
            # Información de la pista
            'disc_number': track['disc_number'],
            'duration_ms': track['duration_ms'],
            'explicit': track['explicit'],
            'track_number': track['track_number'],
            'track_popularity': track['track_popularity'],
            'track_id': track['track_id'],
            'track_name': track['track_name'],
            # Obtener los atributos del subdiccionario audio_features
            **obtener_detalles_pista(track),
            # Información del artista
            'artist_id': data['artist_id'],
            'artist_name': data['artist_name'],
            'artist_popularity': data['artist_popularity'],
            # Información del álbum
            'album_id': album['album_id'],
            'album_name': album['album_name'],
            'album_release_date': album['album_release_date'],
            'album_total_tracks': album['album_total_tracks'],
        }
        #Agregar la fila a la lista rows
        rows.append(row)

#Creación df para almacenar los registros obtenidos 
df = pd.DataFrame(rows)

#Creación csv con la información obtenida del archivo json
df.to_csv(archivo_csv_output,encoding='utf-8-sig', index=False)
