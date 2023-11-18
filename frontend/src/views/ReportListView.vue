<template>
  <div class="row">
    <div class="col-md-6 col-lg-3">
      <button
        type="button"
        class="btn btn-secondary"
        data-bs-toggle="modal"
        data-bs-target="#createReportModal"
      >
        Добавить отчет
      </button>
    </div>
  </div>
  <div class="row mt-4">
    <ReportListItem
      v-for="report in reports"
      :key="report.id"
      :report="report"
    />
  </div>
  <CreateReportModal id="createReportModal" />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";
import { ReportsService } from "@/api/services/reports";
import ReportListItem from "@/components/ReportListItem.vue";
import CreateReportModal from "@/components/CreateReportModal.vue";

interface State {
  reports: Report[];
}

export default defineComponent({
  components: { CreateReportModal, ReportListItem },
  data(): State {
    return {
      reports: [],
    };
  },
  async created() {
    try {
      this.reports = await new ReportsService().list();
    } catch (error) {
      console.log(error);
    }
  },
});
</script>

<style scoped></style>
