<template>
  <v-btn
    fab
    elevation="7"
    x-large
    color="#008099"
    @click="sendMessages"
  >
    <span style="color:white;">適用</span>
  </v-btn>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'TemplateAccess',
  methods: {
    sendMessages: function() {
      this.$emit("clearStack");
      this.$emit('catchMessages', this.messages)
    },
  },
  computed: mapState({
      messages: state => state.messages.messages
  }),
  created() {
    this.$store.dispatch('messages/getMessages')
  },
};
</script>
