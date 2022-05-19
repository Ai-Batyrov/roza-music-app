import {createApp} from "vue";
import App from "./App.vue";
import axios from "axios";
import VueAxios from "vue-axios"
import router from "./router";

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App)
    .use(router, axios)
    // .use(VueAxios, axios)
    .mount("#app");
