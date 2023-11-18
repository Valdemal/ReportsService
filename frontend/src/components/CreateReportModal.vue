<script lang="ts">
import { defineComponent } from "vue";
import ResizableTextarea from "@/components/ResizableTextarea.vue";
import { ReportsService } from "@/api/services/reports";
import router from "@/router";

interface State {
  name: string;
  description: string;
  errors: object;
}

export default defineComponent({
  name: "CreateReportModal",
  components: { ResizableTextarea },
  data(): State {
    return {
      name: "",
      description: "",
      errors: {},
    };
  },
  methods: {
    async modalSubmit() {
      try {
        const service = new ReportsService();
        const newReport = await service.create({
          name: this.name,
          description: this.description,
        });
        this.$store.commit("updateReport", newReport);
        this.closeModal();
        await router.push({
          name: `report-detail`,
          params: { pk: newReport.id },
        });
      } catch (error: any) {
        // eslint-disable-next-line
        this.errors = error.response.data;
      }
    },
    closeModal() {
      let htmlBodyElement = document.querySelector("body");

      if (htmlBodyElement) {
        htmlBodyElement.classList.remove("modal-open");
        let modalBackdrop = document.querySelector(".modal-backdrop");
        if (modalBackdrop) {
          modalBackdrop.remove();
        }
      }
    },
  },
});
</script>

<template>
  <div class="modal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Добавить отчет</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form action="#">
            <div class="mb-3">
              <label for="title" class="form-label">Название отчета</label>
              <input
                type="text"
                class="form-control"
                id="title"
                v-model="name"
              />
            </div>
            <div class="mb-3">
              <label for="description" class="form-label"
                >Описание отчета</label
              >
              <ResizableTextarea v-model="description" id="description" />
            </div>
            <div v-if="Object.keys(errors).length">
              {{ errors }}
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Закрыть
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click.capture="modalSubmit"
          >
            Ок
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
