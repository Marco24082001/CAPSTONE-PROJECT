<template>
    <div class="container">
        <div class="cp-projects">
            <CardProject
                v-for="project in listProjects"
                :project="project"
                :key="project.id"
            ></CardProject>
        </div>
    </div>
</template>

<script>
import ProjectService from "@/services/project/ProjectService";
import CardProject from "@/pages/project/cardProject.vue";
export default {
    name: "List-Projects",
    components: {
        CardProject,
    },
    data() {
        return {
            listProjects: [],
        };
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
    .cp-projects {
        position: relative;
        width: 100%;
        align-self: center;
        height: 28rem;
        display: inline-flex;
        // justify-content: center;
        flex-wrap: wrap;
        gap: 4rem;
    }
}
</style>
