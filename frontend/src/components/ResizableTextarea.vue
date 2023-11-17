<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ResizableTextarea",
  props: {
    modelValue: {
      required: true,
    },
    placeholder: {
      required: false,
    },
  },
  mounted() {
    this.resizeTextArea(this.$refs.textarea);
  },
  methods: {
    resizeTextArea(textArea: any) {
      textArea.style.height = "auto";
      const scHeight = textArea.scrollHeight;
      textArea.style.height = `${scHeight}px`;
    },
  },
  emits: ["update:modelValue"],
});
</script>

<template>
  <textarea
    class="form-control"
    ref="textarea"
    @placeholder="this.placeholder ? this.placeholder : 'Введите текст'"
    @keyup="resizeTextArea($event.target)"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  ></textarea>
</template>

<style scoped>
textarea {
  overflow: hidden;
  outline: none;
  resize: none;
}

textarea::-webkit-scrollbar(:focus, :valid) {
  width: 0;
}
</style>
