import { Service } from "@/api/services/base";
import { API_URL } from "@/api/config";
import { Report } from "@/api/schemas";

export class ReportsService extends Service {
  protected baseUrl = API_URL + "reports/";

  public async list() {
    const response = await Service.API.get(this.baseUrl);

    return response.data.map((json: any) => {
      return new Report(json);
    });
  }

  public async detail(id: number) {
    const response = await Service.API.get(`${this.baseUrl}${id}/`);
    return new Report(response.data);
  }
}
