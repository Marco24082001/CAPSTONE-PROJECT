import UserLayout from "@/layouts/user/UserLayout.vue";
import DashBoardLayout from "@/layouts/dashboard/DashboardLayout.vue";
import Login from "@/pages/login/index.vue";
import Register from "@/pages/register/index.vue";
import Home from "@/pages/home/index.vue";
import ListProjects from "@/pages/project/ListProjects.vue";
import ProjectDetail from "@/pages/project/ProjectDetail.vue";
import ManageProject from "@/pages/project/ManageProjects.vue";
import CreateProject from "@/pages/project/CreateProject.vue";
const routes = [
    {
        path: "/",
        name: "userlayout",
        component: UserLayout,
        redirect: "home",
        children: [
            {
                path: "home",
                name: "HomePage",
                component: Home,
            },
            {
                path: "projects",
                name: "Projects",
                component: ListProjects,
            },
            {
                path: "projects/:id",
                name: "Projectdetail",
                component: ProjectDetail,
            },
            {
                path: "dashboard",
                name: "Dashboard",
                component: DashBoardLayout,
                redirect: "dashboard/projects",
                children: [
                    {
                        path: "projects",
                        name: "ManageProject",
                        component: ManageProject,
                    },
                    {
                        path: "projects/create",
                        name: "CreateProject",
                        component: CreateProject,
                    },
                ],
            },
        ],
    },
    {
        path: "/:user",
        name: "",
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",   
        component: Register,
    }
];

export default routes;
