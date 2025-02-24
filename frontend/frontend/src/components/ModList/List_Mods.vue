<template>
    <div>
        <!-- Deaktivierter Refresh-Button -->
        <!-- <button v-on:click="getModList()">ModList aktualisieren</button> -->
        
        <table>
            <tbody>
                <!-- Tabellenkopf mit Spaltenüberschriften -->
                <tr>
                    <th id="number">No.</th>  <!-- Indexspalte -->
                    <th id="modid">ModId</th> <!-- Mod-ID Spalte -->
                    <th id="modname">ModName</th> <!-- Modname Spalte -->
                </tr>
                
                <!-- Dynamische Zeilen für Modliste -->
                <tr 
                    v-for="(mod, index) in modlist" 
                    :key="mod['id']"
                    v-on:click="select_item($event, index)"
                    draggable="true"
                    @dragstart="onDrag($event, index)"
                    @drop="onDrop($event, 1)"
                    @dragover.prevent="onDragover($event, index)"
                    @dragend="onDragend($event, index)"
                    :class="{
                        'drag-start': index === oldIndex,
                        'drag-over': index === newIndex,
                        'selected': index === selected,
                    }"
                >
                    <!-- Zeileninhalte -->
                    <td>{{ index }}</td> <!-- Laufende Nummer -->
                    <td>{{ mod["id"] }}</td> <!-- Mod-ID Anzeige -->
                    <td>{{ mod["name"] }}</td> <!-- Modname Anzeige -->
                </tr>
            </tbody>
        </table>
        <ConfirmationDialog v-model="showConfirmation" @confirm="performDrop()" @cancel="cancelDrop()">
            <template v-slot:content>
                Möchten Sie diese Aktion wirklich durchführen?<br>
                Du könntest hierbei deine Mods in die falsche Reihenfolge bringen!
            </template>
        </ConfirmationDialog>
    </div>
</template>


<script setup>
    import ConfirmationDialog from '../ConfirmationDialog.vue';
</script>

<script>
/* 
  ❗️ Komponentenlogik
  - Verwaltet Modliste mit Drag & Drop
  - Kommuniziert mit Flask-Backend
  - Emittet Änderungen an Parent-Komponente

*/
import axios from 'axios';

export default {
    emits: ['data'],
    name: 'ModList',
    data() {
        return {
            modlist: [],   // Gespeicherte Modliste
            oldIndex:null, // Drag-Startposition
            newIndex:null, // Drag-Zielposition
            selected:null, // Ausgewählter Index
            showConfirmation:false,
        }
    },
    methods: {
        // API-Abruf für Modliste
        getModList() {
            const path = 'http://localhost:5000/modlist';
            axios.get(path)
            .then((res) => {
                // Transformiert Serverresponse
                for (let index = 0; index < Object.keys(res.data).length; index++) {
                    this.modlist[index] = res.data[index]
                }
                this.$emit('data', this.modlist);
            })
            .catch((err) => {
                console.error("API Error: " + err);
            });    
        },
        // Erstellt Server-Parameter String
        getModServerArg() {
            let modarg = "mods=";
            const modcache = this.modlist.map(mod => mod.id);
            return modarg + modcache.join(',');
        },

        // Zeilenauswahl-Handler
        select_item(event, index) {
            this.selected = index;
        },

        // Drag & Drop Event-Handler
        onDrag(evt, oldIndex) {
            this.selected = null;
            this.oldIndex = oldIndex;
            evt.dataTransfer.effectAllowed = 'move';
        },

        onDragover(evt, newIndex) {
            this.newIndex = newIndex;
        },

        onDrop() {
            // Abfrage von ConfirmationDialog
            this.showConfirmation = true;
        },
        performDrop() {
            // Array-Operation zum Verschieben
            const removed = this.modlist.splice(this.oldIndex, 1)[0];
            this.modlist.splice(this.newIndex, 0, removed);
        },
        cancelDrop() {
            console.log("confirmation canceled... doing nothing");
        },
        onDragend() {
            this.selected = null;
            this.oldIndex = null;
            this.newIndex = null;
            this.$emit('data', this.modlist);
        }
    },
    created() {
        // Initialer Datenabruf
        this.getModList();
    }
}
</script>

<style lang="scss" scoped>
/* ❗️ Scrollcontainer für Tabelle */
div{
    display: block;
    overflow: scroll;
    user-select:none; /* Verhindert Textauswahl */
}

/* ❗️ Tabellensticky-Header */
th {
    position: sticky;
    top: 0; /* Fixiert Header beim Scrollen */
    padding: 8px;
    background-color: #1d9240;
    color: white;
    font-size: large;
    font-weight: bolder;
}

/* ❗️ Drag & Drop Visuals */
.drag-start {
    background-color: gold !important; /* Hervorgehobenes ziehendes Element */
}

.drag-over {
    outline: 2px dashed black !important; /* Drop-Zielmarkierung */
    color: #ab3232;
}

/* ❗️ Basis-Tabellenformatierung */
table {
    border-collapse: collapse;
    margin: 0;
    width: 100%;
}

td {
    border: 1px solid #ddd;
    padding: 8px;
}

/* ❗️ Zebra-Striping für Zeilen */
tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}

/* ❗️ Zeilenselektion */
.selected {
    background-color: #a0f8f8;
    border: #a0f8f8;
}

.selected td {
    border: 1px solid #8ee1e1;
}

.selected:nth-child(even) {
    background-color: #8ee1e1;
}

.selected:nth-child(even) td {
    border: 1px solid #a0f8f8;
}

/* ❗️ Spaltenbreite für Index-Spalte */
#number {
    width: 0;
}
</style>