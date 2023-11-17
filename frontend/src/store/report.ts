import { Report } from "@/api/schemas";
import { createStore } from "vuex";
import { ReportsService } from "@/api/services/reports";

interface State {
  report: Report | null;
}

const SERVICE = new ReportsService();

export default createStore<State>({
  state: {
    report: null,
  },
  actions: {
    async fetchReport(context, id: number) {
      const data = await SERVICE.detail(id);
      context.commit("updateReport", data);
    },
  },
  mutations: {
    updateReport(state, report: Report) {
      state.report = report;
    },
  },
  getters: {
    report(state) {
      return state.report;
    },
  },
});
