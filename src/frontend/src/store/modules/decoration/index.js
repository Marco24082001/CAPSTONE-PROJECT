export default {
    namespaced: true,
    state: {
        themeMode: "default",
    },
    mutations: {
        setThemeMode(state, value) {
            state.themeMode = value;
        },
    },
};
