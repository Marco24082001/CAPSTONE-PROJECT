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

    async getAll() {
        try {
            const res = await this.request().get(`/${this.entity}/`);
            console.log(res)
            return res;
        } catch (error) {
            console.log(error)
            return { error: error };
        }
    }

    async getbyId(id) {
        try {
            const res = await this.request().get(`${this.entity}/${id}/`);
            return res;
            
        } catch (error) {
            console.log(error);
            return { error: error }
        }
    }
}

export default new ProjectService();
