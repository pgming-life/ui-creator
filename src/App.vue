<template>
  <v-app id="inspire">
    <v-card class="overflow-hidden">
      <v-app-bar
        absolute
        color="#A0522D"
        dark
        src="https://picsum.photos/1920/1080?random"
      >
        <template v-slot:img="{ props }">
          <v-img
            v-bind="props"
            gradient="to top right, rgba(255, 99, 71,.3), rgba(25,32,72,.7)"
          ></v-img>
        </template>
        <v-app-bar-title>
          <Icon/>
        </v-app-bar-title>
        <v-spacer></v-spacer>
        <template v-slot:extension>
          <v-tabs grow>
            <v-tab
              v-for="(link, index) in links"
              :key="index"
              :to="link.route"
              exact
            >
              {{ link.text }}
            </v-tab>
          </v-tabs>
        </template>
      </v-app-bar>
      <v-container style="height:120px;"></v-container>
    </v-card>
    <v-main>
      <transition>
        <router-view/>
      </transition>
    </v-main>
  </v-app>
</template>

<script>
import Icon from './components/Icon'
export default {
  name: 'App',
  components: {
    Icon,
  },
  data: () => ({
    links: [
      { text: "PROCESS", route: "/" },
      { text: "WORKSPACE", route: "/workspace" },
    ],
  }),
};
</script>

<style>
a {
  text-decoration:none;
}

.v-enter {
  transform: translate(-100px, 0);
  opacity: 0;
}
.v-enter-to {
  opacity: 1;
}
.v-enter-active {
  transition: all 1s 0s ease;
}
.v-leave {
  transform: translate(0, 0);
  opacity: 1;
}
.v-leave-to {
  transform: translate(100px, 0);
  opacity: 0;
}
.v-leave-active {
  transition: all .5s 0s ease;
}
</style>
