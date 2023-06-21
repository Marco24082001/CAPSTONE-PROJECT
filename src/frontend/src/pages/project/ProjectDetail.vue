<template>
    <div class="container">
        <AppToolbar>
            <template #content>
                <el-breadcrumb>
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
                            <div class="fund-raised-number">
                                <span>Amount spent </span>
                                <span>{{ project.fund_used }}</span>
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
            <el-tab-pane label="Report" @click="getAllReports">
                <div class="report-form-container" v-if="isOwner()">
                    <el-tooltip
                        :content="isOpenReportForm ? 'Close report' : 'Make a report'"
                        placement="top"
                        effect="dark"
                    >
                        <el-button type="info" @click="toogleReport"
                            ><i
                                class="bx"
                                :class="isOpenReportForm ? 'bx-chevrons-up' : 'bx-chevrons-down'"
                            ></i
                        ></el-button>
                    </el-tooltip>
                    <div class="report-form" :class="{ close: !isOpenReportForm }">
                        <el-form
                            label-width="140px"
                            label-position="left"
                            :model="reportForm"
                            :rules="reportFormRules"
                            ref="form"
                        >
                            <el-form-item label="Title" prop="title">
                                <el-input v-model="reportForm.title"></el-input>
                            </el-form-item>
                            <el-form-item label="Amount spent" prop="amount">
                                <el-input-number v-model="reportForm.amount" :step="1" :min="0" />
                            </el-form-item>
                            <el-form-item label="Description" prop="description">
                                <!-- <el-input v-model="projectForm.description" type="textarea" /> -->
                                <TextEditor
                                    :initial_content="reportForm.description"
                                    @input-description="updateDescription"
                                />
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="handleCreateReport"
                                    >Create</el-button
                                >
                            </el-form-item>
                        </el-form>
                    </div>
                </div>
                <el-timeline>
                    <el-timeline-item
                        v-for="report in reports"
                        :key="report.id"
                        :timestamp="new Date(report.created_at).toLocaleDateString()"
                        placement="top"
                    >
                        <el-card>
                            <h4>{{ report.title }}</h4>
                            <div v-html="report.description"></div>
                            <p class="report-spent">Spent: {{ report.amount }} $</p>
                        </el-card>
                    </el-timeline-item>
                </el-timeline></el-tab-pane
            >
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
                            :min="0"
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
import TextEditor from "@/components/TextEditor.vue";
import ProjectService from "@/services/project/ProjectService";
import ReportService from "@/services/project/ReportService";
import PaypalButton from "@/components/checkout/PaypalButton.vue";
import { ElMessage } from "element-plus";
export default {
    name: "project-detail",
    components: {
        PaypalButton,
        TextEditor,
        AppToolbar,
    },
    data() {
        return {
            project: {
                author: {},
            },
            reports: [],
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
            reportForm: {
                project: "",
                amount: 0,
                description: "",
            },
            reportFormRules: {
                title: [{ required: true, message: "Title is required", trigger: "blur" }],
                description: [
                    { required: true, message: "Description is required", trigger: "blur" },
                ],
                amount: [{ required: true, message: "Amount is required", trigger: "blur" }],
            },
            searchQuery: "",
            isOpenReportForm: false,
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
        this.getProjectDetail();
        this.getAllTransactions();
        this.getAllReports();
    },
    methods: {
        async getProjectDetail() {
            const res = await ProjectService.getbyId(this.$route.params.id);
            if (!res.error) {
                this.project = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },

        async getAllTransactions() {
            const res = await TransactionService.getAllOfProject(this.project.id, "INCREASE");
            if (!res.error) {
                this.transactions = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },

        async getAllReports() {
            const res = await ReportService.getReports(this.project.id);
            if (!res.error) {
                this.reports = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
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
                ElMessage.error("Transaction failed!");
            }
            this.checkoutVisible = false;
        },

        updateDescription: function (value) {
            this.reportForm.description = value;
        },

        async handleCreateReport() {
            this.reportForm.project = this.project.id;
            await this.$refs.form.validate(async (valid) => {
                if (valid) {
                    this.$store.commit("decoration/setFullscreenLoading", true);
                    const res = await ReportService.create(this.reportForm);
                    this.$store.commit("decoration/setFullscreenLoading", false);
                    if (res.status == 201) {
                        console.log(res);
                        ElMessage.success("Create Report Successful!");
                        this.reports.unshift(res.data);
                        this.closeReportForm();
                    } else {
                        ElMessage.error("Create Report failed!");
                    }
                }
            });
        },

        closeReportForm() {
            this.isOpenReportForm = false;
            this.reportForm = { project: "", amount: 0, description: "" };
        },

        toogleReport() {
            this.isOpenReportForm = !this.isOpenReportForm;
        },

        isOwner() {
            return this.user.currentUser.id === this.project.user;
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

    .report-form-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        margin: 1rem;
        flex-direction: column;
        .report-form {
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.12);
            padding-top: 20px;
            padding-bottom: 5px;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            transition: all 0.3s ease-in-out;
            max-height: 700px;
            :deep(form) {
                width: 90%;
                .ql-container {
                    // min-height: 250px;
                    max-height: 34vh !important;
                }
            }
            &.close {
                max-height: 0px;
                opacity: 0;
                padding: 0;
            }
        }
    }

    .report-spent {
        color: rgb(103, 194, 58);
    }
}

@media (max-width: 800px) {
    .project-header {
        display: flex;
        flex-direction: column;
    }
}
</style>
