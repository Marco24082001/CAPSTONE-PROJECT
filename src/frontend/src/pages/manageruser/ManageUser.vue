<template>
    <div class="container">
        <AppToolbar>
            <template #content
                ><el-breadcrumb>
                    <el-breadcrumb-item>
                        <router-link to="/home">Home</router-link>
                    </el-breadcrumb-item>
                    <el-breadcrumb-item>User</el-breadcrumb-item>
                </el-breadcrumb></template
            >
        </AppToolbar>
        <div class="cp-users row">
            <div class="col-24">
                <el-table :data="resultQuery">
                    <el-table-column label="Avatar" width="80">
                        <template #default="scope">
                            <div>
                                <img
                                    width="50"
                                    height="50"
                                    :src="scope.row.avatar"
                                    v-bind:style="{
                                        'border-radius': '50%',
                                        border: '1px solid black',
                                    }"
                                />
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="Email" prop="email" sortable width="180" />
                    <el-table-column label="Full Name" prop="full_name" sortable width="180"/>
                    <el-table-column label="Phone" prop="phone" sortable />
                    <el-table-column label="Role" prop="role" sortable />
                    <el-table-column label="Joined" prop="created_at" sortable>
                        <template #default="scope">
                            <span>{{ new Date(scope.row.created_at).toLocaleDateString() }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column align="center">
                        <template #header>
                            <el-input
                                v-model="searchQuery"
                                size="small"
                                placeholder="Type to search"
                            />
                        </template>
                        <template #default="scope">
                            <el-button
                                v-if="scope.row.is_active"
                                size="small"
                                type="danger"
                                @click="deactivate(scope.$index, scope.row)"
                            >
                                Deactivate</el-button
                            >
                            <el-button
                                v-else
                                size="small"
                                type="primary"
                                @click="activate(scope.$index, scope.row)"
                            >
                                Activate
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import { ElMessage } from "element-plus";
import AppToolbar from "@/components/AppToolbar.vue";
import UserService from "@/services/user/UserService";
export default {
    name: "manage-user",
    components: {
        AppToolbar,
    },
    data() {
        return {
            listUsers: [],
            searchQuery: "",
        };
    },

    computed: {
        ...mapState(["user"]),
        resultQuery() {
            if (this.searchQuery != "") {
                return this.listUsers.filter((item) => {
                    return item.full_name.toLowerCase().includes(this.searchQuery.toLowerCase());
                });
            } else {
                return this.listUsers;
            }
        },
    },
    created() {
        this.getAllUsers();
    },
    methods: {
        async getAllUsers() {
            const res = await UserService.getAll();
            if (!res.error) {
                this.listUsers = res.data;
            } else {
                if (res.error.status === 302) {
                    ElMessage.error(res.error.data);
                }
            }
        },
        async deactivate(index, user) {
            
            const res = await UserService.edit({
                id: user.id,
                is_active: false
            })

            if(!res.error) {
                ElMessage.success("Deactivate Successful!")
                // const objIndex = this.listUsers.findIndex((obj => obj.id == user.id));
                this.listUsers[index].is_active = false;
            }else
            {
                ElMessage.error("Deactivate failed!")
            }
        },

        async activate(index, user) {
            const res = await UserService.edit({
                id: user.id,
                is_active: true
            })

            if(!res.error) {
                ElMessage.success("Activate Successful!")
                // const objIndex = this.listUsers.findIndex((obj => obj.id == user.id));
                this.listUsers[index].is_active = true;
            } else {
                ElMessage.error("Activate failed!")
            }
        },
    },
};
</script>
