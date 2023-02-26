from flask import Flask, request

app = Flask(__name__)

dummyData = {
    "obj": {
        "obj": [
            {
                "cm_artist": "3907",
                "name": "Marshmello",
                "pronoun": "he/him",
                "band": False,
                "image_url": "https://i.scdn.co/image/ab6761610000517441e4a3b8c1d45a9e49b6de21",
                "code2": "US",
                "cm_tag": [
                    462887,
                    462882,
                    462885
                ],
                "radio_spins": 2539867,
                "num_am_editorial_playlists": 418,
                "num_am_playlists": 1334,
                "num_az_editorial_playlists": 659,
                "num_az_playlists": 729,
                "boomplay_favorites": 1754,
                "boomplay_plays": 6200000,
                "de_editorial_playlist_total_reach": 9830979,
                "de_playlist_total_reach": 13412128,
                "deezer_fans": 2646549,
                "num_de_editorial_playlists": 94,
                "num_de_playlists": 1027,
                "line_music_artist_likes": 32589,
                "line_music_likes": 121929,
                "line_music_mv_plays": 6242,
                "line_music_plays": 13559407,
                "melon_artist_fans": 22330,
                "melon_likes": 413444,
                "melon_video_likes": 2323,
                "melon_video_views": 289096,
                "pandora_lifetime_stations_added": 3560218,
                "pandora_lifetime_streams": 1431410071,
                "pandora_listeners_28_day": 1427922,
                "soundcloud_followers": None,
                "soundcloud_plays": 559811049,
                "num_sp_editorial_playlists": 492,
                "num_sp_playlists": 799497,
                "sp_editorial_playlist_total_reach": 64832955,
                "sp_followers": 34626586,
                "sp_followers_to_listeners_ratio": 0.854659,
                "sp_monthly_listeners": 40515079,
                "sp_playlist_total_reach": 386655639,
                "sp_popularity": 83,
                "bs_followers": 794212,
                "facebook_followers": 18749251,
                "facebook_talks": 33865,
                "genius_pageviews": 16812270,
                "ins_engagement_rate": 1.2682,
                "ins_followers": 29753164,
                "shazam_count": 72989362,
                "siriusXm_spins": 9797,
                "tiktok_engagement_rate": 0.8616,
                "tiktok_followers": 27200000,
                "tiktok_likes": 213000000,
                "tiktok_top_video_views": 6264937024,
                "tiktok_track_posts": 11860106,
                "twitch_followers": 45499,
                "twitch_monthly_viewer_hours": None,
                "twitch_views": 89325,
                "twitch_weekly_viewer_hours": None,
                "ts_followers": 2457761,
                "ts_retweets": 899,
                "ws_views": 1365,
                "num_yt_editorial_playlists": 43,
                "num_yt_playlists": 460,
                "ycs_subscribers": 56100000,
                "ycs_views": 13923264282,
                "youtube_daily_video_views": 4090761,
                "youtube_engagement_rate": 0.05159999999999999,
                "youtube_monthly_video_views": 114310263,
                "yt_editorial_playlist_total_reach": 24792522,
                "yt_playlist_total_reach": 24792522,
                "cm_artist_rank": 73,
                "cm_artist_score": 182534,
                "rank_fb": 30,
                "rank_eg": 148,
                "genres": "Pop, Dance, Electronic",
                "career_status": {
                    "stage": "superstar",
                    "stage_score": 36,
                    "trend": "decline",
                    "trend_score": 12
                }
            },
        ],
        "offset": 10,
        "total": 49
    }
}

@app.route("/")
def index():
    return "Hello World1"

@app.route("/search", methods=['POST'])
def search():
    data = request.get_json()
    print(data)
    requestedgenreId = data["target_genre"]
    careerStage = data["career_stage"]
    target_country = data["target_country"]
    name = data["target_genre"]
    originalGenreId = data["my_genre"]

    return dummyData

if __name__ == "__main__":
    app.run(debug=True)