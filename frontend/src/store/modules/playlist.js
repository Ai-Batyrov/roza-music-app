import axios from "axios";
import player from "@/assets/js/Player"

export default {
    actions: {
        getSample: async function (ctx) {
            await axios
                .get('/api/v1/track/2')
                .then(response => {
                    ctx.commit('updatePlaylist', response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        playItem: async function (ctx, playlist) {
            await ctx.commit('updatePlaylist', playlist)
        }
    },
    mutations: {
        async updatePlaylist(state, track_id) {
            await axios
                .get('/api/v1/track/' + track_id)
                .then(response => {
                    state.playlist.push(response.data)
                    console.log(state.playlist)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    state: {
        playlist: [
            {
                "id": 2,
                "title": "Mi Gente (Dj Mario rmx)",
                "artist": "J Balvin ft Willy William",
                "file": "http://127.0.0.1:8000/media/tracks/Mi_Gente_-_J_Balvin_Ft_Willy_Williams__Extended_Mix_Dj_Mario_Andretti_.mp3",
                "album": 3,
                "genres": [
                    1
                ]
            },
        ],
    },
    getters: {
        getPlaylist: function (state) {
            return state.playlist
        },
        getCurrent: function (state) {
            return state.playlist[0]
        },
        getLength: function (state) {
            return state.playlist.length
        }
    },
}
