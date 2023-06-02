<template>
    <div class="container">
        <AppToolbar :title="title_page"></AppToolbar>
        <div class="main-container">
            <div class="project-form">
                <el-form
                    label-width="140px"
                    label-position="left"
                    :model="projectForm"
                    :rules="projectFromRules"
                    ref="form"
                >
                    <el-form-item label="Pictures" prop="image_url">
                        <!-- <el-upload
                            v-model:file-list="fileList"
                            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                            list-type="picture-card"
                            :on-preview="handlePictureCardPreview"
                            :on-remove="handleRemove"
                            limit="2"
                        >
                            <el-icon><Plus /></el-icon>
                        </el-upload> -->
                        <el-upload
                            class="avatar-uploader"
                            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                            :show-file-list="false"
                        >
                            <img
                                v-if="projectForm.image_url"
                                :src="projectForm.image_url"
                                class="avatar"
                            />
                            <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                        </el-upload>
                    </el-form-item>
                    <el-form-item label="Title" prop="title">
                        <el-input v-model="projectForm.title"></el-input>
                    </el-form-item>
                    <el-form-item label="Category" prop="type_projects">
                        <el-select
                            v-model="projectForm.type_projects"
                            multiple
                            filterable
                            allow-create
                            default-first-option
                            :reserve-keyword="false"
                            placeholder="Please select category"
                        >
                            <el-option
                                v-for="item in listTypeProject"
                                :key="item.id"
                                :label="item.name"
                                :value="item.id"
                            />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Fund goal" prop="fund_goal">
                        <el-input-number
                            v-model="projectForm.fund_goal"
                            :step="1000"
                            :min="10000"
                        />
                    </el-form-item>
                    <el-form-item label="Summary" prop="summary">
                        <el-input v-model="projectForm.summary"></el-input>
                    </el-form-item>
                    <el-form-item label="Description" prop="description">
                        <el-input v-model="projectForm.description" type="textarea" />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="handleCreateProject">Create</el-button>
                        <el-button>Cancel</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import AppToolbar from "@/components/AppToolbar.vue";
import ProjectService from "@/services/project/ProjectService";
import TypeService from "@/services/project/TypeService";
export default {
    name: "create-project",
    props: {
        title_page: {
            type: String,
            default: "Create New Project",
        },
    },
    components: {
        AppToolbar,
    },
    data() {
        return {
            listTypeProject: [],
            fileList: [],
            dialogImageUrl: "",
            dialogVisible: false,
            projectForm: {
                title: "Chung tay hỗ trợ học bổng cho 12 em học sinh nghèo",
                image_url: "https://givenow.vn/wp-content/uploads/2023/03/Cover-2-800x600.png",
                summary: "Chung tay hỗ trợ học bổng cho 12 em học sinh nghèo",
                description: "Chung tay hỗ trợ học bổng cho 12 em học sinh nghèo",
                fund_goal: 333333,
                type_projects: ["60bf7f49-96dd-44de-b809-624c409f92c6"],
            },
            projectFromRules: {
                title: [{ required: true, message: "Title is required", trigger: "blur" }],
                image_url: [{ required: true, message: "Image is required", trigger: "blur" }],
                summary: [{ required: true, message: "Summary is required", trigger: "blur" }],
                description: [
                    { required: true, message: "Description is required", trigger: "blur" },
                ],
                type_projects: [
                    { required: true, message: "Category is required", trigger: "blur" },
                ],
                fund_goal: [{ required: true, message: "Fund goal is required", trigger: "blur" }],
            },
        };
    },
    async created() {
        this.listTypeProject = (await TypeService.getAll()).data.results;
        console.log(this.listTypeProject);
    },
    methods: {
        handleRemove(uploadFile, uploadFiles) {
            console.log(uploadFile, uploadFiles);
        },
        handlePictureCardPreview(uploadFile) {
            this.dialogImageUrl = uploadFile.url;
            this.dialogVisible = true;
        },
        handleCreateProject: async function () {
            await this.$refs.form.validate((valid) => {
                if (valid) {
                    console.log(valid);
                    console.log(this.projectForm);
                }
            });
            const res = await ProjectService.create(this.projectForm);
            console.log(res);
        },
    },
};
</script>

<style scoped lang="scss">
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.main-container {
    padding: var(--cs-main-panel-pading);
}

.project-form {
    width: 75%;
}

.avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
}

.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    text-align: center;
}
</style>
