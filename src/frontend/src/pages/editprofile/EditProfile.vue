<template>
    <div class="container">
        <AppToolbar>
            <template #content>
                <el-breadcrumb>
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>

                    <el-breadcrumb-item>Edit Profile </el-breadcrumb-item>
                </el-breadcrumb>
            </template>
        </AppToolbar>
        <div class="profile-container">
            <div class="profile-form">
                <el-form
                    :model="profileForm"
                    label-position="left"
                    :rules="profileFormRule"
                    ref="form"
                    status-icon
                    label-width="200px"
                >
                    <el-form-item label="Avatar" prop="avatar">
                        <el-upload
                            class="avatar-uploader"
                            action="http://localhost:8000/api/v1/api_project/projects/upload_image/"
                            :show-file-list="false"
                            :on-success="handleAvatarSuccess"
                            :before-upload="beforeAvatarUpload"
                        >
                            <img
                                v-if="profileForm.avatar"
                                :src="profileForm.avatar"
                                class="avatar"
                            />
                            <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                        </el-upload>
                    </el-form-item>
                    <el-form-item label="First Name" prop="first_name">
                        <el-input
                            prop="first_name"
                            v-model="profileForm.first_name"
                            label="First Name"
                            placeholder="First Name"
                        />
                    </el-form-item>
                    <el-form-item label="Last Name" prop="last_name">
                        <el-input
                            v-model="profileForm.last_name"
                            label="Last Name"
                            placeholder="Last Name"
                        />
                    </el-form-item>
                    <el-form-item label="Email" prop="email"
                        ><el-input v-model="profileForm.email" label="Email" placeholder="Email" />
                    </el-form-item>
                    <el-form-item label="Phone">
                        <el-input v-model="profileForm.phone" label="Phone" placeholder="Phone" />
                    </el-form-item>
                    <el-form-item label="Address">
                        <el-input
                            v-model="profileForm.address"
                            label="Address"
                            placeholder="Address"
                        />
                    </el-form-item>
                    <el-form-item label="Biography">
                        <el-input
                            v-model="profileForm.biography"
                            :rows="8"
                            type="textarea"
                            placeholder="Biography"
                        ></el-input>
                    </el-form-item>
                    <el-form-item class="group-button">
                        <el-button type="primary" @click="handleEditProfile">Save</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import { ElMessage } from "element-plus";
import { uploadImage } from "@/utils/cloudinaryUtils";
import AppToolbar from "@/components/AppToolbar.vue";
import UserService from "@/services/user/UserService";
export default {
    name: "edit-profile",
    components: {
        AppToolbar,
    },
    computed: {
        ...mapState(["user"]),
    },
    data() {
        return {
            profileForm: {
                first_name: "",
                last_name: "",
                email: "",
                avatar: "",
                biography: "",
                phone: "",
                address: "",
            },
            profileFormRule: {
                first_name: [
                    { required: true, message: "Please input First name", trigger: "blur" },
                ],
                last_name: [{ required: true, message: "Please input Last name", trigger: "blur" }],
                avatar: [{ required: true, message: "Please set Avatar", trigger: "change" }],
                email: [{ required: true, message: "Please input Email", trigger: "blur" }],
            },
            rawFileImage: "",
        };
    },

    created() {
        this.getProfile();
    },

    methods: {
        async getProfile() {
            const res = await UserService.getbyId(this.user.currentUser.id);
            console.log(res);
            if (!res.error) {
                const profile = res.data;
                this.profileForm = {
                    id: profile.id,
                    first_name: profile.first_name,
                    last_name: profile.last_name,
                    email: profile.email,
                    phone: profile.phone,
                    biography: profile.biography,
                    avatar: profile.avatar,
                    address: profile.address,
                };
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },

        handleEditProfile: async function () {
            await this.$refs.form.validate(async (valid) => {
                if (valid) {
                    this.$store.commit("decoration/setFullscreenLoading", true);
                    if (this.rawFileImage !== "") {
                        try {
                            const { url } = await uploadImage(this.rawFileImage);
                            this.profileForm.avatar = url;
                        } catch (error) {
                            this.$store.commit("decoration/setFullscreenLoading", false);
                            ElMessage.error("Upload image failed!");
                            return;
                        }
                    }
                    const res = await UserService.edit(this.profileForm);
                    this.$store.commit("decoration/setFullscreenLoading", false);

                    if (res.status === 200) {
                        ElMessage.success("Edit Successful!");
                    } else {
                        ElMessage.error("Edit failed!");
                    }
                }
            });
        },

        handleAvatarSuccess: async function (response, uploadFile) {
            this.profileForm.avatar = URL.createObjectURL(uploadFile.raw);
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
    },
};
</script>

<style lang="scss" scoped>
.container {
    width: 100%;
    padding: var(--cs-main-panel-pading);
    display: flex;
    flex-direction: column;
    .profile-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        .profile-form {
            width: 39.5rem;

            .group-button {
                :deep(.el-form-item__content) {
                    justify-content: flex-end;
                }
            }
        }
    }
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

.avatar-uploader :deep(.el-upload:hover) {
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
