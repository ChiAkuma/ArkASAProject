<!-- eslint-disable no-unused-vars -->
<script setup>
import Table_ModList from '@/components/ModList/List_Mods.vue';
</script>

<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable vue/multi-word-component-names -->
<script>
import axios from 'axios';
import { onMounted } from 'vue';


export default {
    name: 'Shark',
    data() {
        return {
            msg: "",
            modlist: {}
        }
    },
    methods: {
        getResponse() {
            const path = 'http://localhost:5000/shark';
            // Backend connection to Flask
            axios.get(path)
            .then((res) => {
                console.log(res.data);
                this.msg = res.data;
            })
            .catch((err) => {
                console.error(err);
            });
        },
        home() {
            const path = 'http://localhost:5000/';
            // Backend connection to Flask
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
        <button v-on:click="home();">Home</button>
        <Table_ModList />
    </div>
</template>

<style scoped>
p {
    margin: 5px;
}
</style>