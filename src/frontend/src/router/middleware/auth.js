export function Authenticate({ next, router, store }) {
    if (!store.state.authentication.tokenInfo.access) {
        return router.push({ name: "login" });
    }
    return next();
}

export function AuthorizeAdmin({ next, store }) {
    if (store.state.user.currentUser.role === "ADMIN") {
        return next();
    }
    return next({ path: "/home" });
}
