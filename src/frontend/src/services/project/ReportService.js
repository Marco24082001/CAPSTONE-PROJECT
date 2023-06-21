import BaseService from "../BaseService";

class ReportService extends BaseService {
    get entity() {
        return "api_project/reports";
    }

    async create(data) {
        try {
            const res = await this.request().post(`/${this.entity}/`, data);
            return res;
        } catch (error) {
            return error;
        }
    }

    async getReports(id = "") {
        try {
            const res = await this.request().get(`/${this.entity}?project=${id}`);
            console.log(res);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async getbyId(id) {
        try {
            const res = await this.request().get(`${this.entity}/${id}/`);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }
}

export default new ReportService();
