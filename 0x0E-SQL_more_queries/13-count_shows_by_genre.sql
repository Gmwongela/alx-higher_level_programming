-- Script that lists all genres from the database hbtn_0d_tvshows along with
-- with the number of shows linked to each
-- Does not display genres without linked shows
-- Records are ordered by descending number of shows linked
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
