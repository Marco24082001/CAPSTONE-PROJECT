import BaseService from "../BaseService";

class ProjectService extends BaseService {
    get entity() {
        return "api_project/projects";
    }

    async create(data) {
        try {
            const res = await this.request().post(`/${this.entity}/`, data);
            return res;
        } catch (error) {   
            console.log("thanhvi");
            return error;
        }
    }

    // async login(data) {
    //     const post_login = this.request()
    //         .post(`/${this.entity}/login/`, data)
    //         .then(
    //             (response) => {
    //                 return response;
    //             },
    //             (error) => {
    //                 return error.response;
    //             }
    //         );
    //     const res = await post_login;

    //     console.log(res);
    //     if (res.status === 200) {
    //         console.log(jwt_decode(res.data.access));
    //         storeTokenToVuex(res.data);
    //         storeCurrentUserToVuex(jwt_decode(res.data.access));
    //     }
    //     return res;
    // }
}

export default new ProjectService();
