<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable vue/multi-word-component-names -->
<script>
import axios from 'axios';
import { onMounted } from 'vue';


export default {
    name: 'Shark',
    data() {
        return {
            msg: ""
        }
    },
    methods: {
        getResponse() {
            const path = 'http://localhost:5000/shark';
            axios.get(path)
            .then((res) => {
                console.log(res.data);
                this.msg = res.data;
            })
            .catch((err) => {
                console.error(err);
            });
        }
    },
    created() {
        this.getResponse();
    }
}
</script>

<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<style scoped>
</style>