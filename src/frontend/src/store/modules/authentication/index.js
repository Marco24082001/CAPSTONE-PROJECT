export default {
    namespaced: true,
    state: {
        tokenInfo: {
            access: null,
            refresh: null,
        },
    },
    getters: {
        getTokenInfo(state) {
            return state.tokenInfo;
        },
    },
    mutations: {
        setTokenInfo(state, { access, refresh }) {
            state.tokenInfo = { access, refresh };
        },
    },
};
