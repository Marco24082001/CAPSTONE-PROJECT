<template>
    <div class="container">
        <AppToolbar>
            <template #content
                ><el-breadcrumb>
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>
                    <el-breadcrumb-item>Project</el-breadcrumb-item>
                </el-breadcrumb></template
            >
        </AppToolbar>
        <div class="cp-header">
            <div class="filter-group">
                <el-radio-group v-model="statusFilter">
                    <el-radio-button label="ACTIVE">ACTIVE</el-radio-button>
                    <el-radio-button label="FINISHED" class="finished">FINISHED</el-radio-button>
                    <el-radio-button label="INACTIVE" class="inactive">INACTIVE</el-radio-button>
                    <el-radio-button label="UNVERIFIED" class="unverified"
                        >UNVERIFIED</el-radio-button
                    >
                </el-radio-group>
            </div>
            <div class="button-create-wrapper" v-if="user.currentUser.role === 'USER'">
                <RouterLink to="/dashboard/projects/create">Start Project!</RouterLink>
                <div class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 268.832 268.832">
                        <path
                            d="M265.17 125.577l-80-80c-4.88-4.88-12.796-4.88-17.677 0-4.882 4.882-4.882 12.796 0 17.678l58.66 58.66H12.5c-6.903 0-12.5 5.598-12.5 12.5 0 6.903 5.597 12.5 12.5 12.5h213.654l-58.66 58.662c-4.88 4.882-4.88 12.796 0 17.678 2.44 2.44 5.64 3.66 8.84 3.66s6.398-1.22 8.84-3.66l79.997-80c4.883-4.882 4.883-12.796 0-17.678z"
                        />
                    </svg>
                </div>
            </div>
        </div>

        <div class="cp-projects">
            <CardProject
                v-for="project in resultQuery"
                :project="project"
                :key="project.id"
                :isManageProject="Boolean(true)"
            ></CardProject>
        </div>
    </div>
</template>

<script>
import CardProject from "@/pages/project/CardProject.vue";
import ProjectService from "@/services/project/ProjectService";
import AppToolbar from "@/components/AppToolbar.vue";
import { mapState } from "vuex";
import { ElMessage } from "element-plus";

export default {
    name: "Manage-Projects",
    components: {
        CardProject,
        AppToolbar,
    },
    data() {
        return {
            listProjects: [],
            statusFilter: "ACTIVE",
            searchQuery: "",
        };
    },
    async created() {
        this.getAllProjects();
    },
    computed: {
        ...mapState(["user"]),
        resultQuery() {
            if (this.searchQuery != "") {
                return this.listProjects.filter((item) => {
                    if (this.statusFilter === "UNVERIFIED") {
                        return item.is_verified;
                    }
                    return (
                        item.status === this.statusFilter &&
                        item.title.toLowerCase().includes(this.searchQuery.toLowerCase())
                    );
                });
            } else {
                return this.listProjects.filter((item) => {
                    if (this.statusFilter === "UNVERIFIED") {
                        return !item.is_verified;
                    }
                    return item.status === this.statusFilter;
                });
            }
        },
    },
    methods: {
        async getAllProjects() {
            let res = null;
            if (this.user.currentUser.role === "ADMIN") {
                res = await ProjectService.getAll();
            } else {
                res = await ProjectService.getProjectOwner(this.user.currentUser.id);
            }
            if (!res.error) {
                this.listProjects = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },
    },
};
</script>

<style scoped lang="scss">
:root {
    --bodyBack: #ffeaed;
    --textColor: #1b2741;
    --starColor: #f67034;
    --sectionBack: #f7f6f9;
}

.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: var(--cs-main-panel-pading);
    gap: 2rem;

    .filter-group {
        .finished {
            :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
                background: rgb(103, 194, 58) !important;
                border-color: rgb(103, 194, 58) !important;
                box-shadow: -1px 0 0 0 rgb(103, 194, 58) !important;
            }
            :deep(.el-radio-button__inner:hover) {
                color: rgb(108, 231, 126);
            }
        }
        .inactive {
            :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
                background: rgb(245, 108, 108) !important;
                border-color: rgb(245, 108, 108) !important;
                box-shadow: -1px 0 0 0 rgb(245, 108, 108) !important;
            }
            :deep(.el-radio-button__inner:hover) {
                color: rgb(245, 108, 108);
            }
        }

        .unverified {
            :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
                background: rgb(133, 119, 119) !important;
                border-color: rgb(133, 119, 119) !important;
                box-shadow: -1px 0 0 0 rgb(133, 119, 119) !important;
            }
            :deep(.el-radio-button__inner:hover) {
                color: rgb(133, 119, 119);
            }
        }
    }

    .cp-projects {
        width: 100%;
        align-self: center;
        display: inline-flex;
        flex-wrap: wrap;
        gap: 4rem;
        // justify-content: center;
    }

    .cp-header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        // justify-items: center;
        // margin-bottom: 1rem;
        .button-create-wrapper {
            position: relative;
            a {
                display: block;
                width: 200px;
                height: 40px;
                line-height: 40px;
                font-weight: 500;
                text-decoration: none;
                background: var(--cs-color-button);
                text-align: center;
                color: var(--wc-primary-text);
                text-transform: uppercase;
                letter-spacing: 1px;
                // border: 3px solid #333;
                transition: all 0.35s;
                cursor: pointer;
                &:hover {
                    width: 200px;
                    border: 3px solid var(--cs-color-button);
                    background: transparent;
                    color: var(--cs-color-button);
                }
                &:hover + .icon {
                    border: 3px solid var(--cs-color-button);
                    right: -18%;
                    z-index: 1;
                }
            }
            .icon {
                width: 40px;
                height: 40px;
                border: 3px solid transparent;
                position: absolute;
                transform: rotate(45deg);
                right: 0;
                top: 0;
                z-index: -1;
                transition: all 0.35s;
                svg {
                    width: 30px;
                    position: absolute;
                    top: calc(50% - 15px);
                    left: calc(50% - 15px);
                    transform: rotate(-45deg);
                    fill: var(--cs-color-button);
                    transition: all 0.35s;
                }
            }
        }
    }
}
</style>
