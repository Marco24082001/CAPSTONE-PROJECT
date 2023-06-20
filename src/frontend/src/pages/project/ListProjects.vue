<template>
    <div class="container">
        <AppToolbar>
            <template #content
                ><el-breadcrumb :separator-icon="ArrowRight">
                    <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
                    <el-breadcrumb-item :to="{ path: '/projects' }">Project</el-breadcrumb-item>
                </el-breadcrumb></template
            >
        </AppToolbar>

        <div class="filter-group">
            <el-radio-group v-model="statusFilter">
                <el-radio-button label="ACTIVE">ACTIVE</el-radio-button>
                <el-radio-button label="FINISHED" class="finished">FINISHED</el-radio-button>
                <el-radio-button label="INACTIVE" class="inactive">INACTIVE</el-radio-button>
            </el-radio-group>
        </div>
        <div class="cp-projects">
            <CardProject
                v-for="project in resultQuery"
                :project="project"
                :key="project.id"
            ></CardProject>
        </div>
    </div>
</template>

<script>
import ProjectService from "@/services/project/ProjectService";
import AppToolbar from "@/components/AppToolbar.vue";
import CardProject from "@/pages/project/CardProject.vue";
export default {
    name: "List-Projects",
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

    computed: {
        resultQuery() {
            if (this.searchQuery != "") {
                return this.listProjects.filter((item) => {
                    return (
                        item.status === this.statusFilter &&
                        item.title.toLowerCase().includes(this.searchQuery.toLowerCase())
                    );
                });
            } else {
                return this.listProjects.filter((item) => {
                    return item.status === this.statusFilter;
                });
            }
        },
    },

    async created() {
        this.listProjects = (await ProjectService.getAll()).data;
        console.log(this.listProjects);
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
    padding: var(--cs-main-panel-pading);
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    gap: 2rem;

    .filter-group {
        display: flex;
        justify-content: center;
        align-items: center;
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
    }
    .cp-projects {
        position: relative;
        width: 100%;
        align-self: center;
        height: 28rem;
        display: inline-flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 4rem;
    }
}
</style>
