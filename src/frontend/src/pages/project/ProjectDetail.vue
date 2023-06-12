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
                                <img :src="project.author.avatar" />
                                <a href="#">{{ project.author.full_name }}</a>
                            </div>
                            <div class="project-giver-number">
                                <div class="bx bx-donate-blood"></div>
                                100
                            </div>
                        </div>
                        <div class="project-goal">
                            <span>Project objectives</span>
                            <span>{{ project.fund_goal }}</span>
                        </div>
                        <div class="project-fund-raised">
                            <div class="neo-progressbar">
                                <div></div>
                            </div>
                            <div class="fund-raised-number">
                                <span>Achieved</span>
                                <span>{{ project.fund_total }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-form-donation">
                        <el-input-number
                            v-model="transactionForm.amount"
                            :min="10000"
                            :step="1000"
                            controls-position="right"
                            size="large"
                        />
                        <el-button @click="checkoutVisible = true" type="primary" size="large">
                            Support now
                        </el-button>
                    </div>
                </div>
            </div>
        </div>

        <el-tabs type="border-card" class="demo-tabs">
            <el-tab-pane label="Content" :lazy="true">
                <div class="project-content" v-html="project.description"></div>
            </el-tab-pane>
            <el-tab-pane label="List of supporters" :lazy="true">
                <el-table
                    :data="transactions"
                    style="width: 100%"
                    height="300"
                    :default-sort="{ prop: 'created_at', order: 'descending' }"
                >
                    <el-table-column fixed label="Date" prop="created_at" sortable>
                        <template #default="scope">
                            <span>{{ new Date(scope.row.created_at).toLocaleDateString() }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="supporter.full_name" label="Name" />
                    <el-table-column prop="amount" label="Amount" />
                    <el-table-column prop="description" label="Message" />
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="Comment">Comment</el-tab-pane>
        </el-tabs>

        <!--                    Check out dialog                       -->
        <el-dialog v-model="checkoutVisible" title="Checkout" width="350px" draggable>
            <el-form label-position="left" style="max-width: 460px">
                <el-space fill>
                    <!-- <el-form-item label="Supporter's name" label-position="top">
                        <el-input v-model="transactionForm.full_name" />
                    </el-form-item> -->

                    <el-form-item label="Amount of support">
                        <el-input-number
                            v-model="transactionForm.amount"
                            :min="10000"
                            :step="1000"
                            controls-position="right"
                            size="large"
                        />
                    </el-form-item>
                    <el-checkbox
                        v-model="transactionForm.is_anonymous"
                        label="I want to support anonymously"
                        size="large"
                    />
                </el-space>
                <!-- <el-space fill>
                    <el-form-item label="Your Information">
                        <el-row :gutter="20">
                            <el-col :span="12">
                                <el-input
                                    v-model="formAccessibility.firstName"
                                    label="First Name"
                                    placeholder="First Name"
                                />
                            </el-col>
                            <el-col :span="12">
                                <el-input
                                    v-model="formAccessibility.lastName"
                                    label="Last Name"
                                    placeholder="Last Name"
                                />
                            </el-col>
                        </el-row>
                    </el-form-item>
                </el-space> -->
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="checkoutVisible = false">Cancel</el-button>
                    <el-button type="primary" @click="checkoutVisible = false"> Confirm </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import { mapState } from "vuex";
import TransactionService from "@/services/project/TransactionService";
import ProjectService from "@/services/project/ProjectService";
export default {
    name: "project-detail",
    data() {
        return {
            project: {
                author: {},
            },
            transactions: [],
            checkoutVisible: false,
            transactionForm: {
                full_name: "",
                phone_number: "",
                address: "",
                email: "",
                is_anonymous: false,
                amount: 0,
                description: "",
            },
        };
    },
    computed: {
        ...mapState(["user"]),
    },
    mounted() {
        console.log(this.$route.params.id);
    },
    async created() {
        this.project = (await ProjectService.getbyId(this.$route.params.id)).data;
        console.log(this.project);
        this.transactions = (
            await TransactionService.getAllOfProject(this.project.id, "INCREASE")
        ).data;
        console.log(this.transactions);
    },
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
