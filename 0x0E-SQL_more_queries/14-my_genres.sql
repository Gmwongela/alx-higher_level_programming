-- Script that lists all genres of the show Dexter in the database hbtn_0d_tvshows
-- Records are ordered by ascending genre name
SELECT name FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
