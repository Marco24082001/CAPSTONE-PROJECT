import BaseService from "../BaseService";
import jwt_decode from "jwt-decode";

import { storeTokenToVuex, storeCurrentUserToVuex } from "@/helper/storeHelper";
class AuthenticationService extends BaseService {
    get entity() {
        return "api_auth";
    }

    async login(data) {
        const post_login = this.request()
            .post(`/${this.entity}/login/`, data)
            .then(
                (response) => {
                    return response;
                },
                (error) => {
                    return error.response;
                }
            );
        const res = await post_login;

        console.log(res);
        if (res.status === 200) {
            console.log(jwt_decode(res.data.access));
            storeTokenToVuex(res.data);
            storeCurrentUserToVuex(jwt_decode(res.data.access));
        }
        return res;
    }

    

    async register(data) {
        const post_register = this.request()
            .post(`/${this.entity}/register/`, data)
            .then(
                (response) => {
                    return response;
                },
                (error) => {
                    return error.response;
                }
            );
        const res = await post_register;
        console.log(res);
        return res
    }

    async getCurrentUser() {
        try {
            return await this.request().get(`/${this.entity}/getCurrentUser`);
        } catch (error) {
            console.log(error);
        }
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
}

export default new AuthenticationService();
