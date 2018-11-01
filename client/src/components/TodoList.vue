<template>
  <div>
    <div v-for="todo in todos" v-bind:key="todo.id">
      <h1>{{ todo.title }}</h1>
      <p>{{ todo.contents }}</p>
    </div>
    <input type="text" name="title" v-model="title" />
    <input type="text" name="contents" v-model="contents" />
    <button class="btn btn-primary" v-on:click="createTodo">생성하기</button>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  data: function () {
    return {
      uri: 'https://wintercoding-server.run.goorm.io',
      todos: [],
      title: '',
      contents: '',
    }
  },
  methods: {
    readTodos: function() {
      this.$http.get(`${this.uri}/todos`)
      .then((result) => {
        this.todos = result.data;
      })
      .catch((error) => {
        console.log(error);
      });
    },
    createTodo: function () {
      this.$http.post(`${this.uri}/todos`, {
        title: this.title,
        contents: this.contents
      })
      .then((result) => {
        this.readTodos();
      })
      .catch((error) => {
        console.log(error);
      });
    }
  },
  mounted() {
    this.readTodos()
  }
}
</script>

<style scoped>
</style>
