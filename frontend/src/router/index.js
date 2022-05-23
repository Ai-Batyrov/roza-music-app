import {createRouter, createWebHashHistory} from "vue-router";
import ChartsView from "@/views/ChartsView";
import ChartPlaylistView from "@/views/ChartPlaylist/ChartPlaylistView";
import RadioStationsView from "@/views/RadioStationsView";
import SearchView from "@/views/SearchView";
import LikedSongsView from "@/views/LikedSongsView";
import PlaylistView from "@/views/PlaylistView";


const routes = [
    {
        path: "/",
        name: "home",
        component: ChartsView,
    },
    {
        path: "/chart/:id",
        name: "chart-playlist",
        component: ChartPlaylistView,
    },
    {
        path: "/playlist/:id",
        name: "user-playlist",
        component: PlaylistView,
    },
    {
        path: "/radio",
        name: "radio",
        component: RadioStationsView,
    },
    {
        path: "/search",
        name: "search",
        component: SearchView
    },
    {
        path: '/liked',
        name: 'liked-songs',
        component: LikedSongsView
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
