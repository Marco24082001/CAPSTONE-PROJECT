<template>
    <div class="login">
        <el-card>
            <h2>Login</h2>
            <el-form
                class="login-form"
                :model="model"
                :rules="rules"
                ref="form"
                @submit.enter.prevent="login"
            >
                <el-form-item prop="email">
                    <el-input v-model="model.email" placeholder="email" :prefix-icon="ICONS.User">
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
                <el-form-item>
                    <el-button
                        :loading="loading"
                        class="login-button"
                        type="primary"
                        native-type="submit"
                        block
                        >Login</el-button
                    >
                </el-form-item>
                <a class="forgot-password" href="https://oxfordinformatics.com/"
                    >Forgot password ?</a
                >
            </el-form>
        </el-card>
    </div>
</template>

<script>
import { User, Lock } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
// import { mapState } from "vuex";
import AuthenticationService from "@/services/authentication/AuthenticationService.js";
export default {
    name: "login-page",
    data() {
        return {
            validCredentials: {
                email: "lightscope",
                password: "lightscope",
            },
            model: {
                email: "admin@gmai.com",
                password: "adminpw",
            },
            loading: false,
            rules: {
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
                        message: "Password is required",
                        trigger: "blur",
                    },
                    {
                        min: 4,
                        message: "Password length should be at least 5 characters",
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
        };
    },
    // computed: {
    //     ...mapState(["user"]),
    // },
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
            this.$store.commit("decoration/setFullscreenLoading", true);
            const res = await AuthenticationService.login(this.model);
            this.$store.commit("decoration/setFullscreenLoading", false);
            if (res.status === 200) {
                this.$router.push("/");
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
