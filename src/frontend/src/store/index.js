import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import user from "./modules/user";
import authentication from "./modules/authentication";
import decoration from "./modules/decoration";
// import animation from "./modules/animation";

export default createStore({
    plugins: [createPersistedState()],
    modules: {
        authentication: authentication,
        user: user,
        decoration: decoration,
    },
});
