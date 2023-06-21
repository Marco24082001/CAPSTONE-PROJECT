export function storeTokenToVuex(payload) {
    const store = require("@/store");
    let { access, refresh } = payload;
    store.default.commit("authentication/setTokenInfo", { access, refresh });
}

export function storeCurrentUserToVuex(payload) {
    let { id, email, first_name, last_name, full_name, role, phone, avatar } = payload;
    const currentUser = { id, email, first_name, last_name, full_name, role, phone, avatar };
    const store = require("@/store");
    store.default.commit("user/setCurrentUser", currentUser);
}
