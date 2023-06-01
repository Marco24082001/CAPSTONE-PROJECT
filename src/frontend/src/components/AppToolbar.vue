<template>
    <nav class="app-toolbar">
        <div class="title-page">{{ title }}</div>
    </nav>
</template>

<script>
export default {
    name: "app-toolbar",
    props: {
        title: {
            type: String,
            default: "Watting",
        },
    },
};
</script>

<style scoped lang="scss">
.app-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
    margin-bottom: 2rem;
    border-bottom: var(--cs-header-border-width) solid var(--cs-color-contrast-200);
}
</style>
