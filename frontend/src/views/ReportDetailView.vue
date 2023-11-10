<script lang="ts">
import { defineComponent } from "vue";
import { Report } from "@/api/schemas";
import { ReportsService } from "@/api/services/reports";
import router from "@/router";
import _ from "lodash";

interface State {
  report: Report | null;
  initialReport: Report | null;
  nameEdit: boolean;
  descriptionsEdit: boolean;
}

export default defineComponent({
  name: "ReportDetailView",
  components: {},
  data(): State {
    return {
      report: null,
      initialReport: null,
      nameEdit: false,
      descriptionsEdit: false,
    };
  },
  async created() {
    const id = Number(this.$route.params.pk);

    try {
      this.initialReport = await new ReportsService().detail(id);
      this.report = this.initialReport.clone();
    } catch {
      await router.push({ name: "not-found" });
    }
  },
  updated() {
    const reportTemplateTextArea: HTMLTextAreaElement | null =
      document.querySelector(".resizable-textarea");

    if (reportTemplateTextArea) {
      this.resizeTextArea(reportTemplateTextArea);
    }
  },
  methods: {
    resizeTextArea(textArea: HTMLTextAreaElement) {
      const scHeight = textArea.scrollHeight;
      textArea.style.height = `${scHeight}px`;
    },
  },
  computed: {
    reportChanged(): boolean {
      return !_.isEqual(this.report, this.initialReport);
    },
  },
});
</script>

<template>
  <div v-if="this.report">
    <div class="row mt-2">
      <div class="report-header">
        <h2>{{ this.report.name }}</h2>
        <button v-if="reportChanged" type="button" class="btn btn-primary m-2">
          <img
            src="../assets/diskette-svgrepo-com.svg"
            width="35"
            height="35"
            alt="Кнопка сохранения отчета"
          />
        </button>
        <button type="button" class="btn btn-warning m-2">Предпросмотр</button>
      </div>
      <div class="report-description mb-2">
        <div v-if="descriptionsEdit" class="input-group">
          <textarea
            v-model="this.report.description"
            placeholder="Текст описания"
            class="form-control resizable-textarea"
          ></textarea>
          <span @click="descriptionsEdit = false" class="input-group-text">
            ✏
          </span>
        </div>
        <div v-else-if="this.report.description">
          <p class="lead">{{ this.report.description }}</p>
          <span @click="descriptionsEdit = true">✏</span>
        </div>
        <div v-else>
          <button
            type="button"
            class="btn btn-light"
            @click="
              descriptionsEdit = true;
              this.report.description = 'Текст описания';
            "
          >
            Добавить описание
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="form-floating">
          <textarea
            class="form-control font-monospace resizable-textarea"
            placeholder="RML-код шаблона"
            id="floatingTextarea2"
            @keyup="resizeTextArea($event.target)"
            v-model="this.report.template"
          ></textarea>
        </div>
      </div>
      <div class="col-md-6">Тут должен быть PDF</div>
    </div>
  </div>
</template>
<style scoped>
.report-header {
  display: flex;
}

.resizable-textarea {
  overflow: hidden;
  outline: none;
  resize: none;
}

.resizable-textarea::-webkit-scrollbar(:focus, :valid) {
  width: 0;
}

.report-description div {
  display: flex;
}
</style>
