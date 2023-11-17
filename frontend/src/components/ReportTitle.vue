<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";
import EditButton from "@/components/EditButton.vue";

interface State {
  titleEdits: boolean;
}

export default defineComponent({
  name: "ReportTitle",
  components: { EditButton },
  data(): State {
    return {
      titleEdits: false,
    };
  },
  computed: mapGetters(["report"]),
});
</script>

<template>
  <div class="col-md-6">
    <div v-if="titleEdits" class="input-group input-group-lg">
      <input
        type="text"
        class="form-control"
        v-model="report.name"
        placeholder="Название отчета"
      />
      <edit-button @click="titleEdits = false" class="input-group-text" />
    </div>
    <div v-else class="d-flex align-middle">
      <h2>{{ report.name }}</h2>
      <edit-button @click="titleEdits = true" />
    </div>
  </div>
</template>

<style scoped></style>
