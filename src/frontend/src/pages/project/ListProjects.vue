<template>
    <div class="container">
        <div class="cp-projects">
            <CardProject
                project_img="project-0.jpg"
                author_img="https://givenow.vn/wp-content/uploads/2022/08/_resampled/File-Anh-Logo-Quy-Phan-Anh-fit-60-60.jpg"
            ></CardProject>
            <CardProject
                project_img="project-1.jpg"
                author_img="https://givenow.vn/wp-content/uploads/2022/08/_resampled/File-Anh-Logo-Quy-Phan-Anh-fit-60-60.jpg"
            ></CardProject>
            <CardProject
                project_img="project-2.png"
                author_img="https://givenow.vn/wp-content/uploads/2022/08/_resampled/File-Anh-Logo-Quy-Phan-Anh-fit-60-60.jpg"
            ></CardProject>
        </div>
    </div>
</template>

<script>
import CardProject from "@/pages/project/cardProject.vue"
export default {
    name: "List-Projects",
    components: {
        CardProject,
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
    .cp-projects {
        width: 100%;
        align-self: center;
        // height: 65vh;
        display: inline-flex;
        // justify-content: center;
        flex-wrap: wrap;
        gap: 4rem;
    }
}
</style>
