<template>
    <div
        :data-site-scheme="decoration.themeMode"
        :data-scheme="decoration.themeMode"
        v-loading.fullscreen.lock="decoration.fullscreenLoading"
        class="main"
    >
        <router-view></router-view>
    </div>
</template>

<script>
import { mapState } from "vuex";
export default {
    name: "App",
    computed: {
        ...mapState(["decoration"]),
    },
    created() {
        this.$store.commit("decoration/setFullscreenLoading", false);
    },
};
</script>

<style lang="scss">
@import "./assets/style/main.scss";
html {
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

*,
*:before,
*:after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    text-decoration: none;
    list-style: none;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    // &::-webkit-scrollbar {
    //     width: 0px !important;
    // }
}

a {
    color: var(--cs-color-primary);
}

#app {
    display: flex;
    flex-direction: column;
    transition: background 0.3s ease-in-out;
    font-family: Roboto, sans-serif;
    .main {
        min-height: 100vh;
        background-color: var(--cs-color-site-background);
        font-family: var(--cs-font-base-family), sans-serif;
        font-size: var(--cs-font-base-size);
        font-weight: var(--cs-font-base-weight);
        font-style: var(--cs-font-base-style);
        line-height: var(--cs-font-base-line-height);
        letter-spacing: var(--cs-font-base-letter-spacing);
    }
}

body {
    background-size: cover;
    background-position: 15% 20%;
    &::-webkit-scrollbar {
        width: 0px !important;
    }
}
</style>
