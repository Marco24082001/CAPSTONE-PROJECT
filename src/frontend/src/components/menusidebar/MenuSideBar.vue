<template>
    <header div="menu-sidebar"></header>
    <!-- <router-link to="/dashboard/project">Nested Page One</router-link> -->
</template>

<script>
export default {
    name: "menu-sidebar",
};
</script>

<style scoped lang="scss">
.menu-sidebar {
    --sidebar-color: #fff;
    --primary-color: #695cfe;
    --primary-color-light: #f6f5ff;
    --toggle-color: #ddd;
    --text-color: #707070;

    // ========= Transition ========= //
    --tran-02: all 0.2s ease;
    --tran-03: all 0.3s ease;
    --tran-04: all 0.4s ease;
    --tran-05: all 0.5s ease;
}
</style>
