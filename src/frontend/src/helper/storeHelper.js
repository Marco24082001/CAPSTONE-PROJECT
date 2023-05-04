export function storeTokenToVuex(payload) {
    const store = require("@/store");
    let { access, refresh } = payload;
    store.default.commit("authentication/setTokenInfo", { access, refresh });
}

export function storeCurrentUserToVuex(currentUser) {
    const store = require("@/store");
    store.default.commit("user/setCurrentUser", currentUser);
}
