<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div id="huu">
        <h1>This is the Default Component of this fucking thing in this elaborate hindum</h1>
    </div>
    
    <p>{{ msg }}</p>
    <Table_ModList @data="whaa('data')" ref="mlist" id="sizing"/>
</template>

<script setup>
    import Table_ModList from '@/components/Table_ModList.vue';
</script>

<script>
    export default {
        data() {
            return {
                msg: ""
            }
        },
        methods: {
            whaa(data) {
                console.log(data);
                this.msg = this.$refs.mlist.getModServerArg();
            }
        }
    }
    
</script>

<style lang="scss" scoped>
    #sizing {
        max-width: fit-content;
        max-height: 400pt;
    }

    #huu {
        margin: 0;
    }

    h1 {
        margin: 0;
        padding-left: 5px;
    }

    p {
        padding-left: 5px;;
    }
</style>