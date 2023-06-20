<template>
    <nav class="app-toolbar">
        <slot name="content"> </slot>
    </nav>
</template>

<script>
export default {
    name: "app-toolbar",
};
</script>

<style scoped lang="scss">
.app-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0;
    margin-bottom: 2rem;
    border-bottom: var(--cs-header-border-width) solid var(--cs-color-contrast-200);
}
</style>
