<template>
  <div class="about">
    <!-- <button @click="this.fetchDataTable()">Fetch Data</button> -->
    <div class="aboutTable">
      <table v-if="this.data!==null">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in this.data.data" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'AboutView',
  data(){
    return{
      data: null,
      token: null
    }
  },
  created(){
    this.token = localStorage.getItem('authToken');
    if (!this.token) {
      alert('Please log in first.');
      this.$router.push({ name: 'login' });
      return;
    }
    this.fetchDataTable();
  },
  methods: {
    fetchDataTable(){
      axios
        .post('http://localhost:5000/about',
          {},
          {
            headers: {
              'Authentication': `${this.token}`
            }
          }
        )
        .then(response => {
          if (response.status === 200) {
            this.data = response.data;
          } else {
            alert('Error: ' + response.status);
          }
        })
        .catch(error => {
          alert('Error: ' + error.response.status + ' - ' + error.response.data);
        })
    }
  }
}
</script>

<!-- <style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style> -->
