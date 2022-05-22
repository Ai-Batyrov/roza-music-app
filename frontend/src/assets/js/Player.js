import PlayerNextButton from "@/components/buttons/PlayerNextButton";
import PlayerPrevButton from "@/components/buttons/PlayerPrevButton";
import PlayerPlayButton from "@/components/buttons/PlayerPlayButton";
import PlayerPauseButton from "@/components/buttons/PlayerPauseButton";
import {mapGetters, mapActions} from "vuex";
import store from "@/store";

export default {
    name: "Player",
    components: {PlayerPauseButton, PlayerPlayButton, PlayerNextButton, PlayerPrevButton},
    data() {
        return {
            player: new Audio(),
            current: store.getters.getCurrent,
            index: 0,
            isPlaying: false,
            playlist: store.getters.getPlaylist,
            playlistLength: store.getters.getLength
        }
    },
    async mounted() {
        // playlist: tracklist
        // this.current = store.getters.getCurrent
        // this.playlist = store.getters.getPlaylist
    },
    async computed() {
    },
    methods: {
        play(track) {
            if (typeof track.file != "undefined") {
                this.current = track
                this.player.src = this.current.file
            }
            this.player.play()
            this.player.addEventListener('ended', function () {
                this.index++
                if (this.index > this.playlist.length - 1) {
                    this.index = 0
                }
                this.current = this.playlist[this.index]
                this.play(this.current)
            }.bind(this))
            this.isPlaying = true
        },
        pause() {
            this.player.pause()
            this.isPlaying = false
        },
        next() {
            this.index++
            if (this.index > this.playlist.length - 1) {
                this.index = 0
            }
            this.current = this.playlist[this.index]
            this.play(this.current)
        },
        prev() {
            this.index--
            if (this.index < 0) {
                this.index = this.playlist.length - 1
            }
            this.current = this.playlist[this.index]
            this.play(this.current)
        },
    },
    created() {
        // this.current = this.playlist[this.index]
        this.player.src = this.current.file
    }
}
