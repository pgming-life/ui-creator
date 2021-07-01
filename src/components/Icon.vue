<template>
	<v-img
    :src="icon_src"
    max-width="160"
  />
</template>

<script>
export default {
  data() {
    return {
      icon_src: require("@/assets/ui-creator.png")
    }
  }
};
</script>
