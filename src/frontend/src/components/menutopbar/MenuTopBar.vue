<template>
    <header class="menu-topbar" :class="{ 'menu-topbar--hidden': !showMenu }">
        <a href="#" class="logo"><img src="@/assets/logo.png" /></a>
        <div
            id="menu-icon"
            class="bx bx-menu"
            :class="{ 'bx-x': isOpen }"
            @click="toggleMenu"
        ></div>
        <ul class="navbar" :class="{ open: isOpen }" data-scheam="default">
            <menu-link
                v-for="(link, index) in topbarLinks"
                :key="index"
                :to="link.path"
                :name="link.name"
            >
            </menu-link>
        </ul>

        <div v-if="!user.currentUser.user_id" class="header-btn">
            <router-link to="/register" class="sign-up">Sign Up</router-link>
            <router-link to="/login" class="sign-in">Sign In</router-link>
        </div>
        <div v-else class="profile-menu">
            <img class="user-pic" src="@/assets/avatar1.jpg" @click.stop="isSubOpen = !isSubOpen" />

            <OnClickOutside @trigger="dropdownHandler">
                <div class="sub-menu-wrap" :class="{ 'open-menu': isSubOpen }">
                    <div class="sub-menu">
                        <div class="user-info">
                            <img src="@/assets/avatar1.jpg" />
                            <h4>Marco</h4>
                        </div>
                        <hr />
                        <router-link to="/" class="sub-menu-link"
                            ><div class="bx bxs-user sub-menu-icon"></div>
                            <p>Your profile</p>
                            <div class="bx bx-chevron-right"></div
                        ></router-link>
                        <router-link to="/dashboard/projects" class="sub-menu-link"
                            ><div class="bx bx-briefcase-alt-2 sub-menu-icon"></div>
                            <p>Dashboard</p>
                            <div class="bx bx-chevron-right"></div>
                        </router-link>
                        <router-link to="/" @click="logout" class="sub-menu-link"
                            ><div class="bx bx-log-out sub-menu-icon"></div>
                            <p>Logout</p>
                            <div class="bx bx-chevron-right"></div
                        ></router-link>
                    </div>
                </div>
            </OnClickOutside>
        </div>

        <div class="dark-mode-switch">
            <el-switch
                v-model="themeMode"
                class="mb-2"
                active-text="Dark"
                active-value="dark"
                inactive-value="default"
                active-color="var(--cs-color-secondary)"
                style="
                    --el-switch-on-color: var(--cs-color-contrast-400);
                    --el-switch-off-color: var(--cs-color-contrast-400);
                "
                size="small"
            />
        </div>
    </header>
</template>
<script>
import MenuLink from "./MenuLink.vue";
import { mapState } from "vuex";
import { OnClickOutside } from "@vueuse/components";

import AuthenticationService from "@/services/authentication/AuthenticationService.js";

export default {
    name: "menu-topbar",
    props: {
        title: {
            type: String,
            default: "User Topbar",
        },
        topbarLinks: {
            type: Array,
            default: () => [
                {
                    path: "/home",
                    name: "Home Page",
                },
                {
                    path: "/projects",
                    name: "Project",
                },
                {
                    path: "/about",
                    name: "About",
                },
                {
                    path: "/faqs",
                    name: "FAQs",
                },
                {
                    path: "/donate-us",
                    name: "Donate Us",
                },
            ],
        },
    },
    components: {
        MenuLink,
        OnClickOutside,
    },
    data() {
        return {
            isOpen: false,
            isSubOpen: false,
            showMenu: true,
            lastScrollPosition: 0,
            circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        };
    },
    computed: {
        ...mapState(["user"]),
        themeMode: {
            get() {
                return this.$store.state.decoration.themeMode;
            },
            set(value) {
                this.$store.commit("decoration/setThemeMode", value);
            },
        },
    },
    mounted() {
        window.addEventListener("scroll", this.onScroll);
    },
    beforeUnmount() {
        window.removeEventListener("scroll", this.onScroll);
    },
    methods: {
        toggleMenu() {
            this.isOpen = !this.isOpen;
        },

        onScroll() {
            const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;
            if (currentScrollPosition < 0) {
                return;
            }
            // Stop executing this function if the difference between
            // current scroll position and last scroll position is less than some offset
            if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
                return;
            }
            this.showMenu = currentScrollPosition < this.lastScrollPosition;
            this.lastScrollPosition = currentScrollPosition;
        },

        logout: async function () {
            await AuthenticationService.logout();
            this.$router.go();
        },

        dropdownHandler(event) {
            console.log(event)
            if (this.isSubOpen == true) {
                this.isSubOpen = false;
            } else if (this.isSubOpen == false) {
                this.isSubOpen = true;
            }
        },
    },
};
</script>

