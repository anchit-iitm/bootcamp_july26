<template>
    <div class="test">
        <h1>Test</h1>
        <input type="text" placeholder="Enter your name" v-model="this.name" />
        <button @click="this.testMethod()">Submit</button>
        <!-- <p>{{ this.name }}</p> -->
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'Test',
    data(){
        return {
                name: ''
            }
    },
    methods: {
        testMethod(){
            if (this.name === '') {
                alert('Please enter your name');
                return;
            }
            axios
                .post('http://localhost:5000/contact',
                    {
                        "name": this.name
                    }
                )
                .then(response => {
                    if (response.status === 200) {
                        alert(response.data.message);
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
<style></style>