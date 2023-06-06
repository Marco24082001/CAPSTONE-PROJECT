<template>
    <div class="editor-container">
        <QuillEditor v-model:content="content" theme="snow" toolbar="full" contentType="html" />
    </div>
</template>

<script>
export default {
    name: "text-editor",
    props: {
        initial_content: {
            type: String,
            default: null,
        },
    },
    data() {
        return {
            content: null,
        };
    },
    created() {
        this.content = this.initial_content;
    },

    watch: {
        content: function (val) {
            this.$emit("input-description", val);
        },
    },
};
</script>

<style lang="scss" scoped>
.editor-container {
    min-height: 300px;
    max-height: fit-content;
    margin-bottom: 30px;
    border-radius: 20px;

    :deep(.ql-toolbar) {
        border-radius: 4px 4px 0px 0px;
    }

    :deep(.ql-container) {
        border-radius: 0px 0px 4px 4px;
        border: 1px solid #d1d5db;
    }

    :deep(.ql-editor) {
        min-height: 400px !important;
        max-height: 70vh !important;
        overflow: auto;
        color: black;
    }
}
</style>
