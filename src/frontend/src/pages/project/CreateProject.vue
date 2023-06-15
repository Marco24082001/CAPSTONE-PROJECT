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
                        <!-- <el-input v-model="projectForm.description" type="textarea" /> -->
                        <TextEditor
                            :initial_content="projectForm.description"
                            @input-description="updateDescription"
                        />
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
            listTypeProject: [],
            fileList: [],
            dialogImageUrl: "",
            dialogVisible: false,
            rawFileImage: "",
            projectForm: {
                title: "",
                image_url: "",
                summary: "",
                description: "",
                fund_goal: 100000,
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
        this.listTypeProject = (await TypeService.getAll()).data;
        console.log(this.listTypeProject);
        this.projectForm.type_projects.push(this.listTypeProject[0].id);
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
            await this.$refs.form.validate(async (valid) => {
                if (valid) {
                    console.log(this.projectForm);
                    if (this.rawFileImage !== "") {
                        try {
                            const { url } = await uploadImage(this.rawFileImage);
                            this.projectForm.image_url = url;
                        } catch (error) {
                            ElMessage.error("Upload image fail!");
                            return;
                        }
                    }
                    const res = await ProjectService.create(this.projectForm);
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
