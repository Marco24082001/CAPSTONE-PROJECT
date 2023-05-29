<template>
    <div class="wrapper">
        <!-- <side-bar v-if="role === 'admin'" :sidebarLinks="sidebarLinks">
            <template v-slot:links> </template>
        </side-bar> -->
        <MenuSideBar></MenuSideBar>
        <div class="main-panel">
            <layout-content></layout-content>
        </div>
    </div>
</template>
<style lang="scss"></style>
<script>
import LayoutContent from "./Content.vue";
import MenuSideBar from "@/components/menusidebar/MenuSideBar.vue";
export default {
    name: "dashboard-layout",
    components: {
        MenuSideBar,
        LayoutContent,
    },
};
</script>

<style scoped lang="scss">
.wrapper {
    display: flex;
}
.main-panel {
    margin-top: 4rem;
    padding: 0px 10%;
    color: var(--cs-color-contrast-900);
}
</style>
