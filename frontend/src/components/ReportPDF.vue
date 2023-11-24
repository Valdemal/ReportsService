<template>
  <div class="col-md-6">
    <vue-pdf-embed :source="pdf" />
  </div>
</template>

<script>
import VuePdfEmbed from "vue-pdf-embed";
import { mapGetters } from "vuex";

export default {
  components: {
    VuePdfEmbed,
  },

  computed: mapGetters(["pdf"]),
};
</script>
