export default {
    namespaced: true,
    state: {
        themeMode: "default",
        fullscreenLoading: false,
    },
    getters: {
        getFullscreenLoading(state) {
            return state.fullscreenLoading;
        },
        getThemeMode(state) {
            return state.themeMode;
        },
    },
    mutations: {
        setThemeMode(state, value) {
            state.themeMode = value;
        },
        setFullscreenLoading(state, status) {
            state.fullscreenLoading = status;
        },
    },
};


// this.$store.commit("decoration/setFullscreenLoading", true);