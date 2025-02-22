<template>
    <div>
        <!-- <button v-on:click="getModList()">ModList aktualisieren</button> -->
        <table>
            <tbody>
                <tr>
                    <th id="number">No.</th>
                    <th id="modid">ModId</th>
                    <th id="modname">ModName</th>
                </tr>
                
                <tr v-for="(value, key, index) in modlist" :key="key" v-on:click="selected($event, key)">
                    <td>{{ index }}</td>
                    <td>{{ key }}</td>
                    <td>{{ value }}</td>
                </tr>
            </tbody>

        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    emits: ['data'],
    name: 'ModList',
    data() {
        return {
            modlist: {}
        }
    },
    methods: {
        getModList() {
            const path = 'http://localhost:5000/modlist';
            // Backend connection to Flask
            axios.get(path)
            .then((res) => {
                console.log(res.data);
                this.modlist = res.data;
                console.log("INSIDE");
                this.$emit('data', this.modlist);
            })
            .catch((err) => {
                console.error(err);
            });    
        },
        getModServerArg() {
            
            var modarg = "";
            var modcache = [];

            console.log("logtest: " + this.modlist);
            console.log("logtest2: " + this.modlist[0]);
            var ob = Object.entries(this.modlist);
            console.log("ob: " + ob);
            console.log("obkey: " + ob.values());
            // TODO: Rausfinden ob nutzlos weil muss auf Server
            ob.values().forEach((mod, index) => {
                console.log("k:" + mod[0] + " v:" + mod[1] + " i:" + index);
                modcache.push(mod[0]);
            });
            console.log("mcc: " + modcache);
            modarg = "mods=" + modcache.join(',');
            console.log(modarg);
            return modarg;
        },
        selected(event, modid) {
            console.log("selected element: " + modid);
            console.log(event);
            event.currentTarget.classList.toggle('selected');
            // TODO: Finish selector
            // TODO: Adding to modlist
            // TODO: Remove from modlist when selected
        }
    },
    created() {
        this.getModList();
        
        console.log("OUTSIDE");
    }
}
// TODO: ModList table sorting
// TODO: ModList select item

</script>

<style lang="scss" scoped>
div{
    display: block;
    overflow: scroll;
}

table {
    border-collapse: collapse;
    margin: 0;
    top: 0;
    width: 100%;
}

td{
    border: 1px solid #ddd;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2;}
tr:hover {background-color: #ddd;}

th {
    //padding-top: 12px;
    //padding-bottom: 12px;
    padding: 8px;
    position: sticky;
    top: 0;

    text-align: left;
    background-color: #1d9240;
    color: white;

    font-size: large;
    font-weight: bolder;
}

#number {
    width: 0;
    //max-width: fit-content;
}

tbody .selected {
    background-color: #a0f8f8;
    border: #a0f8f8;
}

tbody .selected td {
    border: 1px solid #8ee1e1;
}

tbody .selected:nth-child(even) {
    background-color: #8ee1e1;
}

tbody .selected:nth-child(even) td {
    border: 1px solid #a0f8f8;
}
</style>