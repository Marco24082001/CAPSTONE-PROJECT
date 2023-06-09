<template>
    <div class="container">
        <div class="cp-header">
            <div class="button-create-wrapper">
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
            <CardProject v-for="project in listProjects" :project="project" :key="project.id" :isManageProject=Boolean(true)></CardProject>
        </div>
    </div>
</template>

<script>
import CardProject from "@/pages/project/cardProject.vue";
import ProjectService from "@/services/project/ProjectService";
export default {
    name: "Manage-Projects",
    components: {
        CardProject,
    },
    data() {
        return {
            listProjects: [],
        };
    },
    async created() {
        //                 isManageProject="true"
        this.listProjects = (await ProjectService.getProjectOwner()).data;
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
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 0px 5%;
    .cp-projects {
        width: 100%;
        align-self: center;
        // height: 65vh;
        display: inline-flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 4rem;
    }

    .cp-header {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        margin-bottom: 3rem;
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
