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
                >
                    <el-form-item label="Pictures">
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
                            :on-success="handleAvatarSuccess"
                            :before-upload="beforeAvatarUpload"
                        >
                            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                            <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                        </el-upload>
                    </el-form-item>
                    <el-form-item label="Title">
                        <el-input v-model="projectForm.title"></el-input>
                    </el-form-item>
                    <el-form-item label="Category">
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
                                v-for="item in default_type_projects"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Fund goal">
                        <el-input-number
                            v-model="projectForm.fund_goal"
                            :step="1000"
                            :min="10000"
                        />
                    </el-form-item>
                    <el-form-item label="Summary">
                        <el-input v-model="projectForm.summary"></el-input>
                    </el-form-item>
                    <el-form-item label="Description">
                        <el-input v-model="projectForm.description" type="textarea" />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary">Create</el-button>
                        <el-button>Cancel</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import AppToolbar from "@/components/AppToolbar.vue";

export default {
    name: "create-project",
    props: {
        title_page: {
            type: String,
            default: "Create New Project",
        },
        default_type_projects: {
            type: Array,
            default: () => {
                return [
                    {
                        label: "Cộng đồng",
                        value: "5605da24ecd44cfda2db85b3005ef693",
                    },
                    {
                        label: "Giáo dục",
                        value: "f1f9a8de6efa4fcea775816e45377688",
                    },
                    {
                        label: "Y tế",
                        value: "704cd15e0d13472a974661d730a80144",
                    },
                ];
            },
        },
    },
    components: {
        AppToolbar,
    },
    data() {
        return {
            fileList: [],
            dialogImageUrl: "",
            dialogVisible: false,
            projectForm: {
                title: "",
                image_url: "",
                summary: "",
                description: "",
                type_projects: [],
                fund_goal: 0,
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
    methods: {
        handleRemove(uploadFile, uploadFiles) {
            console.log(uploadFile, uploadFiles);
        },
        handlePictureCardPreview(uploadFile) {
            this.dialogImageUrl = uploadFile.url;
            this.dialogVisible = true;
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
