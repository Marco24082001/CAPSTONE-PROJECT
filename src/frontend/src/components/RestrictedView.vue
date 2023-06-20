<template>
    <slot v-if="permissionValidate"></slot>
</template>

<script>
import { mapState } from "vuex";

export default {
    name: "restricted-view",
    props: {
        roles: null,
    },
    components: {},
    computed: {
        ...mapState({
            role: (state) => state.user.currentUser.role,
        }),

        permissionValidate() {
            if (!this.roles) return true;
            return this.roles.indexOf(this.role) != -1;
        },
    },
};
</script>
