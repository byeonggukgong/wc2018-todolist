<template>
  <div>
    <input type="text" name="title" v-model="title" />
    <input type="text" name="contents" v-model="contents" />
    <button class="btn btn-primary" v-on:click="createTodo">생성하기</button>
    <div v-for="todo in todos" v-bind:key="todo.id">
      <h1>{{ todo.title }}</h1>
      <p>{{ todo.contents }}</p>
      <input type="checkbox" name="is_done" v-bind:value="todo.is_done" v-model="todo.is_done" />
      <button class="btn btn-primary" v-on:click="updateTodo(todo)">수정하기</button>
      <button class="btn btn-primary" v-on:click="deleteTodo(todo)">삭제하기</button>
    </div>
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
    },
    updateTodo: function (todo) {
      this.$http.put(`${this.uri}/todos/${todo.id}`, {
        title: todo.title,
        contents: todo.contents,
        deadline: todo.deadline,
        priority: todo.priority,
        is_done: todo.is_done
      })
      .then((result) => {
        this.readTodos();
      })
      .catch((error) => {
          console.log(error);
      })
    },
    deleteTodo: function (todo) {
      this.$http.delete(`${this.uri}/todos/${todo.id}`)
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
