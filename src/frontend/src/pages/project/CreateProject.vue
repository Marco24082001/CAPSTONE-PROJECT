<template>
    <div class="container">
        <AppToolbar>
            <template #content>
                <el-breadcrumb>
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>
                    <el-breadcrumb-item
                        ><router-link to="/dashboard/projects"
                            >Project</router-link
                        ></el-breadcrumb-item
                    >
                    <el-breadcrumb-item>Create Project</el-breadcrumb-item>
                </el-breadcrumb>
            </template>
        </AppToolbar>
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
                        <el-upload
                            class="avatar-uploader"
                            action="http://localhost:8000/api/v1/api_project/projects/upload_image/"
                            :show-file-list="false"
                            :on-success="handleAvatarSuccess"
                            :before-upload="beforeAvatarUpload"
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
                                v-for="item in listTypes"
                                :key="item.id"
                                :label="item.name"
                                :value="item.id"
                            />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Fund goal" prop="fund_goal">
                        <el-input-number v-model="projectForm.fund_goal" :step="1" :min="1" />
                    </el-form-item>
                    <el-form-item label="Summary" prop="summary">
                        <el-input v-model="projectForm.summary"></el-input>
                    </el-form-item>
                    <el-form-item label="Description" prop="description">
                        <TextEditor
                            :initial_content="projectForm.description"
                            @input-description="updateDescription"
                        />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="handleCreateProject">Create</el-button>
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
import { ElMessage } from "element-plus";
import { uploadImage } from "@/utils/cloudinaryUtils";
import TextEditor from "@/components/TextEditor.vue";

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
        TextEditor,
    },
    data() {
        return {
            listTypes: [],
            fileList: [],
            dialogImageUrl: "",
            dialogVisible: false,
            rawFileImage: "",
            projectForm: {
                title: "",
                image_url: "",
                summary: "",
                description: "",
                fund_goal: 1,
                type_projects: [],
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
        this.getAllTypes();
    },
    methods: {
        async getAllTypes() {
            const res = await TypeService.getAll();
            if (!res.error) {
                this.listTypes = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },
        handlePictureCardPreview(uploadFile) {
            this.dialogImageUrl = uploadFile.url;
            this.dialogVisible = true;
        },
        handleCreateProject: async function () {
            await this.$refs.form.validate(async (valid) => {
                if (valid) {
                    this.$store.commit("decoration/setFullscreenLoading", true);
                    if (this.rawFileImage !== "") {
                        try {
                            const { url } = await uploadImage(this.rawFileImage);
                            this.projectForm.image_url = url;
                        } catch (error) {
                            this.$store.commit("decoration/setFullscreenLoading", false);
                            ElMessage.error("Upload image fail!");
                            return;
                        }
                    }
                    const res = await ProjectService.create(this.projectForm);
                    this.$store.commit("decoration/setFullscreenLoading", false);
                    if (res.status == 201) {
                        this.$router.push({
                            name: "Projectdetail",
                            params: { id: res.data.id },
                        });
                    } else {
                        ElMessage.error("Create project fail!");
                    }
                }
            });
        },
        handleAvatarSuccess: async function (response, uploadFile) {
            this.projectForm.image_url = URL.createObjectURL(uploadFile.raw);
            this.rawFileImage = uploadFile.raw;
        },
        beforeAvatarUpload: function (rawFile) {
            if (rawFile.type !== "image/jpeg" && rawFile.type !== "image/png") {
                ElMessage.error("Avatar picture must be JPG|PNG format!");
                return false;
            } else if (rawFile.size / 1024 / 1024 > 5) {
                ElMessage.error("Avatar picture size can not exceed 2MB!");
                return false;
            }
            return true;
        },
        updateDescription: function (value) {
            this.projectForm.description = value;
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
    gap: 2rem;
    padding: var(--cs-main-panel-pading);
}

.main-container {
    padding: var(--cs-main-panel-pading);
}

.project-form {
    width: 100%;
}

.avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
}

.avatar-uploader {
    :deep(.el-upload) {
        border: 1px dashed var(--el-border-color);
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: var(--el-transition-duration-fast);
    }
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
