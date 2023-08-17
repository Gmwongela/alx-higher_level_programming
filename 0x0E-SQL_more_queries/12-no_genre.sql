-- Script that lists all shows in the database hbtn_0d_tvshows without a genre linked
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
