import BaseService from "../BaseService";
import jwt_decode from "jwt-decode";

import { storeTokenToVuex } from "@/helper/storeHelper";
class AuthenticationService extends BaseService {
    get entity() {
        return "auth";
    }

    async login(data) {
        const res = this.request()
            .post(`/${this.entity}/login/`, data)
            .then(
                (response) => {
                    return response;
                },
                (error) => {
                    return error.response;
                }
            );
        if (res.status === 200) {
            console.log(jwt_decode(res.data.access));
            storeTokenToVuex(res.data);
        }
        // if (!res.data.error) {
        //     storeTokenToVuex(res.data);
        //     const currentUser = (await this.getCurrentUser()).data.response;
        //     storeCurrentUserToVuex(currentUser);
        // }
        return res;
    }

    async logout() {
        try {
            localStorage.removeItem("vuex");
            localStorage.clear();
            return true;
        } catch (error) {
            return false;
        }
    }

    async getCurrentUser() {
        try {
            return await this.request().get(`/${this.entity}/getCurrentUser`);
        } catch (error) {
            console.log(error);
        }
    }
}

export default new AuthenticationService();
