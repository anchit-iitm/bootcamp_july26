<template>
    <div class="login">
        <div class="loginForm">
            <h1>Login</h1>
            <input type="email" placeholder="Enter your email" v-model="this.mail" /> <br><br>
            <input type="password" placeholder="Enter your password" v-model="this.password" />
            <button @click="this.loginMethod()">Login</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'Login',
    data(){
        return {
            mail: '',
            password: ''
        }
    },
    methods: {
        loginMethod(){
            if (this.mail === '' || this.password === '') {
                alert('Please enter your mail and password');
                return;
            }
            axios
                .post('http://localhost:5000/login',
                    {
                        "email": this.mail,
                        "password": this.password
                    }
                )
                .then(response => {
                    if (response.status === 200) {
                        localStorage.setItem('authToken', response.data.authToken);
                        localStorage.setItem('user_email', response.data.email);
                        localStorage.setItem('user_id', response.data.user_id);
                        this.mail='';
                        this.password='';
                        this.$router.push({ name: 'about'})
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