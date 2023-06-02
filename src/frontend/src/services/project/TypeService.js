import BaseService from "../BaseService";

class TypeService extends BaseService {
    get entity() {
        return "api_project/types";
    }

    async getAll() {
        try {
            const res = await this.request().get(`/${this.entity}/`);
            return res;
        } catch (error) {
            return { error: error };
        }
    }
}

export default new TypeService();
