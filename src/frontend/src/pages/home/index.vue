<template>
    <!-- <h1>login successfully</h1> -->
    <header>
        <a href="#" class="logo"><img src="@/assets/logo.png" /></a>
        <div id="menu-icon" class="bx bx-menu" :class="{ 'bx-x': is_open }" @click="toggleMenu"></div>
        <ul class="navbar" :class="{ open: is_open }">
            <li><a href="#">Home Page</a></li>
            <li><a href="#">Project</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">FAQs</a></li>
            <li><a href="#">Donate Us</a></li>
        </ul>

        <div class="header-btn">
            <a href="#" class="sign-up">Sign Up</a>
            <a href="#" class="sign-in">Sign In</a>
        </div>
    </header>
</template>

<script>
export default {
    name: "home-page",
    data() {
        return {
            is_open: false,
        };
    },
    methods: {
        toggleMenu() {
            this.is_open = !this.is_open;
        },
    },
};
</script>

<style lang="scss" scoped>
header {
    position: fixed;
    width: 100%;
    top: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 35px 10%;
    background: transparent;
    white-space: nowrap;
    .logo {
        color: #fff;
        img {
            width: 50px;
        }
    }
    .navbar {
        display: flex;
        a {
            font-size: 18px;
            font-weight: 500;
            padding: 10px 20px;
            margin: 0 3px;
            color: #f5f5f5;
            transition: all 0.45s ease;
            border-radius: 5 px;
            &:hover {
                background-color: #c32865;
            }
        }
    }

    #menu-icon {
        font-size: 30px;
        z-index: 10001;
        color: #fff;
        cursor: pointer;
        display: none;
    }

    .header-btn {
        a {
            padding: 10px 20px;
            color: #fff;
            font-size: 16px;
            font-weight: 600;
        }

        .sign-in {
            background: #c32865;
            border: 2px solid transparent;
            border-radius: 5px;
            transition: all 0.5s eace;
            &:hover {
                border: 2px solid #c32865;
                background: transparent;
            }
        }
    }
}

@media (max-width: 1070px) {
    header {
        padding: 18px 3%;
        transition: 0.2s;
        #menu-icon {
            display: block;
        }
        .navbar {
            position: absolute;
            top: -800px;
            left: 0;
            right: 0;
            display: flex;
            flex-direction: column;
            background: #1b1b1b;
            text-align: left;
            a {
                display: block;
                padding: 1rem;
                margin: 0.8 rem;
            }
            &.open {
                top: 100%;
            }
        }
        .sign-up {
            display: none;
        }
    }
}
</style>
