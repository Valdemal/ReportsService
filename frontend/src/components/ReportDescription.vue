<script lang="ts">
import { defineComponent } from "vue";
import ResizableTextarea from "@/components/ResizableTextarea.vue";
import { mapGetters } from "vuex";
import EditButton from "@/components/EditButton.vue";

interface State {
  descriptionEdits: boolean;
}

export default defineComponent({
  name: "ReportDescription",
  components: { EditButton, ResizableTextarea },
  data(): State {
    return {
      descriptionEdits: false,
    };
  },
  computed: mapGetters(["report"]),
});
</script>

<template>
  <div class="report-description">
    <div v-if="descriptionEdits" class="input-group">
      <!-- TODO: Лютейший костыль -->
      <ResizableTextarea v-model="report.description" />
      <edit-button @click="descriptionEdits = false" class="input-group-text" />
    </div>
    <div v-else-if="report.description">
      <p class="lead description-label">{{ report.description }}</p>
      <edit-button @click="descriptionEdits = true" />
    </div>
    <div v-else>
      <button
        type="button"
        class="btn btn-light"
        @click="
          descriptionEdits = true;
          report.description = 'Текст описания';
        "
      >
        Добавить описание
      </button>
    </div>
  </div>
</template>

<style scoped>
.report-description div {
  display: flex;
}

.description-label {
  margin-right: 2px;
}
</style>
