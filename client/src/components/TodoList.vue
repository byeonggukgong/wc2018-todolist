<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>2018 Winter Coding Web Assignment: Todo List</h1>
        <hr><br><br>
        <form class="form-inline">
          <input type="text" class="form-control form-rounded mr-sm-2" placeholder="Title" v-model="newTitle">
          <input type="text" class="form-control form-rounded mr-sm-2" placeholder="Contents" v-model="newContents">
          <button type="button" class="btn btn-info btn-sm" @click.prevent="createTodo">
            <i class="fas fa-pen"></i>
          </button>
        </form>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Done</th>
              <th scope="col">Title</th>
              <th scope="col">Contents</th>
              <th scope="col">Priority</th>
              <th scope="col">Deadline</th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="todo in todos" :key="todo.id">
              <td>
                <input type="checkbox" :checked="todo.is_done" @change="doneTodo(todo)" />
              </td>
              <td><input type="text" v-model="todo.title"></td>
              <td><input type="text" v-model="todo.contents"></td>
              <td><input type="text" v-model="todo.priority"></td>
              <td><datetime v-model="todo.deadline"></datetime></td>
              <td>
                <span class="badge badge-success" v-if="todo.is_done">Done :)</span>
                <span class="badge badge-danger" v-else-if="isDeadlineOver(todo)">Deadline is over :(</span>
              </td>
              <td>
                <button type="button" class="btn btn-warning btn-sm" @click.prevent="updateTodo(todo)">
                  <i class="fas fa-edit"></i>
                </button>
              </td>
              <td>
                <button type="button" class="btn btn-danger btn-sm" @click.prevent="deleteTodo(todo)">
                  <i class="fas fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row">
      
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
.form-rounded {
  border-radius: 1rem;
}
</style>
