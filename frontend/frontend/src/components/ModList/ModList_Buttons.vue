<template>
    <footer>
        <button id="save">Save List</button>
        <button id="newmod">New Mod</button>
        <button id="deletemod">Delete Mod</button>
    </footer>
</template>

<script setup>

</script>

<style lang="scss" scoped>
    footer {
        display: flex;
        flex-direction: row;
        gap: 8px;

        padding: 5pt;

        border-left: 2px solid #4a4364;
        border-right: 2px solid #4a4364;
        border-bottom: 2px solid #4a4364;
        border-radius: 7pt;
    }
    button {
        padding: 8px 16px;
        width: 100%;
        border: none;
        border-radius: 4px;

        font-size: medium;

        cursor: pointer;
        transition: all 0.3s;
    }

    #save {
        background: #409eff;
        color: white;
    }

    #newmod {
        background: #48a544;
        color: white;
    }

    #deletemod {
        background: #dd6041;
        color: white;
    }


</style>