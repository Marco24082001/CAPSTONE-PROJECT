import App from "./App.vue";
import { createApp } from "vue";
import ElementPlus from "element-plus";
import router from "./router/index";
import "element-plus/dist/index.css";
import "boxicons/css/boxicons.min.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
import store from "./store";
// import PaperDashboard from "./plugins/paperDashboard";
// import "vue-notifyjs/themes/default.css";

const app = createApp(App);
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}
app.use(router);
// app.use(PaperDashboard);
app.use(store);
app.mount("#app");
