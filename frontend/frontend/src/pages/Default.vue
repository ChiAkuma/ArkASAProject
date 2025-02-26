<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div id="huu">
        <h1>This is the Default Component of this App</h1>
    </div>
    
    <span>Copy to clipboard:</span>
    <span class="box" v-on:click="copyText($event)">&nbsp;&#8209;{{ msg }}</span>
    <Table_ModList ref="table_modlist" v-on:data="(instance) => gmlsa(instance)" id="sizing"/>
</template>

<script setup>
    import Table_ModList from '@/components/ModList/List_Mods.vue';
</script>

<script>
    export default {
        data() {
            return {
                msg: ""
            }
        },
        methods: {
            gmlsa(instance) {
                this.msg = instance.getModServerArg();
            },
            copyText(event) {
                var text = event.originalTarget.innerText;
                navigator.clipboard.writeText(text);
            }
        }
    }
    
</script>

<style lang="scss" scoped>
    #sizing {
        height: 600px;
        width: 800px;
    }

    .box {
        display: block;
        background-color: #edf6ff;
        box-shadow: 1pt 1pt 1pt 1pt black;
        padding: 5pt;
        margin-bottom: 2pt;
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