<template>
    <div class="wrapper">
        <!-- <side-bar v-if="role === 'admin'" :sidebarLinks="sidebarLinks">
            <template v-slot:links> </template>
        </side-bar> -->
        <MenuTopBar></MenuTopBar>
        <div class="main-panel">
            <layout-content></layout-content>
        </div>
        <BaseFooter></BaseFooter>
    </div>
</template>
<style lang="scss"></style>
<script>
import LayoutContent from "./Content.vue";
import BaseFooter from "../BaseFooter.vue";
import MenuTopBar from "@/components/menutopbar/MenuTopBar.vue";
export default {
    name: "user-layout",
    components: {
        MenuTopBar,
        LayoutContent,
        BaseFooter,
    },
};
</script>

<style scoped lang="scss">
.wrapper {
    display: flex;
    flex-direction: column;
    margin-top: var(--cs-header-initial-height);
}
.main-panel {
    margin-top: 2rem;
    color: var(--cs-color-contrast-900);
    margin-bottom: 4rem;
    width: 100vw;
    min-height: 100vh;
}
</style>
