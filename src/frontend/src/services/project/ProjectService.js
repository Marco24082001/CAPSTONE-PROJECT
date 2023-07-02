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
            console.log(error);
            return { error: error };
        }
    }

    async edit(data) {
        try {
            const { id, ...dataWithoutKey } = data;
            const res = await this.request().patch(`/${this.entity}/${id}/`, dataWithoutKey);
            console.log(res);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async getAll() {
        try {
            const res = await this.request().get(`/${this.entity}/`);
            console.log(res);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async getActiveProjects() {
        try {
            const res = await this.request().get(`/${this.entity}?status=ACTIVE`);
            console.log(res);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async getLikeProjects() {
        try {
            const res = await this.request().get(`/${this.entity}/getLikeProjects/`);
            console.log(res);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async getProjectOwner(id) {
        try {
            const res = await this.request().get(
                `/${this.entity}/get_project_owner/?user_id=${id}`
            );
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async deactivate(id) {
        try {
            const res = await this.request().put(`/${this.entity}/${id}/deactivate/`);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async activate(id) {
        try {
            const res = await this.request().put(`/${this.entity}/${id}/activate/`);
            return res;
        } catch (error) {
            console.log(error);
            return { error: error };
        }
    }

    async verify(id) {
        try {
            const res = await this.request().put(`/${this.entity}/${id}/verify/`);
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

export default new ProjectService();
