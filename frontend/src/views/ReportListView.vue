<template>
  <div class="row mt-4">
    <ReportListItem
      v-for="report in reports"
      :key="report.id"
      :report="report"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";
import { ReportsService } from "@/api/services/reports";
import ReportListItem from "@/components/ReportListItem.vue";

interface State {
  reports: Report[];
}

export default defineComponent({
  components: { ReportListItem },
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
