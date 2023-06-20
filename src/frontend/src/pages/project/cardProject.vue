<template>
    <div class="cp-project">
        <div class="image-project">
            <div class="tooltip" v-if="isManageProject">
                <div
                    ref="tooltip"
                    class="bx bx-dots-horizontal tooltip-icon"
                    @click="isToolOpen = !isToolOpen"
                ></div>
                <OnClickOutside @trigger="dropdownHandler">
                    <div class="tooltip-menu" :class="{ 'open-tooltip': isToolOpen }">
                        <router-link
                            class="tooltip-menu-item"
                            :to="{ name: 'OwnerProjectDetail', params: { id: project.id } }"
                        >
                            <div class="bx bx-detail tooltip-menu-icon"></div>
                            View Detail</router-link
                        >
                        <router-link
                            class="tooltip-menu-item"
                            :to="{ name: 'EditProject', params: { id: project.id } }"
                            ><div class="bx bx-edit tooltip-menu-icon"></div>
                            Edit</router-link
                        >
                        <div
                            v-if="project.status == 'ACTIVE'"
                            class="tooltip-menu-item"
                            @click="deactivate"
                        >
                            <div class="bx bx-trash tooltip-menu-icon"></div>
                            <p>Deactivate</p>
                        </div>
                        <div
                            v-else-if="project.status == 'INACTIVE'"
                            class="tooltip-menu-item"
                            @click="activate"
                        >
                            <div class="bx bx-bolt-circle tooltip-menu-icon"></div>
                            <p>Activate</p>
                        </div>
                    </div>
                </OnClickOutside>
            </div>
            <router-link
                :to="{ name: 'Projectdetail', params: { id: project.id } }"
                class="image-index"
            >
                <img :src="project.image_url" alt="" />
            </router-link>
        </div>

        <div class="cp-content">
            <div class="cp-meta">
                <a href="/#" v-for="type_project in project.list_types" :key="type_project.id">
                    {{ type_project.name }}</a
                >
            </div>
            <h2 class="cp-title">
                <a
                    href="https://givenow.vn/du-an/chung-tay-cham-soc-suc-khoe-cho-200-tre-nhap-cu-tai-truong-tinh-thuong-ai-linh/"
                    >{{ project.title }}</a
                >
            </h2>
            <div class="cp-progressbar">
                <div class="neo-progressbar">
                    <div v-bind:style="{ width: project.percent + '%' }"></div>
                </div>
                <div class="fund-raised">
                    <div class="fund-raised-txt">{{ project.fund_total }} đ</div>
                    <div class="fund-raised-percent">{{ project.percent }}%</div>
                </div>
            </div>
            <!-- <span>$ 15.99</span> -->
            <div class="cp-details">
                <div class="cp-details-data">
                    <a class="cp-author-avatar" href="#">
                        <img :src="project.author.avatar" />
                    </a>
                    <div class="cp-details-meta">
                        <div class="cp-author-meta">
                            <a href="/#">{{ project.author.full_name }}</a>
                        </div>
                        <div class="cp-post-meta">
                            <div class="cp-meta-date">
                                {{ new Date(project.created_at).toLocaleDateString() }}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="cp-fund-goal">
                    <span>{{ project.fund_goal }} $</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { OnClickOutside } from "@vueuse/components";
