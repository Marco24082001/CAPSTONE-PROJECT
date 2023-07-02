<template>
    <div class="container">
        <div class="content">
            <div class="page-header">
                <div class="page__author">
                    <div v-if="isOwner()" class="edit-button">
                        <router-link to="/user/edit-profile"
                            ><i class="bx bx-edit"></i
                        ></router-link>
                    </div>
                    <div class="page__author-photo">
                        <div class="author-thumbnail"><img :src="author.avatar" /></div>
                    </div>
                    <div class="page__author-info">
                        <h1 class="author-infor-title">{{ author.full_name }}</h1>
                        <div class="page__archive-count">{{ listProjects.length }} projects</div>
                        <div class="author-infor-contact">
                            <ul class="contact-wrap">
                                <li>
                                    <a href="tel:0122222">
                                        <div class="contact-icon-section">
                                            <div><i class="bx bxs-phone"></i></div>
                                        </div>
                                        <div class="contact-info-section">
                                            <span class="key">Hotline</span>
                                            <span v-if="author.phone" class="value">{{
                                                author.phone
                                            }}</span>
                                            <span v-else class="value">None</span>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="tel:0122222">
                                        <div class="contact-icon-section">
                                            <div><i class="bx bx-envelope"></i></div>
                                        </div>
                                        <div class="contact-info-section">
                                            <span class="key">Email</span>
                                            <span class="value">{{ author.email }}</span>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="tel:0122222">
                                        <div class="contact-icon-section">
                                            <div><i class="bx bxs-map"></i></div>
                                        </div>
                                        <div class="contact-info-section">
                                            <span class="key">Address</span>
                                            <span v-if="author.address" class="value">{{
                                                author.address
                                            }}</span>
                                            <span v-else class="value">None</span>
                                        </div>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="line-section"><hr /></div>

                        <div class="page__archive-description">"{{ author.biology }}"</div>
                    </div>
                </div>
            </div>
            <div class="page-projects-area">
                <div class="filter-group">
                    <el-radio-group v-model="statusFilter">
                        <el-radio-button label="ACTIVE">ACTIVE</el-radio-button>
                        <el-radio-button label="FINISHED" class="finished"
                            >FINISHED</el-radio-button
                        >
                        <el-radio-button label="INACTIVE" class="inactive"
                            >INACTIVE</el-radio-button
                        >
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
        </div>
    </div>
</template>

<script>
import { ElMessage } from "element-plus";
import UserService from "@/services/user/UserService";
import ProjectService from "@/services/project/ProjectService";
import { mapState } from "vuex";
import CardProject from "@/pages/project/CardProject.vue";
import TransactionService from "@/services/project/TransactionService";

export default {
    name: "author-page",
    components: {
        CardProject,
    },
    data() {
        return {
            author: {},
            listProjects: [],
            statusFilter: "ACTIVE",
            searchQuery: "",
            numberPersonSupport: 0,
        };
    },
    computed: {
        ...mapState(["user"]),
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
        this.getAuthor();
        this.getAllProjects();
        this.getNumberPersonSupport();
    },

    methods: {
        async getAuthor() {
            const res = await UserService.getbyId(this.$route.params.id);
            if (!res.error) {
                this.author = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                    return;
                }
                ElMessage.error("Get error");
            }
        },

        async getAllProjects() {
            const res = await ProjectService.getProjectOwner(this.$route.params.id);
            if (!res.error) {
                this.listProjects = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },

        async getNumberPersonSupport() {
            const res = await TransactionService.getNumberOfSupport(this.$route.params.id);
            console.log(res);
            // if(!res.error) {

            // }
        },

        isOwner() {
            return this.user.currentUser.id === this.author.id;
        },
    },
};
</script>

