<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ResizableTextarea",
  props: {
    modelValue: {
      required: true,
    },
  },
});
</script>

<template>Напишу что-нибудь</template>

<style scoped>
.resizable-textarea {
  overflow: hidden;
  outline: none;
  resize: none;
}

.resizable-textarea::-webkit-scrollbar(:focus, :valid) {
  width: 0;
}
</style>
