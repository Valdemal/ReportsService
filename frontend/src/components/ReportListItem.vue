<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";

export default defineComponent({
  name: "ReportListItem",
  props: {
    report: {
      type: Report,
      required: true,
    },
  },
});
</script>

<template>
  <div class="col-md-6 col-lg-3 mb-4">
    <router-link
      class="link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"
      :to="{ name: 'report-detail', params: { pk: this.report.id } }"
    >
      <div class="report card">
        <div class="card-header">{{ report.name }}</div>
        <div class="card-body">
          <p class="card-text">
            {{ report.description }}
          </p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<style scoped></style>
