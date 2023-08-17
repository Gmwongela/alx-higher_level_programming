-- Script that lists all comedy shows in the database hbtn_0d_tvshows
-- Records are ordered by descending show title
SELECT title FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
