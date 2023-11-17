<script lang="ts">
import { defineComponent } from "vue";
import ResizableTextarea from "@/components/ResizableTextarea.vue";
import { mapGetters } from "vuex";

export default defineComponent({
  name: "ReportTemplate",
  components: { ResizableTextarea },
  computed: mapGetters(["report"]),
});
</script>

<template>
  <div class="col-md-6">
    <div class="form-floating">
      <ResizableTextarea v-model="report.template" class="font-monospace" />
    </div>
  </div>
</template>
