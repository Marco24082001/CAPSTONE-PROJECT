<template>
    <div class="thanhvi">
        <router-view></router-view>
    </div>
</template>

<script></script>

<style lang="scss">
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: Roboto, sans-serif;
    text-decoration: none;
    list-style: none;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
#app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    transition: background 0.3s ease-in-out;
}

body {
    background-color: #161f29;
    background-image: url(assets/bg1.jpg);
    background-size: cover;
    background-position: 15% 20%;
}
</style>
