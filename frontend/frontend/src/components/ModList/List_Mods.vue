<template>
    <div class="modlist_content">
        <!-- Dialog wird angezeigt wenn drag and drop event ausgeführt wird. Oder ein anderes Mod änderndes event -->
        <ConfirmationDialog v-on:confirm="performDrop()" v-on:cancel="cancelDrop()" v-model="showConfirmation"
            :visible="showConfirmation" @confirm="performDrop()" @cancel="cancelDrop()">
            <template v-slot:content>
                Möchten Sie diese Aktion wirklich durchführen?<br>
                Du könntest hierbei deine Mods in die falsche Reihenfolge bringen!
            </template>
        </ConfirmationDialog>
        <div class="list">
            <!-- Deaktivierter Refresh-Button -->
            <!-- <button v-on:click="getModList()">ModList aktualisieren</button> -->
            <table>
                <tbody>
                    <!-- Tabellenkopf mit Spaltenüberschriften -->
                    <tr>
                        <th id="number">No.</th> <!-- Indexspalte -->
                        <th id="modid">ModId</th> <!-- Mod-ID Spalte -->
                        <th id="modname">ModName</th> <!-- Modname Spalte -->
                    </tr>

                    <!-- Dynamische Zeilen für Modliste -->
                    <tr v-for="(mod, index) in modlist" :key="mod['id']" v-on:click="select_item($event, index)"
                        draggable="true" @dragstart="onDrag($event, index)" @drop="onDrop($event, 1)"
                        @dragover.prevent="onDragover($event, index)" @dragend="onDragend($event, index)" :class="{
                            'drag-start': index === oldIndex,
                            'drag-over': index === newIndex,
                            'selected': index === selected,
                        }">
                        <!-- Zeileninhalte -->
                        <Item_Mod :index="index" :mod="mod"></Item_Mod>
                    </tr>
                </tbody>
            </table>
        </div>
        <SaveModList></SaveModList>
    </div>
</template>


<script setup>
import ConfirmationDialog from '@/components/ConfirmationDialog.vue';
import SaveModList from '@/components/ModList/ModList_Buttons.vue';
import Item_Mod from '@/components/ModList/Item_Mod.vue';
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
            oldIndex: null, // Drag-Startposition
            newIndex: null, // Drag-Zielposition
            selected: null, // Ausgewählter Index
            showConfirmation: false,
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
                    this.$emit('data', this);
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
            if (this.oldIndex == this.newIndex) return;
            this.showConfirmation = true;
        },
        performDrop() {
            console.log("dropping performed");
            // Array-Operation zum Verschieben
            const removed = this.modlist.splice(this.oldIndex, 1)[0];
            this.modlist.splice(this.newIndex, 0, removed);
            this.showConfirmation = false;
            this.oldIndex = null;
            this.newIndex = null;
            this.$emit('data', this);
        },
        cancelDrop() {
            console.log("confirmation canceled... cleaning up...");
            this.showConfirmation = false;
            this.oldIndex = null;
            this.newIndex = null;
            this.$emit('data', this);
        },
        onDragend() {
            this.selected = null;
            if (!this.showConfirmation) {
                this.oldIndex = null;
                this.newIndex = null;
            }
            this.$emit('data', this);
        }
    },
    created() {
        // Initialer Datenabruf
        this.getModList();
    }
}
</script>

<style lang="scss" scoped>
.modlist_content {
    width: 150%;
    height: 100vh;
    max-height: inherit;
}

/* ❗️ Scrollcontainer für Tabelle */
.list {
    border-radius: 7pt;
    border: 2px solid #4a4364;

    overflow: scroll;
    user-select: none;

    height: inherit;
    max-height: inherit;
    /* Verhindert Textauswahl */
}

/* ❗️ Basis-Tabellenformatierung */
table {
    border-collapse: collapse;
    margin: 0;
    width: 100%;
}

tbody {
    height: inherit;
}

/* ❗️ Tabellensticky-Header */
th {
    position: sticky;
    top: 0;
    /* Fixiert Header beim Scrollen */
    padding: 8pt;
    background-color: #4a4364;
    color: white;
    font-weight: bold;
}

/* ❗️ Drag & Drop Visuals */
.drag-start {
    background-color: #275c91 !important;
    color: white;
    /* Hervorgehobenes ziehendes Element */
}

.drag-over {
    outline: 2px dashed black !important;
    /* Drop-Zielmarkierung */
    color: #ab3232;
}

tr:hover {
    background-color: #706494;
    color: white;
}

/* ❗️ Zeilenselektion */
.selected {
    background-color: #706494;
    color: white;
}

.selected:nth-child(even) {
    background-color: #706494;
}

/* ❗️ Spaltenbreite für Index-Spalte */
#number {
    width: 0;
}
</style>