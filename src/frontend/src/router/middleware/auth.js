export function Authenticate({ next, router, store }) {
    if (!store.state.authentication.tokenInfo.access) {
        return router.push({ name: "login" });
    }
    return next();
}
