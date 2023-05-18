import UserLayout from "@/layouts/user/UserLayout.vue";
import Login from "@/pages/login/index.vue";
import Home from "@/pages/home/index.vue";
import ListProjects from "@/pages/project/list_projects.vue";

const routes = [
    {
        path: "/",
        name: "userlayout",
        component: UserLayout,
        redirect: "home",
        children: [
            {
                path: "home",
                name: "homepage",
                component: Home,
            },
            {
                path: "project",
                name: "listproject",
                component: ListProjects,
            },
        ],
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
];

export default routes;
