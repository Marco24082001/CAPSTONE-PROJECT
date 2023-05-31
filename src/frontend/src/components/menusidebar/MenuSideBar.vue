<template>
    <nav class="menu-sidebar" :class="{ 'menu-sidebar--hidden': !showMenu }">
        <header>
            <div class="image-text">
                <span class="image">
                    <img src="@/assets/logo.png" alt="logo" />
                </span>
                <div class="text header-text">
                    <span class="name">Donation System</span>
                    <span class="profession">Dashboard</span>
                </div>
            </div>
            <div class="bx bx-menu toggle" @click="toggleMenu"></div>
        </header>
        <div class="menu-bar">
            <div class="menu">
                <li class="search-box">
                    <div class="bx bx-search icon"></div>
                    <input type="search" placeholder="Search..." />
                </li>
                <ul class="menu-links">
                    <li class="nav-link">
                        <a href="#">
                            <div class="bx bx-briefcase-alt-2 icon"></div>
                            <span class="text nav-text">Project</span>
                        </a>
                    </li>
                    <li class="nav-link">
                        <a href="#">
                            <div class="bx bx-chart icon"></div>
                            <span class="text nav-text">Analytic</span>
                        </a>
                    </li>
                    <li class="nav-link">
                        <a href="#">
                            <div class="bx bx-heart icon"></div>
                            <span class="text nav-text">Like</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- <router-link to="/dashboard/project">Nested Page One</router-link> -->
</template>

<script>
export default {
    name: "menu-sidebar",
    data() {
        return {
            showMenu: true,
        };
    },
    methods: {
        toggleMenu() {
            this.showMenu = !this.showMenu;
        },
    },
};
</script>

<style lang="scss" scoped>
// ===== Resuable CSS ====
.menu-sidebar {
    .text {
        font-size: 16px;
        font-weight: 500;
        color: var(--cs-color-primary);
        transition: var(--tran-03);
        white-space: nowrap;
        opacity: 1;
    }
    .image {
        min-width: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        .img {
            width: 40px;
        }
    }
}
.menu-sidebar {
    --sidebar-color: #a5a1a1;
    --primary-color: #695cfe;
    --primary-color-light: #f6f5ff;
    --toggle-color: #ddd;
    --text-color: #707070;

    // ========= Transition ========= //
    --tran-02: all 0.2s ease;
    --tran-03: all 0.3s ease;
    --tran-04: all 0.4s ease;
    --tran-05: all 0.5s ease;

    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 250px;
    padding: 0px 14px;
    background: var(--cs-color-header-background);
    box-shadow: var(--cs-box-shadow-menu);
    z-index: 1000000;
    transition: var(--tran-05);
    &.menu-sidebar--hidden {
        width: 88px;
        .text {
            opacity: 0;
        }
    }

    header {
        position: relative;
        padding: 10px 0;
    }
    .image-text {
        display: flex;
        align-items: center;

        .image img {
            width: 40px;
            border-radius: 6px;
        }
        .header-text {
            display: flex;
            flex-direction: column;
            .name {
                font-weight: 600;
            }
            .profession {
                margin-top: -2px;
            }
        }
    }
    .toggle {
        position: absolute;
        top: 50%;
        right: -25px;
        transform: translateY(-50%);
        height: 25px;
        width: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-size: 25px;
        cursor: pointer;
    }

    li {
        height: 50px;
        margin-top: 10px;
        list-style: none;
        display: flex;
        align-items: center;
        .icon {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            min-width: 60px;
        }

        .icon,
        .text {
            color: var(--cs-color-secondary);
            transition: var(--tran-02);
        }
        a {
            height: 100%;
            width: 100%;
            display: flex;
            align-items: center;
            text-decoration: none;
            border-radius: 6px;
            transition: var(--tran-04);
            &:hover {
                background: var(--cs-color-button-hover);
                .icon,
                .text {
                    color: var(--wc-primary-text);
                }
            }
        }
    }

    .search-box {
        background: var(--primary-color-light);
        border-radius: 6px;
        input {
            height: 100%;
            width: 100%;
            outline: none;
            border: none;
            border-radius: 6px;
            background: var(--primary-color-light);
        }
    }

    .menu-bar {
        height: calc(100% -50px);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
}
</style>
