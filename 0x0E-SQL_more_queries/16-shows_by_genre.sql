-- Script that lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows
-- Records are ordered by ascending show title and genre name
SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
