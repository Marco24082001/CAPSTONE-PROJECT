<template>
    <div class="container">
        <AppToolbar>
            <template #content>
                <el-breadcrumb :separator-icon="ArrowRight">
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>
                    <el-breadcrumb-item
                        ><router-link to="/projects">Project</router-link></el-breadcrumb-item
                    >
                    <el-breadcrumb-item>Detail </el-breadcrumb-item>
                </el-breadcrumb>
            </template>
        </AppToolbar>
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
                                {{ transactions.length }}
                            </div>
                        </div>
                        <div class="project-goal">
                            <span>Project objectives</span>
                            <span>{{ project.fund_goal }}</span>
                        </div>
                        <div class="project-fund-raised">
                            <div class="neo-progressbar">
                                <div v-bind:style="{ width: project.percent + '%' }"></div>
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
                            :min="1"
                            :step="1"
                            controls-position="right"
                            size="large"
                        />

                        <el-button
                            v-if="project.status == 'ACTIVE'"
                            @click="checkoutVisible = true"
                            type="primary"
                            size="large"
                        >
                            Support now
                        </el-button>
                        <el-button v-else type="primary" size="large" disabled
                            >Support now</el-button
                        >
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
                    :data="resultQuery"
                    style="width: 100%"
                    height="300"
                    :default-sort="{ prop: 'created_at', order: 'descending' }"
                >
                    <el-table-column fixed label="Date" prop="created_at" sortable>
                        <template #default="scope">
                            <span>{{ new Date(scope.row.created_at).toLocaleDateString() }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="full_name" label="Name" />
                    <el-table-column prop="amount" label="Amount" />
                    <el-table-column prop="message" label="Message" />
                    <el-table-column align="right">
                        <template #header>
                            <el-input
                                v-model="searchQuery"
                                size="small"
                                placeholder="Search name"
                            />
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <!-- <el-tab-pane label="Comment">Comment</el-tab-pane> -->
        </el-tabs>

        <!--                    Check out dialog                       -->
        <el-dialog
            v-model="checkoutVisible"
            class="checkout-dialog"
            title="Checkout"
            width="370px"
            draggable
        >
            <el-form label-position="left" style="max-width: 460px" label-width="130px">
                <el-space fill>
                    <el-form-item
                        v-if="user.currentUser.full_name == null"
                        label="Supporter's name"
                    >
                        <el-input v-model="transactionForm.full_name" />
                    </el-form-item>
                    <el-form-item label="Message">
                        <el-input v-model="transactionForm.message" />
                    </el-form-item>

                    <el-form-item label="Amount of support">
                        <el-input-number
                            v-model="transactionForm.amount"
                            :min="1"
                            :step="1"
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
            </el-form>
            <div class="footer-dialog">
                <PaypalButton
                    :amount="transactionForm.amount"
                    :message="transactionForm.message"
                    @execute-transaction="executeTransaction"
                ></PaypalButton>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import { mapState } from "vuex";
import TransactionService from "@/services/project/TransactionService";
import AppToolbar from "@/components/AppToolbar.vue";

import ProjectService from "@/services/project/ProjectService";
import PaypalButton from "@/components/checkout/PaypalButton.vue";
import { ElMessage } from "element-plus";
export default {
    name: "project-detail",
    components: {
        PaypalButton,
        AppToolbar,
    },
    data() {
        return {
            project: {
                author: {},
            },
            transactions: [],
            checkoutVisible: false,
            transactionForm: {
                project: "",
                full_name: "",
                phone_number: "",
                address: "",
                email: "",
                is_anonymous: false,
                amount: 0,
                message: "",
            },
            searchQuery: "",
        };
    },
    computed: {
        ...mapState(["user"]),
        resultQuery() {
            if (this.searchQuery != "") {
                return this.transactions.filter((item) => {
                    return item.full_name.toLowerCase().includes(this.searchQuery.toLowerCase());
                });
            } else {
                return this.transactions;
            }
        },
    },
    async created() {
        this.getProjectDetail()
        this.transactions = (
            await TransactionService.getAllOfProject(this.project.id, "INCREASE")
        ).data;
        console.log(this.transactions);
    },
    methods: {
        async getProjectDetail() {
            this.project = (await ProjectService.getbyId(this.$route.params.id)).data;
        },
        async executeTransaction() {
            this.transactionForm.project = this.project.id;
            this.$store.commit("decoration/setFullscreenLoading", true);
            const res = await TransactionService.create(this.transactionForm);
            this.$store.commit("decoration/setFullscreenLoading", false);
            if (res.status === 201) {
                this.transactions.push(res.data);
                ElMessage.success("Transaction Successful!");
                this.getProjectDetail();
            } else {
                ElMessage.error("transaction failed!");
            }
            this.checkoutVisible = false;
        },
    },
};
</script>

<style scoped lang="scss">
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--cs-main-panel-pading);
    gap: 2rem;

    .project-header {
        display: flex;
        width: 100%;
        gap: 2rem;
        .project-media {
            overflow: hidden;
            border-radius: 1.5rem;
            height: 18rem;
            flex: 46%;
            img {
                object-fit: cover;
                object-position: center center center;
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
                            overflow: hidden;
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

    :deep(.checkout-dialog) {
        .el-input-number {
            width: 100% !important;
        }
    }
}

@media (max-width: 800px) {
    .project-header {
        display: flex;
        flex-direction: column;
    }
}
</style>
