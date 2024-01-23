import axios from "axios";

const HOSTNAME = window.location.hostname;
// FIXME get from ENV
const PORT = 8088;

const HOST_URL = `http://${HOSTNAME}:${PORT}`;

export default class AxiosService {
  constructor() {
    this.axios = this.createAxios();
  }

  createAxios() {
    return axios.create({
      baseURL: HOST_URL,
      withCredentials: false,
      headers: {
        "Content-Type": "aplication/json",
      },
    });
  }

  handleError(error) {
    // TODO: logger and error handler...
    console.error(error);
  }

  async apiGet(endpoint, urlparams) {
    const res = await this.axios
      .get(`${endpoint}?${urlparams}`)
      .catch((error) => this.handleError(error));
    return res;
  }
}

export function useService() {
  const service = new AxiosService();
  return service;
}
