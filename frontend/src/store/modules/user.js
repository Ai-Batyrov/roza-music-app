import axios from "axios";

export default {
    actions: {
        userLogin(ctx, usercredentials) {
            return new Promise(resolve => {
                axios
                    .post('/api-token/', {
                        username: usercredentials.username,
                        password: usercredentials.password
                    })
                    .then(response => {
                        ctx.commit('updateStorage', {
                            access: response.data.access,
                            refresh: response.data.refresh
                        })
                        resolve()
                    })
            })
        }
    },
    mutations: {
        updateStorage(state, {access, refresh}) {
            state.accessToken = access
            state.refreshToken = refresh
        }
    },
    state: {
        accessToken: null,
        refreshToken: null
    },
    getters: {},
}
