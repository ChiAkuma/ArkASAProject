<template>
    <td id="ind">{{ index }}</td>
    <td>{{ mod["id"] }}</td>
    <td>{{ mod["name"] }}</td>
</template>

<script>
export default {
    emits: [],
    name: 'ModItem',
    props: {
        index: {
            type: Number,
            default: -1
        },
        mod: {
            type: {},
            default: {}
        }
    },
    data() {
        return {
            nth: true
        }
    },
    created() {
        if (this.index % 2 == 1) {
            this.nth = false;
        }
    }
}
</script>

<style lang="scss" scoped>

td {
    padding: 8px;
}

td:nth-child(1) {
    text-align: center;
}

/* ❗️ Zebra-Striping für Zeilen */
tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>