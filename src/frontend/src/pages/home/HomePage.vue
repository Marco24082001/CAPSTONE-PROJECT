<template>
    <div id="home-page-section">
        <header>
            <div class="header-content">
                <h2>
                    Convenient, Reliable And Transparent Online Fundraising And Donation Connection
                </h2>
                <div class="line"></div>
                <h1>A WONDERFUL GIFT</h1>
                <a href="#" class="ctn">Learn More</a>
            </div>
        </header>
        <section>
            <div class="title">
                <h1>The project is fundraising</h1>
                <div class="line"></div>
            </div>
            <div class="section-content">
                <el-carousel :interval="4000" type="card" height="29rem">
                    <el-carousel-item v-for="project in listProjects" :key="project.id">
                        <CardProject :project="project"></CardProject>
                    </el-carousel-item>
                </el-carousel>
            </div>
        </section>
    </div>
</template>

<script>
import ProjectService from "@/services/project/ProjectService";
import CardProject from "@/pages/project/CardProject.vue";
export default {
    name: "home-page",
    components: {
        CardProject,
    },
    data() {
        return {
            listProjects: [],
        };
    },
    async created() {
        this.listProjects = (await ProjectService.getActiveProjects()).data;
        console.log(this.listProjects);
    },
};
</script>

<style lang="scss" scoped>
#home-page-section {
    margin-top: calc(var(--cs-header-initial-height) * -1);
    font-size: 4vmin;

    header {
        width: 100vw;
        position: relative;
        height: 80vh;
        background-image: url("../../assets/bg1.jpg");
        background-position: center;
        background-size: cover;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    header::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(
            0,
            0,
            0,
            0.4
        ); /* Adjust the alpha value (0.5) to control the darkness */
        z-index: 1;
    }

    .header-content {
        position: relative;
        z-index: 2;
        font-family: Serif;
        color: rgb(255, 255, 255);
        text-align: center;
    }

    .line {
        width: 250px;
        height: 4px;
        background-color: #fc036b;
        margin: 10px auto;
        border-radius: 5px;
    }
    .header-content h1 {
        font-size: 7vmin;
        margin-top: 50px;
        margin-top: 30px;
    }
    .ctn {
        padding: 8px 15px;
        background: #fc036b;
        border-radius: 30px;
        color: whitesmoke;
    }

    // Projects
    section {
        width: 80%;
        margin: 80px auto;
    }
    .title {
        text-align: center;
        font-size: 3vmin;
    }

    .section-content {
        margin-top: 2rem;
    }
    .el-carousel__item {
        color: #475669;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
}
</style>