<style lang="scss" scoped>
header {
    position: fixed;
    // transition: all 0.45s ease;
    width: 100%;
    height: var(--cs-header-initial-height);
    top: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 10%;
    background: var(--cs-color-header-background);
    border-bottom: var(--cs-header-border-width) solid var(--cs-color-contrast-200);
    white-space: nowrap;
    .logo {
        color: #fff;
        img {
            width: 40px;
        }
    }
    .navbar {
        display: flex;
        background: var(--cs-color-header-background);
        a {
            display: inline-block;
            position: relative;
            padding: 0.7rem 0.9rem;
            margin: 0 0.2rem;
            border-radius: 5px;
            height: 100%;
            align-items: center;
            white-space: nowrap;
            font-family: var(--cs-font-menu-family), sans-serif;
            font-size: var(--cs-font-menu-size);
            font-weight: var(--cs-font-menu-weight);
            font-style: var(--cs-font-menu-style);
            letter-spacing: var(--cs-font-menu-letter-spacing);
            text-transform: var(--cs-font-menu-text-transform);
            :deep(.menu-item) {
                // color: red;
                display: flex;
                position: relative;
                &::before {
                    content: "";
                    position: absolute;
                    width: 100%;
                    height: 1px;
                    transition: 0.25s;
                    background-color: var(--cs-color-secondary);
                    bottom: -10px;
                    opacity: 0;
                }
            }
            &.active {
                color: var(--cs-color-secondary);
                :deep(.menu-item::before) {
                    bottom: -3px;
                    opacity: 1;
                }
            }
        }
        &:hover {
            > a:hover {
                :deep(.menu-item::before) {
                    bottom: -3px;
                    opacity: 1;
                }
            }
            > a {
                :deep(.menu-item:before) {
                    opacity: 0;
                    bottom: -10px;
                }
            }
        }
    }

    #menu-icon {
        font-size: 30px;
        z-index: 10001;
        color: var(--cs-color-contrast-700);
        cursor: pointer;
        display: none;
    }

    .header-btn {
        span {
            font-size: var(--cs-font-menu-size);
        }
        a {
            padding: 10px 20px;
            font-size: var(--cs-font-menu-sign-up-in-size);
            font-weight: var(--cs-font-menu-sign-up-in-weight);
        }

        .sign-up {
            color: var(--cs-color-contrast-600);
            &:hover {
                color: var(--cs-color-contrast-900);
            }
        }

        .sign-in {
            color: var(--cs-color-button-contrast);
            background: var(--cs-color-button);
            border: 2px solid transparent;
            border-radius: 5px;
            transition: all 0.5s eace;
            &:hover {
                color: var(--cs-color-contrast-900);
                border: 2px solid var(--cs-color-button);
                background: var(--cs-color-contrast-50);
            }
        }
    }

    .profile-menu {
        .user-pic {
            width: 2.4rem;
            height: 2.4rem;
            background-size: cover;
            background-position: 20% 20%;
            border-radius: 50%;
            cursor: pointer;
        }
        .sub-menu-wrap {
            position: absolute;
            top: 100%;
            right: 10%;
            width: 180px;
            max-height: 0px;
            overflow: hidden;
            transition: max-height 0.5s;
            background-color: var(--cs-color-submenu-background);
            box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.1);
            border-top: 1px var(--cs-color-contrast-200) solid;
            &.open-menu {
                max-height: 400px;
                border: 1px var(--cs-color-contrast-200) solid;
            }

            .sub-menu {
                padding: 0.2rem;
                margin: 5px;
                .user-info {
                    display: flex;
                    align-items: center;
                    img {
                        width: 2.6rem;
                        height: 2.6rem;
                        border-radius: 50%;
                        margin-right: 15px;
                    }
                    h4 {
                        font-weight: 500;
                        font-size: 0.8rem;
                        color: var(--cs-color-primary);
                    }
                }
                hr {
                    border: 0;
                    height: 1px;
                    width: 100%;
                    background: #ccc;
                    margin: 8px 0 8px;
                }
                .sub-menu-link {
                    display: flex;
                    align-items: center;
                    text-decoration: none;
                    color: var(--cs-color-primary);
                    background-color: transparent;
                    margin: 0.6rem 0;
                    font-size: var(--cs-font-submenu-size);
                    font-weight: var(--cs-font-submenu-weight);
                    font-style: var(--cs-font-submenu-style);
                    letter-spacing: var(--cs-font-submenu-letter-spacing);
                    text-transform: var(--cs-font-submenu-text-transform);
                    .sub-menu-icon {
                        border-radius: 50%;
                        margin-right: 10px;
                        padding: 8px;
                    }
                    p {
                        width: 100%;
                    }
                    .bx-chevron-right {
                        font-size: 0.9rem;
                        transition: transform 0.5s;
                    }
                    &:hover {
                        color: var(--cs-color-secondary);
                        .bx-chevron-right {
                            transform: translateX(5px);
                        }
                    }
                }
            }
        }
    }

    .dark-mode-switch {
        position: absolute;
        right: 1.2%;
    }
    &.menu-topbar--hidden {
        box-shadow: none;
        transform: translate3d(0, -100%, 0);
    }
}

@media (max-width: 800px) {
    header {
        z-index: 10000;
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
            text-align: left;
            box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.1);
            a {
                display: block;
                padding: 1rem;
                margin: 0.8 rem;
                &:hover {
                    color: var(--cs-color-secondary);
                }
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
