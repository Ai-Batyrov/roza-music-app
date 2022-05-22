import vuex, {createStore} from 'vuex'
import playlist from "./modules/playlist";

export default createStore({
    modules: {
        playlist
    }
})
