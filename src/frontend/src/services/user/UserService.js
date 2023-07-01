import BaseService from "../BaseService";

class UserService extends BaseService {
    get entity() {
        return "api_user/users";
    }

    async getAll() {
        try {
            const res = await this.request().get(`/${this.entity}/`);
            return res;
        } catch (error) {
            return { error: error };
        }
    }

    async create(data) {
        try {
            const res = await this.request().post(`/${this.entity}/`, data);
            return res;
        } catch (error) {
            return error;
        }
    }

    async edit(data) {
        try {
            const { id, ...dataWithoutKey } = data;
            const res = await this.request().patch(`/${this.entity}/${id}/`, dataWithoutKey);
            return res;
        } catch (error) {
            return { error: error };
        }
    }

    async delete(id) {
        try {
            const res = await this.request().delete(`/${this.entity}/${id}/`);
            return res;
        } catch (error) {
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

export default new UserService();
