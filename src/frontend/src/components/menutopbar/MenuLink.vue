<template>
    <component :is="tag" class="nav-item" v-bind="$attrs" tag="li">
        <slot>
            <span class="menu-item">{{ name }}</span>
        </slot>
    </component>
</template>

<script>
export default {
    name: "menu-link",
    inheritAttrs: false,
    inject: {
        autoClose: {
            default: true,
        },
        addLink: {
            default: () => {},
        },
        removeLink: {
            default: () => {},
        },
    },
    props: {
        name: String,
        icon: String,
        tag: {
            type: String,
            default: "router-link",
        },
    },
    methods: {
        isActive() {
            return this.$el.classList.contains("active");
        },
    },
    // mounted() {
    //     if (this.addLink) {
    //         this.addLink(this);
    //     }
    // },
    // beforeUnmount() {
    //     if (this.$el && this.$el.parentNode) {
    //         this.$el.parentNode.removeChild(this.$el);
    //     }
    //     if (this.removeLink) {
    //         this.removeLink(this);
    //     }
    // },
};
</script>
