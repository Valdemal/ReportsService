<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";
import { ReportsService } from "@/api/services/reports";

export default defineComponent({
  name: "ReportListItem",
  props: {
    report: {
      type: Report,
      required: true,
    },
  },
  methods: {
    async removeReport() {
      try {
        const service = new ReportsService();
        await service.remove(this.report);
        this.$emit("removeReportFromList", this.report);
      } catch (e) {
        console.log(e);
      }
    },
  },
});
</script>

<template>
  <div class="col-md-6 col-lg-3 mb-4">
    <div class="report card">
      <div class="card-header d-flex justify-content-between">
        <router-link
          class="nav-link link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"
          :to="{ name: 'report-detail', params: { pk: this.report.id } }"
          >{{ report.name }}
        </router-link>
        <button type="button" class="btn-close" @click="removeReport"></button>
      </div>
      <div class="card-body">
        <p class="card-text">
          {{ report.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