import ProjectService from "@/services/project/ProjectService";
import { ElMessage } from "element-plus";
export default {
    name: "card-project",
    components: {
        OnClickOutside,
    },
    props: {
        project_img: {
            type: String,
        },
        author_img: {
            type: String,
        },
        isManageProject: {
            type: Boolean,
            default: false,
        },
        project: {
            type: Object,
            default: () => {
                return {};
            },
        },
    },
    data() {
        return {
            isToolOpen: false,
        };
    },
    methods: {
        toggleToolTip() {
            this.isToolOpen = !this.isToolOpen;
        },
        async deactivate() {
            const res = await ProjectService.deactivate(this.project.id);
            if (res.status === 200) {
                ElMessage.success("Deactivate Successful!");
            } else {
                ElMessage.error("Deactivate failed!");
            }
            console.log(res);
        },

        async activate() {
            const res = await ProjectService.activate(this.project.id);
            if (res.status === 200) {
                ElMessage.success("Activate Successful!");
            } else {
                ElMessage.error("Activate failed!");
            }
            console.log(res);
        },

        dropdownHandler(event) {
            if (event.target !== this.$refs.tooltip) {
                this.isToolOpen = false;
            }
        },
    },
};
</script>
<style scoped lang="scss">
.cp-project {
    position: relative;
    // background-color: var(--sectionBack);
    background-color: white;
    width: 20rem;
    display: flex;
    flex-direction: column;
    height: 100%;
    transition: 0.3s;
    &:hover {
        box-shadow: var(--cs-box-shadow-menu);
    }
    .image-project {
        flex: 1;
        display: flex;
        flex-direction: column;
        .tooltip {
            width: 100%;
            position: absolute;
            display: flex;
            background-color: rgba(0, 0, 0, 0.367);
            height: 3rem;
            align-items: center;
            // justify-content: center;
            opacity: 0;
            transition: 0.4s ease;
            z-index: 1;
            .tooltip-icon {
                position: absolute;
                font-size: 1.4rem;
                right: 1.1rem;
                color: #d1cdcd;
                cursor: pointer;
            }

            .tooltip-menu {
                position: absolute;
                padding: 0.5rem 0;
                top: 100%;
                right: 0rem;
                width: 105px;
                max-height: 0px;
                opacity: 0;
                overflow: hidden;
                transition: all 0.5s;
                background-color: var(--cs-color-submenu-background);
                box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.1);
                .tooltip-menu-item {
                    display: flex;
                    align-items: center;
                    text-decoration: none;
                    color: var(--cs-color-primary);
                    background-color: transparent;
                    margin: 0.2rem 0;
                    font-size: var(--cs-font-submenu-size);
                    font-weight: var(--cs-font-submenu-weight);
                    font-style: var(--cs-font-submenu-style);
                    letter-spacing: var(--cs-font-submenu-letter-spacing);
                    text-transform: var(--cs-font-submenu-text-transform);
                    cursor: pointer;
                    transition: transform 0.5s;
                    .tooltip-menu-icon {
                        border-radius: 50%;
                        margin-right: 10px;
                        padding: 5px;
                    }

                    &:hover {
                        color: var(--cs-color-secondary);
                    }
                }
                &.open-tooltip {
                    opacity: 1;
                    max-height: 400px;
                }
            }
        }
        &:hover > .tooltip {
            opacity: 1;
        }
    }
    .image-index {
        display: grid;
        overflow: hidden;
        width: 100%;
        height: 100%;
        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center center center;
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-transition: 0.3s ease-in-out;
            transition: 0.3s ease-in-out;
        }
        &:hover img {
            -webkit-transform: scale(1.2);
            transform: scale(1.2);
        }
    }
    .cp-content {
        // flex: 1;
        margin-top: 1.2rem;
        width: 100%;
        .cp-meta {
            font-family: var(--cs-font-category-family), sans-serif;
            font-size: var(--cs-font-category-size);
            font-weight: var(--cs-font-category-weight);
            font-style: var(--cs-font-category-style);
            letter-spacing: var(--cs-font-category-letter-spacing);
            text-transform: var(--cs-font-category-text-transform);
            a {
                color: var(--cs-color-category);
                transition: 0.25s;
                &:hover {
                    color: var(--cs-color-category-hover);
                }
            }
        }
        .cp-title {
            font-family: var(--cs-font-headings-family), sans-serif;
            font-weight: var(--cs-font-headings-weight);
            text-transform: var(--cs-font-headings-text-transform);
            line-height: var(--cs-font-headings-line-height);
            letter-spacing: var(--cs-font-headings-letter-spacing);
            font-size: 1.25rem;
            margin-top: 0.5rem;
            a {
                display: block;
                text-decoration: none;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                color: var(--cs-color-title, var(--cs-color-primary));
                transition: 0.25s;
                &:hover {
                    color: var(--cs-color-title-hover, var(--cs-color-secondary));
                }
            }
        }
        .cp-progressbar {
            padding: 0px;
            margin: 10px 0px 0px 0px;
            .neo-progressbar {
                border-radius: 6px;
                background-color: #ff2e5b1a;
                overflow: hidden;
                div {
                    height: 0.4rem;
                    border-radius: 6px;
                    background-color: #ff2e5b;
                    z-index: 11111;
                }
            }
            .fund-raised {
                margin-top: 0.5rem;
                display: flex;
                justify-content: space-between;
            }
        }
        .cp-details {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            width: 100%;
            margin-top: 0.5rem;
            .cp-details-data {
                display: flex;
                align-items: center;
                flex-wrap: wrap;
                .cp-author-avatar {
                    width: 40px;
                    border-radius: 50%;
                    // overflow: hidden;
                    img {
                        border-radius: 50%;
                        object-position: center;
                        object-fit: cover;
                        width: 40px;
                        height: 40px;
                    }
                }
                .cp-details-meta {
                    margin-left: 0.3rem;
                    display: flex;
                    flex-direction: column;
                    flex-wrap: wrap;
                    flex: 1;
                    font-family: var(--cs-font-post-meta-family), sans-serif;
                    font-size: var(--cs-font-post-meta-size);
                    font-weight: var(--cs-font-post-meta-weight);
                    font-style: var(--cs-font-post-meta-style);
                    letter-spacing: var(--cs-font-post-meta-letter-spacing);
                    text-transform: var(--cs-font-post-meta-text-transform);
                    .cp-author-meta a {
                        font-weight: 500;
                        text-transform: capitalize;
                        color: var(--cs-color-meta-links, var(--cs-color-primary));
                        &:hover {
                            color: var(--cs-color-meta-links-hover, var(--cs-color-secondary));
                        }
                    }
                    .cp-post-meta {
                        display: flex;
                        align-items: center;
                        flex-wrap: wrap;
                        transition: 0.25s;
                        color: var(--cs-color-meta);
                        font-family: var(--cs-font-post-meta-family), sans-serif;
                        font-size: var(--cs-font-post-meta-size);
                        font-weight: var(--cs-font-post-meta-weight);
                        font-style: var(--cs-font-post-meta-style);
                        letter-spacing: var(--cs-font-post-meta-letter-spacing);
                        text-transform: var(--cs-font-post-meta-text-transform);
                    }
                }
            }

            .cp-fund-goal {
                span {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    text-decoration: none;
                    border: none;
                    border-radius: var(--cs-primary-border-radius);
                    transition: 0.25s;
                    box-shadow: none;
                    cursor: pointer;
                    padding: 0.75rem 1.5rem;
                    border-radius: var(--cs-primary-border-radius);
                    --cs-color-style-contrast: var(--cs-color-button);
                    --cs-color-style-border: var(--cs-color-contrast-200);
                    --cs-color-style-hover: var(--cs-color-button);
                    --cs-color-style-hover-contrast: var(--cs-color-button-contrast);
                    --cs-color-style-hover-border: var(--cs-color-button);
                    border: 1px solid var(--cs-color-style-border);
                    background-color: var(--cs-color-style);
                    color: var(--cs-color-style-contrast);
                    font-family: var(--cs-font-primary-family), sans-serif;
                    font-size: var(--cs-font-primary-size);
                    font-weight: var(--cs-font-primary-weight);
                    font-style: var(--cs-font-primary-style);
                    letter-spacing: var(--cs-font-primary-letter-spacing);
                    text-transform: var(--cs-font-primary-text-transform);
                    &:hover {
                        border: 1px solid var(--cs-color-style-hover-border);
                        background-color: var(--cs-color-style-hover);
                        color: var(--cs-color-style-hover-contrast);
                    }
                }
            }
        }
    }
}
</style>
