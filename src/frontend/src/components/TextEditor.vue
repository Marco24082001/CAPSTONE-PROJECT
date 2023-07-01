<template>
    <div class="editor-container" :class="{'preview': preview}">
        <QuillEditor v-model:content="content" theme="snow"  toolbar="full" contentType="html" :readOnly="preview" />
        
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
        preview: {
            type: Boolean,
            default: false
        }
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
        initial_content: function (val) {
            this.content = val;
        },
    },
};
</script>

<style lang="scss" scoped>
.editor-container {
    // min-height: 300px;
    max-height: fit-content;
    // margin-bottom: 30px;
    border-radius: 20px;
    &.preview {
        :deep(.ql-toolbar) {
            display:none;
        }
        :deep(.ql-toolbar.ql-snow + .ql-container.ql-snow) {
            border-top: 1px solid #d1d5db;
        }

        :deep(.ql-editor) {
            max-height: 1000vh !important;
        }
    }
    :deep(.ql-toolbar) {
        border-radius: 4px 4px 0px 0px;
    }

    :deep(.ql-container) {
        border-radius: 0px 0px 4px 4px;
        border: 1px solid #d1d5db;
    }

    :deep(.ql-editor) {
        min-height: 300px !important;
        max-height: 300px;
        overflow: auto;
        color: black;
        max-width: 100vw !important;
        .ql-video {
            width: 100%;
        }
    }
}
</style>
