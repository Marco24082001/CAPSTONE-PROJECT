export default {
    namespaced: true,
    state: {
        currentUser: {
            id: null,
            fist_name: null,
            last_name: null,
            full_name: null,
            email: null,
            password: null,
            avatar: null,
            role: null,
        },
    },
    getters: {
        getCurrentUser(state) {
            return state.currentUser;
        },
    },
    mutations: {
        setCurrentUser(state, currentUser) {
            state.currentUser = currentUser;
        },
    },
};
