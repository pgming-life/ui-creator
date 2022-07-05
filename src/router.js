import Vue from 'vue'
import Router from 'vue-router'
const WorkSpace = () => import('@/components/WorkSpace.vue')
const Process = () => import('@/components/Process.vue')

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'process',
      component: Process,
    },
    {
      path: '/workspace',
      name: 'workspace',
      component: WorkSpace,
    },
  ],
})
