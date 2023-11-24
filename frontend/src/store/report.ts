import { Report } from "@/api/schemas";
import { createStore } from "vuex";
import { ReportsService } from "@/api/services/reports";

interface State {
  report: Report | null;
  pdf: string | null;
}

const SERVICE = new ReportsService();

export default createStore<State>({
  state: {
    report: null,
    pdf: null,
  },
  actions: {
    async fetchReport(context, id: number) {
      const data = await SERVICE.detail(id);
      context.commit("updateReport", data);
      context.commit("updatePdf", null);
    },
    async saveReportOnServer(context) {
      if (context.state.report) {
        const newReport = await SERVICE.update(context.state.report);
        context.commit("updateReport", newReport);
      }
    },
    async printReportOnServer(context) {
      if (context.state.report){
        const pdf: string = await SERVICE.print(context.state.report)
        context.commit("updatePdf", `data:application/pdf;base64,${pdf}`)
      }
    }
  },
  mutations: {
    updateReport(state, report: Report) {
      state.report = report;
    },
    updatePdf(state, pdf: string) {
      state.pdf = pdf
    }
  },
  getters: {
    report(state) {
      return state.report;
    },
    pdf(state): string {
      return state.pdf
        ? state.pdf
        : "https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf";
    },
  },
});