<style lang="scss" scoped>
.content {
    --cs-post-area-align-content: flex-start;
    --cs-post-area-content-padding: 0px;
    --cs-post-area-content-border-radius: 0;
    --cs-post-area-content-background: 0 0;
    --cs-post-area-content-border: 0px;
    --cs-post-area-align-image: stretch;
    font-size: var(--cs-font-post-content-size);
    .page-header {
        margin-bottom: 3rem;
        .page__author {
            display: flex;
            flex-direction: column;
            .edit-button {
                display: flex;
                margin-right: 0.55rem;
                justify-content: flex-end;
                i {
                    transition: all 0.1s;
                    cursor: pointer;
                    font-size: 1.3rem;
                    &:hover {
                        scale: 1.3;
                    }
                }
            }
            .page__author-photo {
                .author-thumbnail {
                    overflow: hidden;
                    transition: 0.25s;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    img {
                        display: block;
                        max-width: 100px;
                        width: auto;
                        // height: 100%;
                        width: 100px;
                        height: 100px;
                        -o-object-fit: cover;
                        object-fit: cover;
                        -o-object-position: center;
                        object-position: center;
                        border-radius: var(--cs-secondary-border-radius);
                    }
                }
            }

            .page__author-info {
                // margin-top: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                flex: 1;
                text-align: center;
                .author-infor-title {
                    word-wrap: break-word;
                    font-family: var(--cs-font-headings-family), sans-serif;
                    font-weight: var(--cs-font-headings-weight);
                    text-transform: var(--cs-font-headings-text-transform);
                    line-height: var(--cs-font-headings-line-height);
                    letter-spacing: var(--cs-font-headings-letter-spacing);
                }
                .page__archive-count {
                    font-family: var(--cs-font-secondary-family), sans-serif;
                    font-size: var(--cs-font-secondary-size);
                    font-weight: var(--cs-font-secondary-weight);
                    font-style: var(--cs-font-secondary-style);
                    letter-spacing: var(--cs-font-secondary-letter-spacing);
                    text-transform: var(--cs-font-secondary-text-transform);
                    color: var(--cs-color-accent);
                }

                .author-infor-contact {
                    margin-top: 1rem;
                    margin-bottom: 2rem;
                    .contact-wrap {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding-left: 0;
                        width: 100%;
                        li {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            flex: 0 0 auto;
                            width: 33.33333333%;
                            a {
                                align-items: center;
                                color: #576d9b;
                                display: flex;
                                padding-left: 0.5rem;
                                padding-right: 0.5rem;
                                .contact-icon-section {
                                    align-items: center;
                                    display: flex;
                                    justify-content: center;
                                    padding-left: 0.5rem;
                                    padding-right: 0.5rem;
                                    div {
                                        height: 27px;
                                        padding: 10px;
                                        width: 27px;
                                        align-items: center;
                                        background: #576d9b;
                                        border-radius: 100%;
                                        display: flex;
                                        justify-content: center;
                                        i {
                                            color: whitesmoke;
                                        }
                                    }
                                }
                                .contact-info-section {
                                    display: flex;
                                    flex-direction: column;
                                    word-wrap: break-word !important;
                                    word-break: break-word !important;
                                    align-items: flex-start !important;
                                    .key {
                                        font-size: 16px;
                                        font-weight: 700;
                                    }
                                    .value {
                                        font-size: 14px;
                                    }
                                }
                            }
                        }
                    }
                }
                .line-section {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    hr {
                        background: #647887;
                        height: 1px;
                        opacity: 0.2;
                        width: 40%;
                        margin-bottom: 2rem;
                    }
                }

                .page__archive-description {
                    margin-top: 1rem;
                    color: #647887;
                }
            }
        }
    }
    .page-projects-area {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        gap: 2rem;
        width: 100%;

        .filter-group {
            display: flex;
            justify-content: center;
            align-items: center;
            .finished {
                :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
                    background-color: rgb(103, 194, 58) !important;
                    border-color: rgb(103, 194, 58) !important;
                    box-shadow: -1px 0 0 0 rgb(103, 194, 58) !important;
                }
                :deep(.el-radio-button__inner:hover) {
                    color: rgb(108, 231, 126);
                }
            }
            .inactive {
                :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
                    background-color: rgb(245, 108, 108) !important;
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
            display: inline-flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 4rem;
        }
    }
}
</style>
