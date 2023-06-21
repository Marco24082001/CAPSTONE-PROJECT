<template>
    <div class="container">
        <AppToolbar>
            <template #content>
                <el-breadcrumb>
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>
                    <el-breadcrumb-item
                        ><router-link to="/dashboard/types">Type</router-link></el-breadcrumb-item
                    >
                </el-breadcrumb>
            </template>
        </AppToolbar>
        <div class="row">
            <div class="col-24">
                <el-table :data="resultQuery" style="width: 100%" max-height="50vh">
                    <el-table-column label="Name" prop="name" sortable />
                    <el-table-column label="Description" prop="description" />
                    <el-table-column align="right">
                        <template #header>
                            <el-input
                                v-model="searchQuery"
                                size="small"
                                placeholder="Type to search"
                            />
                        </template>
                        <template #default="scope">
                            <el-button
                                size="small"
                                @click="handleDialogEdit(scope.$index, scope.row)"
                                >Edit</el-button
                            >
                            <!-- <el-button
                                size="small"
                                type="info"
                                @click="handleHistory(scope.$index, scope.row)"
                                >History</el-button
                            > -->
                            <el-button
                                size="small"
                                type="danger"
                                @click="handleDelete(scope.$index, scope.row)"
                                >Delete</el-button
                            >
                        </template>
                    </el-table-column>
                </el-table>
                <el-button class="mt-4" style="width: 100%" @click="handleDialogCreate"
                    >Add Type</el-button
                >
            </div>
        </div>
        <el-dialog v-model="dialogFormVisible" title="Type Dialog" width="50vw">
            <el-form
                class="login-form"
                label-position="left"
                label-width="7rem"
                :model="typeForm"
                :rules="rules"
                ref="form"
            >
                <el-form-item prop="name" label="Type's name">
                    <el-input v-model="typeForm.name" placeholder="Input name"> </el-input>
                </el-form-item>
                <el-form-item prop="description" label="Description">
                    <el-input v-model="typeForm.description" placeholder="Input description">
                    </el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button
                        v-if="dialogFormStatus === 'create'"
                        @click="handleCreate"
                        type="primary"
                        >Create</el-button
                    >
                    <el-button v-else @click="handleEdit" type="primary">Edit</el-button>
                    <el-button @click="dialogFormVisible = false">Cancel</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import AppToolbar from "@/components/AppToolbar.vue";
import TypeService from "@/services/project/TypeService";
import { ElMessage } from "element-plus";
export default {
    name: "type-project",
    components: {
        AppToolbar,
    },
    data() {
        return {
            searchQuery: "",
            typeProjects: [],
            positionHistory: [],

            dialogFormVisible: false,
            dialogFormStatus: "create",
            dialogHistoryVisible: false,
            typeForm: {
                name: "",
                description: "",
            },
            editId: "",
            loading: false,
            rules: {
                name: [
                    {
                        required: true,
                        message: "Type's name is required",
                        trigger: "blur",
                    },
                ],
                description: [
                    {
                        required: true,
                        message: "Description is required",
                        trigger: "blur",
                    },
                ],
            },
        };
    },

    async created() {
        this.handleGetAll();
    },

    computed: {
        resultQuery() {
            if (this.searchQuery != "") {
                return this.typeProjects.filter((item) => {
                    return item.name.toLowerCase().includes(this.searchQuery.toLowerCase());
                });
            } else {
                return this.typeProjects;
            }
        },
    },

    methods: {
        resetModel: function () {
            this.typeForm.name = "";
            this.typeForm.description = "";
        },
        handleDialogCreate: function () {
            this.dialogFormStatus = "create";
            this.dialogFormVisible = true;
            this.resetModel();
        },
        handleDialogEdit: function (index, row) {
            this.dialogFormStatus = "edit";
            this.dialogFormVisible = true;
            this.editId = row.id;
            this.typeForm.name = row.name;
            this.typeForm.description = row.description;
        },

        handleGetAll: async function () {
            this.typeProjects = (await TypeService.getAll()).data;
        },

        handleCreate: async function () {
            let valid = await this.$refs.form.validate();
            if (!valid) {
                console.log("invalid");
                return;
            }
            this.$store.commit("decoration/setFullscreenLoading", true);
            const res = await TypeService.create(this.typeForm);
            this.$store.commit("decoration/setFullscreenLoading", false);
            if (res.status === 201) {
                this.handleGetAll();
                this.closedialogForm();
            }
        },
        handleEdit: async function () {
            let valid = await this.$refs.form.validate();
            if (!valid) {
                console.log("invalid");
                return;
            }
            this.$store.commit("decoration/setFullscreenLoading", true);
            const res = await TypeService.edit({ id: this.editId, ...this.typeForm });
            this.$store.commit("decoration/setFullscreenLoading", false);
            if (!res.data.error) {
                this.handleGetAll();
                this.closedialogForm();
            }
        },
        handleDelete: async function (index, row) {
            this.$store.commit("decoration/setFullscreenLoading", true);
            const res = await TypeService.delete(row.id);
            this.$store.commit("decoration/setFullscreenLoading", false);
            if (!res.error) {
                this.handleGetAll();
                ElMessage.success("Delete Successful!");
            } else {
                ElMessage.error(res.error.response.data.error);
            }
        },
        closedialogForm: function () {
            this.$refs.form.resetFields();
            this.dialogFormVisible = false;
        },
    },
};
</script>

<style>
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--cs-main-panel-pading);
    gap: 2rem;
}
</style>
