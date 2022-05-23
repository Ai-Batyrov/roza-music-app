import vuex, {createStore} from 'vuex'
import playlist from "./modules/playlist";
import user from "./modules/user";

export default createStore({
    modules: {
        playlist, user
    }
})
