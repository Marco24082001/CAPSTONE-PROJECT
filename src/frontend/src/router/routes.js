import UserLayout from "@/layouts/user/UserLayout.vue";
import DashBoardLayout from "@/layouts/dashboard/DashboardLayout.vue";
import Login from "@/pages/login/index.vue";
import Register from "@/pages/register/index.vue";
import Home from "@/pages/home/HomePage.vue";
import ListProjects from "@/pages/project/ListProjects.vue";
import ProjectDetail from "@/pages/project/ProjectDetail.vue";
import ManageProject from "@/pages/project/ManageProjects.vue";
import CreateProject from "@/pages/project/CreateProject.vue";
import EditProject from "@/pages/project/EditProject.vue";
import TypeProject from "@/pages/project/TypeProject.vue";
import LikeProject from "@/pages/project/LikeProject.vue";
import Author from "@/pages/author/AuthorPage.vue";
import ManageUser from "@/pages/manageruser/ManageUser.vue";
import EditProfile from "@/pages/editprofile/EditProfile.vue";
import NotFound from "@/pages/notfound/NotFoundPage.vue";

import { Authenticate, AuthorizeAdmin } from "./middleware/auth";

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
                path: "author/:id",
                name: "Author",
                component: Author,
            },
            {
                path: "user/edit-profile",
                name: "EditProfile",
                component: EditProfile,
                meta: {
                    middleware: [Authenticate],
                },
            },
            {
                path: "dashboard",
                name: "Dashboard",
                component: DashBoardLayout,
                redirect: "dashboard/projects",
                meta: {
                    middleware: [Authenticate],
                },
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
                    {
                        path: "projects/:id/edit",
                        name: "EditProject",
                        component: EditProject,
                    },
                    {
                        path: "projects/:id",
                        name: "OwnerProjectDetail",
                        component: ProjectDetail,
                    },
                    {
                        path: "likes",
                        name: "LikeProject",
                        component: LikeProject,
                    },
                    {
                        path: "types",
                        name: "ManageType",
                        component: TypeProject,
                        meta: {
                            middleware: [AuthorizeAdmin],
                        },
                    },
                    {
                        path: "users",
                        name: "ManageUser",
                        component: ManageUser,
                        meta: {
                            middleware: [AuthorizeAdmin],
                        },
                    },
                ],
            },
        ],
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
    },
    {
        path: "/:catchAll(.*)",
        name: "notfound",
        component: NotFound,
    },
];

export default routes;
