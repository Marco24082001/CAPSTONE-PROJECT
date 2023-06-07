<template>
    <div class="container">
        <div class="project-header">
            <div class="project-media">
                <img :src="project.image_url" />
            </div>
            <div class="project-summary">
                <h1 class="project-title">{{ project.title }}</h1>
                <div class="project-main">
                    <div class="project-info">
                        <div class="project-session-1">
                            <div class="project-author">
                                <img
                                    src="https://givenow.vn/wp-content/uploads/2022/08/_resampled/File-Anh-Logo-Quy-Phan-Anh-fit-60-60.jpg"
                                />
                                <a href="#">Quỹ học bổng Huỳnh Tấn Phát</a>
                            </div>
                            <div class="project-giver-number">
                                <div class="bx bx-donate-blood"></div>
                                100
                            </div>
                        </div>
                        <div class="project-goal">
                            <span>Mục tiêu dự án</span>
                            <span>{{ project.fund_goal }}</span>
                        </div>
                        <div class="project-fund-raised">
                            <div class="neo-progressbar">
                                <div></div>
                            </div>
                            <div class="fund-raised-number">
                                <span>Đã đạt được</span>
                                <span>{{ project.fund_total }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-form-donation">
                        <el-input-number
                            v-model="amount"
                            :min="10000"
                            :step="1000"
                            controls-position="right"
                            size="large"
                        />
                        <el-button type="primary" size="large"> Ủng hộ ngay </el-button>
                    </div>
                </div>
            </div>
        </div>
        <div class="project-content" v-html="project.description"></div>
    </div>
</template>

<script>
import ProjectService from '@/services/project/ProjectService';
export default {
    name: "project-detail",
    data() {
        return {
            project: {},
            amount: 0,
        };
    },
    mounted() {
        console.log(this.$route.params.id);
    },
    async created() {
        this.project = (await ProjectService.getbyId(this.$route.params.id)).data;
        console.log(this.project)
    }
};
</script>

<style scoped lang="scss">
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--cs-main-panel-pading);
    gap: 3rem;

    .project-header {
        display: flex;
        width: 100%;
        gap: 2rem;
        .project-media {
            flex: 46%;
            img {
                border-radius: 1.5rem;
                width: 100%;
            }
        }
        .project-summary {
            flex: 54%;
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            .project-title {
                margin-top: 0;
                margin-bottom: 0;
                font-family: var(--cs-font-headings-family), sans-serif;
                font-weight: var(--cs-font-headings-weight);
                text-transform: var(--cs-font-headings-text-transform);
                letter-spacing: var(--cs-font-headings-letter-spacing);
                word-wrap: break-word;
                font-size: 1.2rem;
                line-height: 1.2;
            }
            .project-main {
                display: flex;
                flex-direction: column;
                gap: 2rem;
                .project-info {
                    padding: 1.2rem;
                    background: #a7a7a710;
                    border-radius: 15px 15px 0 0;
                    .project-session-1 {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        .project-author {
                            gap: 0.5rem;
                            display: flex;
                            align-items: center;
                            img {
                                width: 2.5rem;
                                border-radius: 50%;
                            }
                        }
                    }
                    .project-goal {
                        margin-top: 1rem;
                        display: flex;
                        justify-content: space-between;
                    }
                    .project-fund-raised {
                        .neo-progressbar {
                            margin: 0.5rem 0;
                            border-radius: 6px;
                            background-color: #ff2e5b1a;
                            div {
                                height: 0.4rem;
                                border-radius: 6px;
                                width: 40%;
                                background-color: #ff2e5b;
                                z-index: 11111;
                            }
                        }
                        .fund-raised-number {
                            display: flex;
                            justify-content: space-between;
                        }
                    }
                }
                .project-form-donation {
                    // margin-top: 3rem;
                    display: flex;
                    justify-content: space-between;
                }
            }
        }
    }
    .project {
    }
}

@media (max-width: 800px) {
    .project-header {
        display: flex;
        flex-direction: column;
    }
}
</style>
