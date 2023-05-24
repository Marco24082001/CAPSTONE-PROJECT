import UserLayout from "@/layouts/user/UserLayout.vue";
import Login from "@/pages/login/index.vue";
import Home from "@/pages/home/index.vue";
import ListProjects from "@/pages/project/list_projects.vue";
import ProjectDetail from "@/pages/project/project_detail.vue";

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
                path: "projects",
                name: "Projects",
                component: ListProjects,
            },
            {
                path: "projects/:id",
                name: "projectdetail",
                component: ProjectDetail,
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
