<template>
    <div>CREATE PROJECT</div>
    <div>
        <div class="upload-list-images">
            <el-upload
                v-model:file-list="fileList"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                list-type="picture-card"
                :on-preview="handlePictureCardPreview"
                :on-remove="handleRemove"
            >
                <el-icon><Plus /></el-icon>
            </el-upload>

            <el-dialog v-model="dialogVisible">
                <img w-full :src="dialogImageUrl" alt="Preview Image" />
            </el-dialog>
        </div>
        <el-form label-width="120px">
            <el-form-item label="Title">
                <el-input></el-input>
            </el-form-item>
            <el-form-item label="Category">
                <el-select placeholder="Please select category">
                    <el-option label="Cộng đồng" />
                    <el-option label="Y tế" />
                    <el-option label="Trẻ em" />
                </el-select>
            </el-form-item>
            <el-form-item label="Fund goal">
                <el-input-number v-model="num" :precision="2" :step="0.1" :max="1000000000000" />
            </el-form-item>
            <el-form-item label="Summary">
                <el-input></el-input>
            </el-form-item>
            <el-form-item label="Description">
                <el-input type="textarea" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary">Create</el-button>
                <el-button>Cancel</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: "create-project",
    data() {
        return {
            fileList: [
                {
                    name: "food.jpeg",
                    url: "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
                },

                {
                    name: "food.jpeg",
                    url: "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
                },
                {
                    name: "food.jpeg",
                    url: "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
                },

                {
                    name: "food.jpeg",
                    url: "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
                },
            ],

            dialogImageUrl: "",
            dialogVisible: false,
        };
    },
};
</script>

<style scoped lang="scss">
.upload-list-images {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 2rem;
}
</style>
