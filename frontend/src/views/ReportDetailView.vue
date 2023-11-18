<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";
import router from "@/router";
import _ from "lodash";
import ReportDescription from "@/components/ReportDescription.vue";
import { mapActions, mapGetters } from "vuex";
import ReportTemplate from "@/components/ReportTemplate.vue";
import ReportPDF from "@/components/ReportPDF.vue";
import ReportTitle from "@/components/ReportTitle.vue";

interface State {
  initialReport: Report | null;
}

export default defineComponent({
  name: "ReportDetailView",
  components: { ReportTitle, ReportPDF, ReportTemplate, ReportDescription },
  data(): State {
    return {
      initialReport: null,
    };
  },
  async created() {
    const id = Number(this.$route.params.pk);

    try {
      await this.fetchReport(id);
      this.initialReport = this.report.clone();
    } catch {
      await router.push({ name: "not-found" });
    }
  },
  methods: {
    ...mapActions(["fetchReport", "saveReportOnServer"]),
    printReport() {
      console.log(this.report);
    },
    async saveReport() {
      try {
        await this.saveReportOnServer();
        this.initialReport = this.report.clone();
      } catch (e) {
        console.log(e);
      }
    },
  },
  computed: {
    ...mapGetters(["report"]),
    reportChanged(): boolean {
      return (
        this.initialReport != null &&
        !_.isEqual(this.report, this.initialReport)
      );
    },
  },
});
</script>

<template>
  <div v-if="report">
    <div class="row mt-2">
      <div class="report-header">
        <ReportTitle />
        <button type="button" class="btn btn-warning m-2" @click="printReport">
          Предпросмотр
        </button>
        <button
          v-if="reportChanged"
          type="button"
          class="btn btn-primary m-2"
          @click="saveReport"
        >
          <img
            src="../assets/diskette-svgrepo-com.svg"
            width="35"
            height="35"
            alt="Кнопка сохранения отчета"
          />
        </button>
      </div>
    </div>
    <ReportDescription class="mb-2" />
    <div class="row">
      <ReportTemplate />
      <ReportPDF />
    </div>
  </div>
</template>

<style scoped>
.report-header {
  display: flex;
}
</style>
