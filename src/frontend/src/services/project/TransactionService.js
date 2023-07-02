import BaseService from "../BaseService";

class TransactionService extends BaseService {
    get entity() {
        return "api_project/transactions";
    }

    async create(data) {
        try {
            const res = await this.request().post(`/${this.entity}/`, data);
            return res;
        } catch (error) {
            return error;
        }
    }

    async getAllOfProject(id = "", type = "") {
        try {
            const res = await this.request().get(
                `/${this.entity}?project=${id}&type_transaction=${type}`
            );
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

    async getNumberOfSupport(user_id) {
        try {
            const res = await this.request().get(
                `${this.entity}/number_user_support/?user_id=${user_id}`
            );
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }
}

export default new TransactionService();
