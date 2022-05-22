import {createRouter, createWebHashHistory} from "vue-router";
import ChartsView from "@/views/ChartsView";
import ChartPlaylistView from "@/views/ChartPlaylist/ChartPlaylistView";
import RadioStationsView from "@/views/RadioStationsView";
import SearchView from "@/views/SearchView";


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
        path: "/radio",
        name: "radio",
        component: RadioStationsView,
    },
    {
        path: "/search",
        name: "search",
        component: SearchView
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
