import Login from "@/pages/login/index.vue";
import Home from "@/pages/home/index.vue";
const routes = [
    {
        path: "",
        name: "home",
        component: Home,
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
];

export default routes;
