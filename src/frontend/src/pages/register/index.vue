<template>
    <div class="login">
        <el-card>
            <h2>Register</h2>
            <el-form
                class="login-form"
                :model="model"
                :rules="rules"
                ref="form"
                @submit.enter.prevent="login"
            >
                <el-form-item prop="email">
                    <el-input v-model="model.email" placeholder="Email" :prefix-icon="ICONS.User">
                    </el-input>
                </el-form-item>
                <el-form-item prop="first_name">
                    <el-input
                        v-model="model.first_name"
                        placeholder="First name"
                        :prefix-icon="ICONS.EditPen"
                    >
                    </el-input>
                </el-form-item>
                <el-form-item prop="last_name">
                    <el-input
                        v-model="model.last_name"
                        placeholder="Last name"
                        :prefix-icon="ICONS.EditPen"
                    >
                    </el-input>
                </el-form-item>

                <el-form-item prop="password">
                    <el-input
                        v-model="model.password"
                        placeholder="Password"
                        type="password"
                        :prefix-icon="ICONS.Lock"
                    ></el-input>
                </el-form-item>
                <el-form-item prop="repassword">
                    <el-input
                        v-model="model.repassword"
                        placeholder="Re-password"
                        type="password"
                        :prefix-icon="ICONS.Lock"
                    ></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button
                        :loading="loading"
                        class="login-button"
                        type="primary"
                        native-type="submit"
                        block
                        >Register</el-button
                    >
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
import { User, Lock, EditPen } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import AuthenticationService from "@/services/authentication/AuthenticationService";
export default {
    name: "register-page",
    data() {
        return {
            validCredentials: {
                first_name: "lightscope",
                last_name: "lightscope",
                email: "lightscope",
                password: "lightscope",
                repassword: "lightscope",
            },
            model: {
                first_name: "",
                last_name: "",
                email: "",
                password: "",
                repassword: "",
            },
            loading: false,
            rules: {
                first_name: [
                    {
                        required: true,
                        message: "first name is required",
                        trigger: "blur",
                    },
                    {
                        min: 1,
                        message: "first name length should be at least 2 characters",
                        trigger: "blur",
                    },
                ],
                last_name: [
                    {
                        required: true,
                        message: "last name is required",
                        trigger: "blur",
                    },
                    {
                        min: 1,
                        message: "last name length should be at least 2 characters",
                        trigger: "blur",
                    },
                ],
                email: [
                    {
                        required: true,
                        message: "email is required",
                        trigger: "blur",
                    },
                    {
                        min: 4,
                        message: "email length should be at least 5 characters",
                        trigger: "blur",
                    },
                ],
                password: [
                    {
                        required: true,
                        message: "password is required",
                        trigger: "blur",
                    },
                    {
                        min: 4,
                        message: "password length should be at least 5 characters",
                        trigger: "blur",
                    },
                ],
                repassword: [
                    {
                        required: true,
                        message: "Re-password is required",
                        trigger: "blur",
                    },
                    {
                        min: 4,
                        message: "Re-password length should be at least 5 characters",
                        trigger: "blur",
                    },
                ],
            },
        };
    },
    created() {
        this.ICONS = {
            User,
            Lock,
            EditPen,
        };
    },

    methods: {
        simulateLogin() {
            return new Promise((resolve) => {
                setTimeout(resolve, 800);
            });
        },
        async login() {
            let valid = await this.$refs.form.validate();
            if (!valid) {
                return;
            }
            const res = await AuthenticationService.register(this.model);
            if (res.status === 201) {
                this.$router.push("/login");
            } else {
                ElMessage.error("Tài khoản mật khẩu không đúng!");
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.login {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 100vh;
}

.login-button {
    width: 100%;
    margin-top: 40px;
}
.login-form {
    width: 290px;
}
.forgot-password {
    margin-top: 10px;
}
$teal: rgb(0, 124, 137);
.el-button--primary {
    background: $teal;
    border-color: $teal;

    &:hover,
    &.active,
    &:focus {
        background: lighten($teal, 7);
        border-color: lighten($teal, 7);
    }
}
.login .el-input__inner:hover {
    border-color: $teal;
}
.login .el-input__prefix {
    background: rgb(238, 237, 234);
    left: 0;
    height: calc(100% - 2px);
    left: 1px;
    top: 1px;
    border-radius: 3px;
    .el-input__icon {
        width: 30px;
    }
}
.login .el-input input {
    padding-left: 35px;
}
.login .el-card {
    padding-top: 0;
    padding-bottom: 30px;
}
h2 {
    font-family: "Open Sans";
    letter-spacing: 1px;
    font-family: Roboto, sans-serif;
    padding-bottom: 20px;
}
a {
    color: $teal;
    text-decoration: none;
    &:hover,
    &:active,
    &:focus {
        color: lighten($teal, 7);
    }
}
.login .el-card {
    width: 340px;
    display: flex;
    justify-content: center;
}
</style>
