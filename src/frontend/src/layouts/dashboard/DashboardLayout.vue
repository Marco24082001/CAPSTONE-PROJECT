<template>
    <div class="wrapper">
        <!-- <side-bar v-if="role === 'admin'" :sidebarLinks="sidebarLinks">
            <template v-slot:links> </template>
        </side-bar> -->
        <MenuSideBar></MenuSideBar>
        <div class="main-panel">
            <Dashboard-content></Dashboard-content>
        </div>
    </div>
</template>
<style lang="scss"></style>
<script>
import DashboardContent from "@/layouts/dashboard/Content.vue";
import MenuSideBar from "@/components/menusidebar/MenuSideBar.vue";
export default {
    name: "dashboard-layout",
    components: {
        MenuSideBar,
        DashboardContent,
    },
};
</script>

<style scoped lang="scss">
.wrapper {
    display: flex;
}
.main-panel {
    position: relative;
    left: 250px;
    width: calc(100% - 250px);
    color: var(--cs-color-contrast-900);
    margin-bottom: 4rem;
}
</style>
