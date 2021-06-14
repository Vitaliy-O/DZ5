import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://vomar:Paviliondv6@localhost:5432/music_site')
engine
connection = engine.connect()



sel5_5 = connection.execute("""SELECT name, genre_name  FROM songwriter s
JOIN sw_genres sw ON s.id = sw.id_sw
JOIN genre g ON sw.id_genre = g.id;
""").fetchall()
print(sel5_5)
print()

# 1.	количество исполнителей в каждом жанре;
sel5_1 = connection.execute("""SELECT genre_name, COUNT(name)  FROM songwriter s
JOIN sw_genres sw ON s.id = sw.id_sw
JOIN genre g ON sw.id_genre = g.id
GROUP BY g.genre_name; 
""").fetchall()
print('#1.	количество исполнителей в каждом жанре;')
print(sel5_1)
print()

# 2.	количество треков, вошедших в альбомы 2019-2020 годов;
sel5_2 = connection.execute("""SELECT released, COUNT(track_name)  FROM songwriters_albums sa
JOIN tracks t ON sa.id = t.id_album
WHERE sa.released >= 2019 AND sa.released <= 2020
GROUP BY sa.released; 
""").fetchall()
print('#2.	количество треков, вошедших в альбомы 2019-2020 годов;')
print(sel5_2)
print()

# 3.	средняя продолжительность треков по каждому альбому;
sel5_3 = connection.execute("""SELECT name_album, AVG(duration)  FROM songwriters_albums sa
JOIN tracks t ON sa.id = t.id_album
GROUP BY name_album; 
""").fetchall()
print('#3.	средняя продолжительность треков по каждому альбому;')
print(sel5_3)
print()

# 4.	все исполнители, которые не выпустили альбомы в 2020 году;
sel5_4 = connection.execute("""SELECT name  FROM songwriter s
JOIN joint_album ja ON s.id = ja.id_sw
JOIN songwriters_albums sa ON ja.id_album = sa.id
WHERE released != 2020
GROUP BY s.name;
""").fetchall()
print('#4.	все исполнители, которые не выпустили альбомы в 2020 году')
print(sel5_4)
print()

# 5.	названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
sel5_5 = connection.execute("""SELECT name_collection  FROM collection c
JOIN tc_sa tc ON c.id = tc.collection_id
JOIN tracks t ON tc.tracks_id = t.id
JOIN songwriters_albums sa ON t.id_album = sa.id
JOIN joint_album ja ON sa.id = ja.id_album
JOIN songwriter s ON ja.id_sw = s.id
WHERE s.name = 'Гр. Кино'
GROUP BY c.name_collection;
""").fetchall()
print('#5.	названия сборников, в которых присутствует конкретный исполнитель, например "Гр. Кино"')
print(sel5_5)
print()

# 7.	наименование треков, которые не входят в сборники;
sel5_7 = connection.execute("""SELECT track_name  FROM tracks t
JOIN tc_sa tc ON t.id = tc.tracks_id
JOIN collection c ON tc.collection_id = c.id
WHERE t.track_name NOT IN (c.name_collection)
GROUP BY t.track_name;
""").fetchall()
print('#7. наименование треков, которые не входят в сборники;')
print(sel5_7)
print()


# 8.	исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
sel5_8 = connection.execute("""SELECT name, track_name, duration  FROM songwriter s
JOIN joint_album ja ON s.id = ja.id_sw 
JOIN songwriters_albums sa ON ja.id_album = sa.id
JOIN tracks t ON sa.id = t.id_album
WHERE t.duration = (SELECT MIN(duration) FROM tracks)
GROUP BY s.name, t.track_name, t.duration;
""").fetchall()
print('#8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)')
print(sel5_8)
print()
print('________________________________________________')
# 6.	название альбомов, в которых присутствуют исполнители более 1 жанра;
sel5_6 = connection.execute("""SELECT name_album  FROM songwriters_albums sa
JOIN joint_album ja ON sa.id = ja.id_album 
JOIN songwriter s ON ja.id_album = s.id
JOIN sw_genres sg ON s.id = sg.id_sw
JOIN genre g ON sg.id_genre = g.id

GROUP BY sa.name_album;
""").fetchall()
print('#6. название альбомов, в которых присутствуют исполнители более 1 жанра;')
print(sel5_6)
print()


# 9.	название альбомов, содержащих наименьшее количество треков.
sel5_9 = connection.execute("""SELECT name_album, COUNT(track_name) FROM songwriters_albums sa
JOIN tracks t ON sa.id = t.id_album

GROUP BY sa.name_album;
""").fetchall()
print('#9. название альбомов, содержащих наименьшее количество треков')
print(sel5_9)
print()


