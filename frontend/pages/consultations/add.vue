<template>
    <h1>Add new consulation note</h1>
    <ConsultationForm :readonly="false" v-model:consultNoteData="consultNoteData"/>
</template>

<script setup lang="ts">
const route = useRoute()

const consultNoteData = ref({
    patient: "",
    consultDate: "",
    code: "",
    description: ""
})


</script>