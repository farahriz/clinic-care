<template>
    <h1>Add new consulation note</h1>
    <v-btn prepend-icon="mdi-content-save" color="primary" text="Save changes" class="mb-5" @click="saveChanges"></v-btn>
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

async function saveChanges(){
    return
}


</script>