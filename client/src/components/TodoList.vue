<template>
  <div class="container">
    <form class="form-inline">
      <input type="text" class="form-control" placeholder="제목" v-model="newTitle">
      <label class="sr-only">Title</label>
      <input type="text" class="form-control" placeholder="내용" v-model="newContents">
      <label class="sr-only">Contents</label>
      <button class="btn btn-primary" @click.prevent="createTodo">생성하기</button>
    </form>
    <div class="row">
      <ul class="list-group">
        <li class="list-group-item" v-for="todo in todos" :key="todo.id">
          <div class="row">
            <div class="col">
              <input type="checkbox" :checked="todo.is_done" @change="doneTodo(todo)" />
            </div>
            <div class="col">
              <input type="text" v-model="todo.title">
            </div>
            <div class="col">
              <input type="text" v-model="todo.contents">
            </div>
            <div class="col">
              <input type="text" v-model="todo.priority">
            </div>
            <div class="col">
              <datetime v-model="todo.deadline"></datetime>
            </div>
            <div class="col" v-if=isDeadlineOver(todo)>
              <span>
                <i class="fas fa-bell"></i>
              </span>
            </div>
            <div class="col">
              <span>
                <a @click.prevent="updateTodo(todo)">
                  <i class="fas fa-hammer"></i>
                </a>
              </span>
            </div>
            <div class="col">
              <span>
                <a @click.prevent="deleteTodo(todo)">
                  <i class="fas fa-trash"></i>
                </a>
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { Datetime } from 'vue-datetime';

export default {
  name: 'TodoList',
  data: function () {
    return {
      apiBaseUrl: process.env.VUE_APP_API_BASE_URL,
      todos: [],
      newTitle: '',
      newContents: '',
    }
  },
  methods: {
    isDeadlineOver: function (todo) {
      const deadline = Date.parse(todo.deadline);
      const now = Date.parse(new Date());
     
      return now > deadline ? true : false;
    },
    readTodos: function() {
      this.$http.get(`${this.apiBaseUrl}/todos`)
      .then((result) => {
        this.todos = result.data;
      })
      .catch((error) => {
        console.log(error);
      });
    },
    createTodo: function () {
      this.$http.post(`${this.apiBaseUrl}/todos`, {
        title: this.newTitle,
        contents: this.newContents
      })
      .then((result) => {
        this.readTodos();
      })
      .catch((error) => {
        console.log(error);
      });
    },
    updateTodo: function (todo) {
      this.$http.put(`${this.apiBaseUrl}/todos/${todo.id}`, {
        ...todo,
        ...todo.deadline ?
          { deadline: todo.deadline } : { deadline: undefined }
      })
      .then((result) => {
        this.readTodos();
      })
      .catch((error) => {
          console.log(error);
      })
    },
    doneTodo: function (todo) {
      this.$http.patch(`${this.apiBaseUrl}/todos/${todo.id}`, {
        is_done: !todo.is_done
      })
      .then((result) => {
        todo.is_done = !todo.is_done;
      })
      .catch((error) => {
         console.log(error) ;
      });
    },
    deleteTodo: function (todo) {
      this.$http.delete(`${this.apiBaseUrl}/todos/${todo.id}`)
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
  },
  components: {
    datetime: Datetime
  }
}
</script>

<style scoped>
</style>
