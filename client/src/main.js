import Vue from 'vue';
import App from './App.vue';

import axios from 'axios';

import Datetime from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css';

Vue.config.productionTip = false;

Vue.prototype.$http = axios;

Vue.use(Datetime);

new Vue({
  render: h => h(App),
}).$mount('#app');
