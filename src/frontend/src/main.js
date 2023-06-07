import App from "./App.vue";
import { createApp } from "vue";
import ElementPlus from "element-plus";
import router from "./router/index";
import "element-plus/dist/index.css";
import "boxicons/css/boxicons.min.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
import { QuillEditor } from "@vueup/vue-quill";
// import ImageResize from 'quill-image-resize-module';
import "@vueup/vue-quill/dist/vue-quill.snow.css";
// const ImageResize = require('quill-image-resize-module').default
// import { ImageResize } from 'quill-image-resize'
// import "quill-image-resize-[module/image-resize.min.js"

import store from "./store";

const app = createApp(App);
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}
// QuillEditor.register('modules/imageResize', ImageResize);
app.component("QuillEditor", QuillEditor);
app.use(router);
app.use(store);
app.mount("#app");
