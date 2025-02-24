<template>
    <td>{{ index }}</td>
    <td>{{ mod["id"] }}</td>
    <td>{{ mod["name"] }}</td>
</template>

<script>
export default {
    emits: [],
    name: 'ModItem',
    data() {
        return {
            index: -1,
            mod: {}
        }
    }
}
</script>

<style>

</style>