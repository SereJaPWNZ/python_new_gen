# 8.8. Пользовательские альбомы: начните с программы из упражнения 8.7. Напишите цикл
# while, в котором пользователь вводит исполнителя и название альбома.
# Затем в цикле вызывается функция make_album() для введенных пользователей
# и выводится созданный словарь. Не забудьте предусмотреть признак завершения в цикле while.

def make_album(artist_name, album_title, tracks=None):
    """Создает словарь состоящий из
    имени исполнителя, названия альбома,
    количества дорожек"""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print('Для завершения программы введите "q"'
          'или оставьте поле пустым')
    artist = input("\nВведите имя исполнителя: \n")
    if artist.lower() == 'q' or artist == '':
        break
    album = input("Введите название альбома: \n")
    if album.lower() == 'q' or album == '':
        break
    track = input("Введите количество дорожек(можно оставить пустым): \n")
    if track.lower() == 'q':
        break
    if track:
        print(make_album(artist, album, track))
    else:
        print(make_album(artist, album))
