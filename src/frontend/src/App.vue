<template>
    <div :data-site-scheme="decoration.themeMode" :data-scheme="decoration.themeMode" class="body">
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
}

a {
    color: var(--cs-color-primary);
}

#app {
    display: flex;
    flex-direction: column;
    transition: background 0.3s ease-in-out;
    font-family: Roboto, sans-serif;
    .body {
        min-height: 100vh;
        background-color: var(--cs-color-site-background);
    }
}

body {
    // background-image: url(assets/bg1.jpg);
    background-size: cover;
    background-position: 15% 20%;
}
</style>
